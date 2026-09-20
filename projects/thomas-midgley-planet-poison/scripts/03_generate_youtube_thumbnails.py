import urllib.request
import json
import base64
import os
import shutil

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

PROJECT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\thomas-midgley-planet-poison'
THUMBS_DIR = os.path.join(PROJECT_DIR, 'thumbnails')
os.makedirs(THUMBS_DIR, exist_ok=True)

THUMBNAIL_PROMPTS = {
    "thumb_01_poisoned_planet": (
        "High CTR viral YouTube thumbnail in the signature 2D cartoon style of Neon Rush, "
        "minimalist stickman scientist with a blank white circular head (#ffffff), round black spectacles, "
        "wearing a white lab coat, standing center-stage looking with shocked wide cartoon eyes, "
        "holding up a glowing neon toxic-green glass beaker in one stick hand, while behind him a giant cartoon Earth "
        "has a massive glowing violet ultraviolet hole ripped through the clouds with toxic smog rising, "
        "bold black outlines, rich saturated colors, high contrast, centered composition, 16:9 widescreen, "
        "no text, no letters, no numbers, no words, no speech bubbles"
    ),
    "thumb_02_deadliest_invention": (
        "High CTR viral YouTube thumbnail in the signature 2D cartoon style of Neon Rush, "
        "minimalist stickman chemist with a blank white circular head (#ffffff), round black spectacles and bowtie, "
        "smiling proudly while holding an antique gasoline nozzle spewing a glowing amber fluid with toxic skull vapors, "
        "beside a split view of an old 1920s automobile engine exploding in flames and an icy aerosol can spraying frost, "
        "bold clean outlines, vibrant saturated colors, high contrast, centered composition, 16:9 widescreen, "
        "no text, no letters, no numbers, no words, no speech bubbles"
    ),
    "thumb_03_the_man_who_broke_earth": (
        "High CTR viral YouTube thumbnail in the signature 2D cartoon style of Neon Rush, "
        "minimalist stickman inventor sitting in an antique wooden wheelchair with tangled overhead pulley ropes, "
        "holding a small glowing green atom model that casts an enormous shadowy monster silhouette across a cracked planet Earth, "
        "dramatic rim lighting, deep space starlight background, bold black outlines, high contrast, centered composition, 16:9 widescreen, "
        "no text, no letters, no numbers, no words, no speech bubbles"
    )
}

def generate_thumb(name: str, prompt: str):
    target = os.path.join(THUMBS_DIR, f"{name}.png")
    if os.path.exists(target) and os.path.getsize(target) > 10000:
        print(f"[SKIP] Thumbnail {name} already exists.")
        return

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

    print(f"[GEN] Generating thumbnail: {name}...")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'data' in data and len(data['data']) > 0:
                item = data['data'][0]
                if 'b64_json' in item:
                    raw_bytes = base64.b64decode(item['b64_json'])
                    with open(target, 'wb') as f:
                        f.write(raw_bytes)
                    print(f"[OK] Saved thumbnail: {target} ({len(raw_bytes):,} bytes)")
                elif 'url' in item:
                    urllib.request.urlretrieve(item['url'], target)
                    print(f"[OK] Downloaded thumbnail from URL: {target}")
    except Exception as e:
        print(f"[ERROR] Thumbnail generation failed: {e}")

def main():
    print("=== GENERATING HIGH-CTR YOUTUBE THUMBNAILS ===")
    for name, prompt in THUMBNAIL_PROMPTS.items():
        generate_thumb(name, prompt)

if __name__ == '__main__':
    main()
