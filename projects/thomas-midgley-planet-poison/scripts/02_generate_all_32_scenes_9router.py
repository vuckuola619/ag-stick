import urllib.request
import json
import base64
import time
import os
import shutil
from PIL import Image

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

PROJECT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\thomas-midgley-planet-poison'
LOCAL_DIR = os.path.join(PROJECT_DIR, 'assets', 'scenes')
REMOTION_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\thomas_midgley\scenes'
STORYBOARD_FILE = os.path.join(PROJECT_DIR, 'script', 'storyboard_32_scenes.json')

os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs(REMOTION_DIR, exist_ok=True)

def generate_scene_image(scene_id: str, prompt: str, retry_limit: int = 3):
    target_local = os.path.join(LOCAL_DIR, f"scene_{scene_id}.png")
    target_remotion = os.path.join(REMOTION_DIR, f"scene_{scene_id}.png")

    if os.path.exists(target_local) and os.path.getsize(target_local) > 10000:
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
                        print(f"[OK] Scene {scene_id} generated & saved ({len(raw_bytes):,} bytes).", flush=True)
                        return True
                    elif 'url' in item:
                        # Download URL
                        urllib.request.urlretrieve(item['url'], target_local)
                        shutil.copyfile(target_local, target_remotion)
                        print(f"[OK] Scene {scene_id} downloaded from URL.", flush=True)
                        return True
            print(f"[WARN] No valid image in response for scene {scene_id}", flush=True)
        except Exception as e:
            print(f"[ERROR] Scene {scene_id} generation failed: {e}", flush=True)
            time.sleep(3)

    return False

def main():
    print("=== BATCH GENERATING 32 2D STICKMAN SCENES (9ROUTER CODEX) ===", flush=True)
    with open(STORYBOARD_FILE, 'r', encoding='utf-8') as f:
        storyboard = json.load(f)

    scenes = storyboard['scenes']
    success_count = 0

    for sc in scenes:
        s_id = sc['scene_id']
        prompt = sc['codex_image_prompt']
        success = generate_scene_image(s_id, prompt)
        if success:
            success_count += 1

    print(f"\n[SUMMARY] Successfully processed {success_count}/{len(scenes)} scenes.", flush=True)

if __name__ == '__main__':
    main()
