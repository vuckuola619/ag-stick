import os
import sys
import time
import argparse
import mimetypes
from typing import Dict, List, Optional, Tuple

# Ensure utf-8 stdout on Windows
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Google API client imports
try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from googleapiclient.errors import HttpError
except ImportError as e:
    print(f"[ERROR] Missing required Google API libraries: {e}", file=sys.stderr)
    print("Run: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib", file=sys.stderr)
    sys.exit(1)

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLIENT_SECRET_FILE = os.path.join(REPO_ROOT, "google.json")
TOKEN_FILE = os.path.join(REPO_ROOT, "token.json")
PROJECTS_DIR = os.path.join(REPO_ROOT, "projects")

def authenticate():
    """Authenticates using google.json and caches token in token.json."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
            print(f"[AUTH] Found existing credentials in {TOKEN_FILE}", flush=True)
        except Exception as e:
            print(f"[WARN] Failed to load token.json: {e}", flush=True)
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("[AUTH] Refreshing expired credentials...", flush=True)
            try:
                creds.refresh(Request())
                print("[AUTH] Successfully refreshed credentials.", flush=True)
            except Exception as e:
                print(f"[WARN] Failed to refresh token: {e}. Starting fresh auth flow...", flush=True)
                creds = None

        if not creds:
            if not os.path.exists(CLIENT_SECRET_FILE):
                raise FileNotFoundError(f"OAuth client secrets file not found: {CLIENT_SECRET_FILE}")

            print("[AUTH] Starting browser-based OAuth 2.0 authorization...", flush=True)
            print("[AUTH] A browser window should open automatically to approve access.", flush=True)
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials for future runs
        with open(TOKEN_FILE, "w", encoding="utf-8") as token_out:
            token_out.write(creds.to_json())
        print(f"[AUTH] Credentials saved securely to {TOKEN_FILE}", flush=True)

    return build('drive', 'v3', credentials=creds)

def find_folder(service, name: str, parent_id: Optional[str] = None) -> Optional[str]:
    """Finds an existing active folder by name and optional parent_id."""
    query = f"mimeType = 'application/vnd.google-apps.folder' and name = '{name}' and trashed = false"
    if parent_id:
        query += f" and '{parent_id}' in parents"

    results = service.files().list(
        q=query,
        spaces='drive',
        fields='files(id, name, parents)',
        pageSize=10
    ).execute()

    files = results.get('files', [])
    if files:
        return files[0]['id']
    return None

def create_folder(service, name: str, parent_id: Optional[str] = None) -> str:
    """Creates a new folder on Google Drive."""
    meta = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        meta['parents'] = [parent_id]

    folder = service.files().create(body=meta, fields='id, name').execute()
    print(f"  [GDRIVE] Created folder: '{name}' (ID: {folder['id']})", flush=True)
    return folder['id']

def get_or_create_folder(service, name: str, parent_id: Optional[str] = None) -> str:
    """Gets existing folder or creates it if missing."""
    fid = find_folder(service, name, parent_id)
    if fid:
        return fid
    return create_folder(service, name, parent_id)

def list_folder_files(service, folder_id: str) -> Dict[str, Dict]:
    """Lists existing files in a folder to enable deduplication."""
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed = false",
        spaces='drive',
        fields='files(id, name, size, md5Checksum)',
        pageSize=100
    ).execute()
    return {f['name']: f for f in results.get('files', [])}

def upload_file_resumable(service, local_path: str, folder_id: str, display_name: Optional[str] = None) -> str:
    """Uploads a file using resumable upload with live chunk progress."""
    filename = display_name or os.path.basename(local_path)
    file_size = os.path.getsize(local_path)
    mime_type, _ = mimetypes.guess_type(local_path)
    if not mime_type:
        mime_type = "application/octet-stream"

    # Check deduplication
    existing = list_folder_files(service, folder_id)
    if filename in existing:
        remote_size = int(existing[filename].get('size', 0))
        if remote_size == file_size:
            print(f"  [SKIP] '{filename}' already exists on Drive ({file_size/(1024*1024):.2f} MB). Skipping.", flush=True)
            return existing[filename]['id']

    file_metadata = {
        'name': filename,
        'parents': [folder_id]
    }

    # 10MB chunk size for smooth progress & fast throughput
    media = MediaFileUpload(local_path, mimetype=mime_type, resumable=True, chunksize=10*1024*1024)
    request = service.files().create(body=file_metadata, media_body=media, fields='id, name')

    print(f"  [UPLOAD] Starting: '{filename}' ({file_size/(1024*1024):.2f} MB)...", flush=True)
    response = None
    start_time = time.time()

    while response is None:
        status, response = request.next_chunk()
        if status:
            progress = status.progress() * 100
            elapsed = time.time() - start_time
            uploaded_mb = (status.resumable_progress or 0) / (1024 * 1024)
            total_mb = file_size / (1024 * 1024)
            speed_mb = (uploaded_mb / elapsed) if elapsed > 0 else 0
            print(f"    --> {progress:5.1f}% [{uploaded_mb:.1f} / {total_mb:.1f} MB] @ {speed_mb:.1f} MB/s", flush=True)

    elapsed_total = time.time() - start_time
    avg_speed = (file_size / (1024 * 1024)) / elapsed_total if elapsed_total > 0 else 0
    print(f"  [OK] Uploaded '{filename}' in {elapsed_total:.1f}s (Avg: {avg_speed:.1f} MB/s) | File ID: {response.get('id')}", flush=True)
    return response.get('id')

def discover_project_ready_assets(project_key: Optional[str] = None) -> Dict[str, Dict[str, List[str]]]:
    """
    Discovers all publish-ready and clean assets organized by project and category.
    Returns:
    {
      "YTF - AG-Stick - case-05-goiania-caesium": {
         "01_Master_Videos": [...],
         "02_Shorts_Vertical": [...],
         "03_Thumbnails": [...],
         "04_Metadata_and_Scripts": [...]
      }, ...
    }
    """
    inventory: Dict[str, Dict[str, List[str]]] = {}

    # Define projects to scan
    target_dirs = []
    for d in sorted(os.listdir(PROJECTS_DIR)):
        dp = os.path.join(PROJECTS_DIR, d)
        if os.path.isdir(dp):
            target_dirs.append((d, dp))

    for proj_name, proj_path in target_dirs:
        # Check sub-case projects (like the-dossier-zero/case-05-goiania-caesium)
        subcases = []
        if os.path.exists(os.path.join(proj_path, "case-05-goiania-caesium")):
            subcases.append(("the-dossier-zero-case-05-goiania", os.path.join(proj_path, "case-05-goiania-caesium"), proj_path))
        else:
            subcases.append((proj_name, proj_path, None))

        for sub_name, sub_path, parent_brand_path in subcases:
            # Filter if project_key specified
            if project_key:
                pk = project_key.lower()
                if pk not in sub_name.lower() and pk not in proj_name.lower():
                    continue

            folder_title = f"YTF - AG-Stick - {sub_name}"

            categories = {
                "01_Master_Videos": [],
                "02_Shorts_Vertical": [],
                "03_Thumbnails": [],
                "04_Metadata_and_Scripts": []
            }

            for root, dirs, files in os.walk(sub_path):
                # Skip build/cache/remotion workspace directories
                if any(k in root.split(os.sep) for k in ['node_modules', '.git', '.remotion', 'temp', '__pycache__', 'remotion', 'node_modules']):
                    continue

                for f in files:
                    fp = os.path.join(root, f)
                    f_lower = f.lower()

                    # 1. Master Videos
                    if f_lower.endswith('.mp4'):
                        if 'short' in f_lower or 'tiktok' in f_lower:
                            if 'master' in f_lower or 'final' in f_lower:
                                categories["02_Shorts_Vertical"].append(fp)
                        elif 'master' in f_lower or 'final' in f_lower:
                            categories["01_Master_Videos"].append(fp)

                    # 2. Thumbnails & Art
                    elif f_lower.endswith(('.png', '.jpg', '.webp')):
                        if any(k in f_lower for k in ['thumb', 'cover', 'banner', 'watermark']):
                            # Exclude temporary test frames
                            if not any(k in f_lower for k in ['test_', 'preview_', 'frame_']):
                                categories["03_Thumbnails"].append(fp)

                    # 3. Metadata & Scripts
                    elif f_lower.endswith(('.md', '.json', '.txt')):
                        if any(k in f_lower for k in ['metadata', 'script', 'storyboard', 'guide', 'manifest']):
                            if not any(k in f_lower for k in ['package.json', 'package-lock.json', 'tsconfig']):
                                categories["04_Metadata_and_Scripts"].append(fp)

            # Also scan parent brand folder for banners/profile/watermarks
            if parent_brand_path:
                brand_assets_dir = os.path.join(parent_brand_path, "assets")
                if os.path.exists(brand_assets_dir):
                    for f in os.listdir(brand_assets_dir):
                        if any(k in f.lower() for k in ['banner', 'profile', 'watermark']) and f.lower().endswith(('.png', '.jpg')):
                            categories["03_Thumbnails"].append(os.path.join(brand_assets_dir, f))
                brand_guide = os.path.join(parent_brand_path, "BRAND_GUIDE.md")
                if os.path.exists(brand_guide):
                    categories["04_Metadata_and_Scripts"].append(brand_guide)

            # Filter master videos to only final/fixed versions (filter out older drafts if final/v5 exists)
            cleaned_master = []
            for v in categories["01_Master_Videos"]:
                v_name = os.path.basename(v).lower()
                if any(k in v_name for k in ['_v1.', '_v2.', '_v3.', '_v4.', '_raw.']):
                    if any('_v5' in os.path.basename(x).lower() or 'final' in os.path.basename(x).lower() for x in categories["01_Master_Videos"]):
                        continue
                if v_name == 'scaling_10m_master.mp4' or v_name == 'scaling_10m_master_voiced.mp4':
                    if any('final' in os.path.basename(x).lower() or '_v5' in os.path.basename(x).lower() for x in categories["01_Master_Videos"]):
                        continue
                cleaned_master.append(v)
            categories["01_Master_Videos"] = cleaned_master

            # Filter shorts to only final/fixed versions
            cleaned_shorts = []
            for s in categories["02_Shorts_Vertical"]:
                s_name = os.path.basename(s).lower()
                if any(k in s_name for k in ['_v1.', '_v2.', '_v3.', '_v4.']):
                    if any('_v5' in os.path.basename(x).lower() or 'final' in os.path.basename(x).lower() for x in categories["02_Shorts_Vertical"]):
                        continue
                if 'kokoro' in s_name and any('master' in os.path.basename(x).lower() for x in categories["02_Shorts_Vertical"]):
                    continue
                cleaned_shorts.append(s)
            categories["02_Shorts_Vertical"] = cleaned_shorts

            # Deduplicate file lists
            for c in categories:
                categories[c] = sorted(list(set(categories[c])))

            # Keep only projects that actually have publish-ready content
            total_items = sum(len(v) for v in categories.values())
            if categories["01_Master_Videos"] or (categories["02_Shorts_Vertical"] and categories["03_Thumbnails"]):
                inventory[folder_title] = categories

    return inventory

def main():
    parser = argparse.ArgumentParser(description="Upload publish-ready AG-Stick assets to Google Drive")
    parser.add_argument("--project", "-p", type=str, help="Filter specific project (e.g. goiania, midgley, demon-core)")
    parser.add_argument("--dry-run", action="store_true", help="List discoverable files without uploading")
    parser.add_argument("--auth-only", action="store_true", help="Authenticate with google.json and test Drive API connection without uploading")
    parser.add_argument("--parent-folder", type=str, default="YTF - AG-Stick", help="Root folder name on Google Drive")
    args = parser.parse_args()

    print("=======================================================================", flush=True)
    print("=== AG-Stick Google Drive Publisher                                 ===", flush=True)
    print("=== Target Folder: 'YTF - AG-Stick - project xxx'                    ===", flush=True)
    print("=======================================================================\n", flush=True)

    if args.auth_only:
        service = authenticate()
        about = service.about().get(fields="user, storageQuota").execute()
        user = about.get('user', {})
        quota = about.get('storageQuota', {})
        print(f"\n[GDRIVE] Authenticated as: {user.get('displayName')} ({user.get('emailAddress')})", flush=True)
        if 'limit' in quota:
            used_gb = int(quota.get('usage', 0)) / (1024**3)
            limit_gb = int(quota.get('limit', 0)) / (1024**3)
            print(f"[GDRIVE] Storage Quota: {used_gb:.2f} GB / {limit_gb:.2f} GB used", flush=True)
        print("[GDRIVE] Authentication verified successfully!\n", flush=True)
        return

    # 1. Scan local assets
    inventory = discover_project_ready_assets(args.project)
    if not inventory:
        print("[WARN] No publish-ready projects found matching criteria.", flush=True)
        return

    total_projects = len(inventory)
    total_files = sum(sum(len(items) for items in cat.values()) for cat in inventory.values())
    total_bytes = sum(
        sum(sum(os.path.getsize(f) for f in items if os.path.exists(f)) for items in cat.values())
        for cat in inventory.values()
    )

    print(f"Found {total_projects} projects with {total_files} publish-ready files ({total_bytes / (1024**3):.2f} GB total):\n")
    for proj_title, cats in inventory.items():
        proj_bytes = sum(sum(os.path.getsize(f) for f in items if os.path.exists(f)) for items in cats.values())
        print(f"[PROJ] {proj_title} ({proj_bytes / (1024*1024):.1f} MB)")
        for cat_name, file_list in cats.items():
            if file_list:
                print(f"   [CAT] {cat_name}/ ({len(file_list)} files)")
                for fl in file_list:
                    sz_mb = os.path.getsize(fl) / (1024*1024)
                    print(f"      - {os.path.basename(fl)} ({sz_mb:.1f} MB)")
        print()

    if args.dry_run:
        print("[DRY-RUN] Completed scan. Run without --dry-run to start upload.", flush=True)
        return

    # 2. Authenticate
    service = authenticate()

    # 3. Locate or create root parent folder "YTF - AG-Stick" if desired, or place directly
    root_folder_id = None
    if args.parent_folder:
        print(f"[GDRIVE] Locating root parent folder: '{args.parent_folder}'...", flush=True)
        root_folder_id = get_or_create_folder(service, args.parent_folder)
        print(f"[GDRIVE] Root folder ID: {root_folder_id}\n", flush=True)

    # 4. Upload each project
    for proj_title, cats in inventory.items():
        print("-----------------------------------------------------------------------", flush=True)
        print(f"[PROCESS] Processing Project: {proj_title}", flush=True)
        print("-----------------------------------------------------------------------", flush=True)

        proj_folder_id = get_or_create_folder(service, proj_title, parent_id=root_folder_id)

        for cat_name, file_list in cats.items():
            if not file_list:
                continue

            cat_folder_id = get_or_create_folder(service, cat_name, parent_id=proj_folder_id)

            for fl in file_list:
                upload_file_resumable(service, fl, cat_folder_id)

    print("\n=======================================================================", flush=True)
    print("[SUCCESS] All publish-ready assets successfully synced to Google Drive!", flush=True)
    print("=======================================================================", flush=True)

if __name__ == '__main__':
    main()
