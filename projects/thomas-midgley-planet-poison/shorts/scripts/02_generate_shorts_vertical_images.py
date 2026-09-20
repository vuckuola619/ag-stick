import urllib.request
import json
import base64
import time
import os
import shutil

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'
SIZE = '1024x1792'

BASE_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\thomas-midgley-planet-poison\shorts"
MANIFEST_FILE = os.path.join(BASE_DIR, "manifest_shorts.json")
LOCAL_DIR = os.path.join(BASE_DIR, "assets", "scenes")
REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\dossier_shorts\scenes"

os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs(REMOTION_DIR, exist_ok=True)

def generate_scene_image(scene_id: str, prompt: str, retry_limit: int = 5):
    target_local = os.path.join(LOCAL_DIR, f"{scene_id}.png")
    target_remotion = os.path.join(REMOTION_DIR, f"{scene_id}.png")

    if os.path.exists(target_local) and os.path.getsize(target_local) > 10000:
        print(f"[SKIP] Scene {scene_id} exists ({os.path.getsize(target_local):,} bytes).", flush=True)
        if not os.path.exists(target_remotion) or os.path.getsize(target_remotion) != os.path.getsize(target_local):
            shutil.copyfile(target_local, target_remotion)
        return True

    payload = {
        'model': MODEL,
        'prompt': prompt,
        'size': SIZE,
        'n': 1
    }

    req = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }
    )

    for attempt in range(1, retry_limit + 1):
        try:
            print(f"[GEN] Scene {scene_id} (Attempt {attempt}/{retry_limit})...", flush=True)
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if 'data' in data and len(data['data']) > 0:
                    item = data['data'][0]
                    if 'b64_json' in item:
                        raw_bytes = base64.b64decode(item['b64_json'])
                        with open(target_local, 'wb') as f:
                            f.write(raw_bytes)
                        shutil.copyfile(target_local, target_remotion)
                        print(f"[OK] Scene {scene_id} saved ({len(raw_bytes):,} bytes).", flush=True)
                        time.sleep(2)
                        return True
                    elif 'url' in item:
                        urllib.request.urlretrieve(item['url'], target_local)
                        shutil.copyfile(target_local, target_remotion)
                        print(f"[OK] Scene {scene_id} downloaded from URL.", flush=True)
                        time.sleep(2)
                        return True
            print(f"[WARN] No image data for {scene_id}", flush=True)
        except Exception as e:
            wait_sec = attempt * 5
            print(f"[ERROR] Scene {scene_id} failed: {e}. Waiting {wait_sec}s...", flush=True)
            time.sleep(wait_sec)

    return False

def main():
    print("=== BATCH GENERATING 15 VERTICAL 9:16 SCENES (1024x1792) ===", flush=True)
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        shorts_list = json.load(f)

    all_scenes = []
    for sh in shorts_list:
        for sc in sh['scenes']:
            all_scenes.append((sc['scene_id'], sc['image_prompt']))

    print(f"Total scenes to generate: {len(all_scenes)}", flush=True)
    success = 0
    for idx, (s_id, prompt) in enumerate(all_scenes):
        print(f"[{idx+1}/{len(all_scenes)}] Generating {s_id}...", flush=True)
        if generate_scene_image(s_id, prompt):
            success += 1

    print(f"\n[SUMMARY] Successfully processed {success}/{len(all_scenes)} vertical scenes.", flush=True)

if __name__ == '__main__':
    main()
