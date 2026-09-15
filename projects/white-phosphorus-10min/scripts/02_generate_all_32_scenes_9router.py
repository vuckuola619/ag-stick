import urllib.request
import json
import base64
import os
import time
import shutil

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'
FALLBACK_MODEL = 'cx/gpt-5.6-luna-image'

LOCAL_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\white-phosphorus-10min\assets\scenes'
REMOTION_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\white_phosphorus\scenes'

os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs(REMOTION_DIR, exist_ok=True)

MANIFEST_FILE = r'c:\Users\bati-\Documents\AG-Stick\projects\white-phosphorus-10min\script\storyboard_32_scenes.json'

def generate_scene_image(scene_id: str, prompt: str, max_retries: int = 3) -> bool:
    out_file = os.path.join(LOCAL_DIR, f"scene_{scene_id}.png")
    remotion_file = os.path.join(REMOTION_DIR, f"scene_{scene_id}.png")
    
    if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
        print(f"[SKIP] Scene {scene_id} already exists ({os.path.getsize(out_file)} bytes).")
        if not os.path.exists(remotion_file):
            shutil.copyfile(out_file, remotion_file)
        return True

    payload = {
        'model': MODEL,
        'prompt': prompt,
        'size': '1024x1024'
    }

    for attempt in range(1, max_retries + 1):
        try:
            print(f"[GEN] Scene {scene_id} | Attempt {attempt}/{max_retries} with {payload['model']}...")
            t0 = time.time()
            req = urllib.request.Request(
                URL,
                data=json.dumps(payload).encode('utf-8'),
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {API_KEY}'
                }
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if 'data' in res and len(res['data']) > 0:
                    item = res['data'][0]
                    img_bytes = None
                    if 'b64_json' in item and item['b64_json']:
                        img_bytes = base64.b64decode(item['b64_json'])
                    elif 'url' in item and item['url']:
                        with urllib.request.urlopen(item['url'], timeout=60) as uresp:
                            img_bytes = uresp.read()
                    
                    if img_bytes:
                        with open(out_file, 'wb') as f:
                            f.write(img_bytes)
                        shutil.copyfile(out_file, remotion_file)
                        dt = time.time() - t0
                        print(f"[SUCCESS] Scene {scene_id} saved in {dt:.1f}s ({len(img_bytes)} bytes)")
                        return True
                    else:
                        print(f"[WARN] Scene {scene_id} returned empty image data.")
        except Exception as e:
            print(f"[ERROR] Scene {scene_id} attempt {attempt} failed: {e}")
            if attempt == 2:
                payload['model'] = FALLBACK_MODEL
                print(f"[INFO] Switching to fallback model {FALLBACK_MODEL}")
            time.sleep(3 * attempt)
            
    return False

def main():
    print("=== BATCH GENERATING 32 SCENE IMAGES VIA 9ROUTER CODEX ===")
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    scenes = manifest['scenes']
    total = len(scenes)
    success_count = 0

    for idx, sc in enumerate(scenes):
        s_id = sc['scene_id']
        prompt = sc['codex_image_prompt']
        print(f"\n--- Progress: {idx+1}/{total} ({(idx+1)/total*100:.1f}%) ---")
        ok = generate_scene_image(s_id, prompt)
        if ok:
            success_count += 1
        time.sleep(1.0)

    print(f"\n[FINISHED] Batch Generation Complete: {success_count}/{total} images ready.")

if __name__ == '__main__':
    main()
