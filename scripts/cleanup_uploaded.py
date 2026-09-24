import os
import sys
import shutil

REPO_ROOT = r"c:\Users\bati-\Documents\AG-Stick"
PROJECTS_DIR = os.path.join(REPO_ROOT, "projects")

def get_drive_c_free():
    total, used, free = shutil.disk_usage("C:\\")
    return free / (1024**3)

def scan_cleanable_files():
    targets = []
    
    for root, dirs, files in os.walk(PROJECTS_DIR):
        parts = root.split(os.sep)
        # Skip git and node_modules
        if any(x in parts for x in ['.git', 'node_modules']):
            continue
        
        is_export = 'export' in parts
        
        for f in files:
            fp = os.path.join(root, f)
            f_lower = f.lower()
            
            # 1. All MP4 video files in projects (master, raw, review, shorts)
            if f_lower.endswith('.mp4'):
                try:
                    sz = os.path.getsize(fp)
                    targets.append((fp, sz))
                except Exception:
                    pass

            # 2. Heavy combined WAV audio files (>20 MB)
            elif f_lower.endswith('.wav'):
                try:
                    sz = os.path.getsize(fp)
                    if sz > 20 * 1024 * 1024:
                        targets.append((fp, sz))
                except Exception:
                    pass

    return targets

def main(dry_run=True):
    free_before = get_drive_c_free()
    targets = scan_cleanable_files()
    total_bytes = sum(sz for _, sz in targets)
    total_gb = total_bytes / (1024**3)

    print("===================================================================", flush=True)
    print(f"=== AG-Stick Clean Uploaded Exports ({'DRY-RUN' if dry_run else 'EXECUTION'}) ===", flush=True)
    print(f"=== Drive C Free: {free_before:.2f} GB | Targets: {len(targets)} files ({total_gb:.2f} GB) ===", flush=True)
    print("===================================================================\n", flush=True)

    deleted_count = 0
    deleted_bytes = 0

    for fp, sz in sorted(targets, key=lambda x: x[1], reverse=True):
        rel = os.path.relpath(fp, REPO_ROOT)
        sz_mb = sz / (1024*1024)
        if dry_run:
            print(f"  [WILL DELETE] {sz_mb:7.1f} MB | {rel}")
        else:
            try:
                os.remove(fp)
                deleted_count += 1
                deleted_bytes += sz
                print(f"  [DELETED] {sz_mb:7.1f} MB | {rel}", flush=True)
            except Exception as e:
                print(f"  [ERROR] Could not delete {rel}: {e}", flush=True)

    if not dry_run:
        free_after = get_drive_c_free()
        freed_gb = deleted_bytes / (1024**3)
        print("\n===================================================================", flush=True)
        print(f"[SUCCESS] Freed {freed_gb:.2f} GB across {deleted_count} files!", flush=True)
        print(f"Drive C Free Space: {free_before:.2f} GB -> {free_after:.2f} GB", flush=True)
        print("===================================================================", flush=True)

if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    main(dry_run=dry)
