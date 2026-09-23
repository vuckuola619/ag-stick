import urllib.request
import json
import base64
import time
import os
import shutil
import sys
import re

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.6-luna-image'
FALLBACK_MODEL = 'cx/gpt-5.5-image'

PROJECT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero\case-05-goiania-caesium'
LOCAL_DIR = os.path.join(PROJECT_DIR, 'assets', 'scenes')
REMOTION_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\goiania_caesium_137\scenes'
STORYBOARD_FILE = os.path.join(PROJECT_DIR, 'script', 'storyboard_48_scenes.json')

os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs(REMOTION_DIR, exist_ok=True)

def generate_scene_image(scene_id: str, prompt: str, retry_limit: int = 5):
    target_local = os.path.join(LOCAL_DIR, f"scene_{scene_id}.png")
    target_remotion = os.path.join(REMOTION_DIR, f"scene_{scene_id}.png")

    if os.path.exists(target_local) and os.path.getsize(target_local) > 20000:
        print(f"[SKIP] Scene {scene_id} already exists ({os.path.getsize(target_local):,} bytes).", flush=True)
        if not os.path.exists(target_remotion) or os.path.getsize(target_remotion) != os.path.getsize(target_local):
            shutil.copyfile(target_local, target_remotion)
        return True

    payload = {
        'model': MODEL,
        'prompt': prompt,
        'size': '1672x941',
        'n': 1
    }

    for attempt in range(1, retry_limit + 1):
        try:
            print(f"[GEN] Scene {scene_id} (Attempt {attempt}/{retry_limit}) via {payload['model']}...", flush=True)
            req = urllib.request.Request(
                URL,
                data=json.dumps(payload).encode('utf-8'),
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {API_KEY}'
                }
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if 'data' in data and len(data['data']) > 0:
                    item = data['data'][0]
                    if 'b64_json' in item and item['b64_json']:
                        raw_bytes = base64.b64decode(item['b64_json'])
                        with open(target_local, 'wb') as f:
                            f.write(raw_bytes)
                        shutil.copyfile(target_local, target_remotion)
                        print(f"[OK] Scene {scene_id} generated & saved ({len(raw_bytes):,} bytes).", flush=True)
                        return True
                    elif 'url' in item and item['url']:
                        urllib.request.urlretrieve(item['url'], target_local)
                        shutil.copyfile(target_local, target_remotion)
                        print(f"[OK] Scene {scene_id} downloaded from URL.", flush=True)
                        return True
            print(f"[WARN] No valid image in response for scene {scene_id}", flush=True)
        except Exception as e:
            err_msg = str(e)
            sleep_time = 5
            if hasattr(e, 'read'):
                try:
                    body = e.read().decode('utf-8', errors='ignore')
                    err_msg += f" - {body}"
                    m = re.search(r'reset after (\d+)s', body)
                    if m:
                        sleep_time = int(m.group(1)) + 2
                except Exception:
                    pass
            print(f"[ERROR] Scene {scene_id} attempt {attempt} failed: {err_msg}", flush=True)
            print(f"[RETRY] Backing off for {sleep_time}s before attempt {attempt + 1}...", flush=True)
            time.sleep(sleep_time)

    return False

def main():
    print("=======================================================================", flush=True)
    print("=== BATCH GENERATING 48 SCENE ARTWORKS (THE DOSSIER ZERO #05)        ===", flush=True)
    print("=== Format: 1672x941 (16:9) | Style: 2D Stickman Noir (IAEA Compliant)===", flush=True)
    print("=== Engine: cx/gpt-5.6-luna-image | Robust Sequential Processing      ===", flush=True)
    print("=======================================================================\n", flush=True)

    with open(STORYBOARD_FILE, 'r', encoding='utf-8') as f:
        storyboard = json.load(f)

    scenes = storyboard['scenes']
    success_count = 0
    total = len(scenes)

    for idx, sc in enumerate(scenes, start=1):
        s_id = sc['scene_id']
        print(f"\n--- [{idx:02d}/{total:02d}] Scene {s_id}: {sc.get('headline', '')} ---", flush=True)
        ok = generate_scene_image(s_id, sc['codex_image_prompt'])
        if ok:
            success_count += 1
            # Brief pause between generations to avoid burst pressure
            time.sleep(1)

    print(f"\n[SUMMARY] Successfully processed {success_count}/{total} scenes.", flush=True)

if __name__ == '__main__':
    main()
