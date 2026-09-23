import urllib.request
import json
import base64
import os
import shutil

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

PROJECT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero\case-05-goiania-caesium'
THUMBS_DIR = os.path.join(PROJECT_DIR, 'thumbnails')
REMOTION_THUMBS_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\goiania_caesium_137\thumbnails'

os.makedirs(THUMBS_DIR, exist_ok=True)
os.makedirs(REMOTION_THUMBS_DIR, exist_ok=True)

THUMBNAIL_PROMPTS = {
    "thumb_01_glowing_hand": (
        "High CTR viral YouTube documentary thumbnail in the signature 2D stickman noir style of The Dossier Zero, "
        "minimalist stickman investigator in dark charcoal trenchcoat and fedora leaning over an iron table in shock, "
        "staring at an open cracked lead cylinder leaking intensely radiant Cherenkov cyan-blue luminescent powder, "
        "beside a stickman hand glowing brightly with blue radioactive dust, dark obsidian void background, "
        "dramatic cinematic chiaroscuro, hazard yellow caution accents, high contrast, 16:9 widescreen, "
        "strictly no text, no letters, no words, no numbers, no speech bubbles"
    ),
    "thumb_02_lead_coffin_riot": (
        "High CTR viral YouTube documentary thumbnail in the signature 2D stickman noir style of The Dossier Zero, "
        "an enormous monolithic 700kg concrete-encased lead coffin being hoisted into the air by a massive yellow construction crane, "
        "while below an angry mob of 2,000 stickman rioters throw cobblestones and bricks, tear gas smoke rising, "
        "military police in riot gear with shields forming a line, dramatic high dynamic contrast, 16:9 widescreen, "
        "strictly no text, no letters, no words, no numbers, no speech bubbles"
    ),
    "thumb_03_the_blue_powder": (
        "High CTR viral YouTube documentary thumbnail in the signature 2D stickman noir style of The Dossier Zero, "
        "close-up shot of a small minimalist stickman child sitting on a dark floor innocently holding food with fingers "
        "intensely coated in glowing bright electric blue dust, while in the shadowy background a yellow vintage radiation meter "
        "has its black needle violently pegged past the red maximum danger zone with flashing red alarm light, "
        "high contrast noir shadows, 16:9 widescreen, strictly no text, no letters, no words, no numbers"
    )
}

def generate_thumb(name: str, prompt: str):
    target_local = os.path.join(THUMBS_DIR, f"{name}.png")
    target_remotion = os.path.join(REMOTION_THUMBS_DIR, f"{name}.png")

    if os.path.exists(target_local) and os.path.getsize(target_local) > 20000:
        print(f"[SKIP] Thumbnail {name} already exists.")
        if not os.path.exists(target_remotion):
            shutil.copyfile(target_local, target_remotion)
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

    print(f"[GEN] Generating thumbnail: {name}...", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'data' in data and len(data['data']) > 0:
                item = data['data'][0]
                if 'b64_json' in item and item['b64_json']:
                    raw_bytes = base64.b64decode(item['b64_json'])
                    with open(target_local, 'wb') as f:
                        f.write(raw_bytes)
                    shutil.copyfile(target_local, target_remotion)
                    print(f"[OK] Saved thumbnail: {target_local} ({len(raw_bytes):,} bytes)", flush=True)
                elif 'url' in item and item['url']:
                    urllib.request.urlretrieve(item['url'], target_local)
                    shutil.copyfile(target_local, target_remotion)
                    print(f"[OK] Downloaded thumbnail from URL: {target_local}", flush=True)
    except Exception as e:
        print(f"[ERROR] Thumbnail generation failed: {e}", flush=True)

def main():
    print("=== GENERATING HIGH-CTR YOUTUBE THUMBNAILS (THE DOSSIER ZERO) ===", flush=True)
    for name, prompt in THUMBNAIL_PROMPTS.items():
        generate_thumb(name, prompt)

if __name__ == '__main__':
    main()
