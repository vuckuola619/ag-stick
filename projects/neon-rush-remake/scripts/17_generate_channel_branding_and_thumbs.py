import urllib.request
import json
import base64
import os
import time
import shutil

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

OUT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\branding'
ARTIFACT_DIR = r'C:\Users\bati-\.gemini\antigravity\brain\f39d64bf-6e51-40b4-92eb-7bf63798ce0e'

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

NEON_RUSH_SUFFIX = (
    ', in the signature 2D cartoon illustration style of YouTube channel Neon Rush, '
    'featuring the iconic minimalist stickman character with a blank white circular head (#ffffff), '
    'simple expressive round cartoon eyes, thin black stick limbs, '
    'bold crisp black ink outlines, clean cel-shading, vibrant high-contrast saturated colors, '
    'punchy high CTR YouTube thumbnail framing, no 3D CGI, no photorealism, no realistic human faces'
)

ASSETS_TO_GENERATE = {
    # 1. Profile Picture / Avatar (1:1, 1024x1024)
    'channel_pfp_avatar': (
        "Iconic YouTube profile picture avatar: a friendly energetic stickman with a blank white circular head (#ffffff), "
        "big expressive round cartoon eyes, happy smile, thin black stick arms, wearing a cool dark-grey tee, "
        "holding a glass laboratory conical flask filled with bubbling gleaming liquid silver chrome quicksilver with electric cyan glow sparks, "
        "bold circular dark navy backdrop (#0b132b) with glowing atomic orbital rings, thick crisp black ink outlines, "
        "clean cel-shading, ultra-high contrast, designed to be instantly recognizable at 32x32 pixel circle on mobile screens"
        + NEON_RUSH_SUFFIX
    ),

    # 2. Channel Banner (16:9, 1024x1024 widescreen composition)
    'channel_banner_youtube': (
        "Epic YouTube channel banner illustration: a panoramic timeline progression of science and history across human ages. "
        "On the far left: prehistoric caveman stickman discovering fire with red cinnabar rock. "
        "In the middle: Renaissance alchemist stickman with glass distillation retorts and modern scientist stickman in white lab coat with atom model. "
        "On the far right: futuristic stickman astronaut floating in starry deep space next to a high-tech ion engine spaceship. "
        "Center has an open clean area with glowing cyan and neon yellow grid lines for channel text, vibrant saturated colors, "
        "16:9 widescreen composition, bold comic ink outlines"
        + NEON_RUSH_SUFFIX
    ),

    # 3. High-CTR Thumbnail Variant A: "CAN YOU TOUCH IT?"
    'thumbnail_v1_forbidden_quicksilver': (
        "Ultra high CTR YouTube thumbnail: A curious caveman stickman with a blank white circular head (#ffffff), "
        "wide astonished round cartoon eyes, leaning forward with his finger inches away from touching a floating glistening droplet "
        "of pure liquid silver mercury dripping from a giant cracked blood-red crystalline cinnabar rock, "
        "large bold comic text 'CAN YOU TOUCH IT?' in vibrant yellow (#FFE600) with thick black stroke and red question mark, "
        "roaring stone campfire with glowing sparks, high contrast, mobile optimized, 16:9 widescreen composition"
        + NEON_RUSH_SUFFIX
    ),

    # 4. High-CTR Thumbnail Variant B: "IRON FLOATS ON THIS?!"
    'thumbnail_v2_iron_floats': (
        "Ultra high CTR YouTube thumbnail: A stickman scientist in white lab coat with jaw dropped wide open in extreme shock, "
        "hands clutching cheeks, looking at a huge solid black cast-iron cannonball floating effortlessly on top of a clear glass tank "
        "filled with shiny liquid metallic mercury, large yellow comic starburst text 'IRON FLOATS?!' and '13.5x HEAVIER!', "
        "red exclamation marks, high contrast laboratory background, mobile optimized, 16:9 widescreen composition"
        + NEON_RUSH_SUFFIX
    ),

    # 5. High-CTR Thumbnail Variant C: "100 MERCURY RIVERS"
    'thumbnail_v3_100_mercury_rivers': (
        "Ultra high CTR YouTube thumbnail: Emperor Qin Shi Huang stickman in ornate black and gold dragon robes with beaded crown, "
        "standing on an imperial terrace gazing into a vast dark subterranean pyramid chamber containing 100 glowing mechanical rivers "
        "of flowing shining liquid mercury, under a starry bronze cosmic ceiling, large bold yellow text '100 MERCURY RIVERS' "
        "with red glowing subtitle 'TOMB OF SECRETS', high contrast, mobile optimized, 16:9 widescreen composition"
        + NEON_RUSH_SUFFIX
    ),
}

def generate_asset(name, prompt):
    filename = f"{name}.png"
    out_file = os.path.join(OUT_DIR, filename)
    artifact_file = os.path.join(ARTIFACT_DIR, filename)

    if os.path.exists(out_file) and os.path.getsize(out_file) > 100000:
        print(f"[EXISTS] {filename} ({os.path.getsize(out_file)} bytes), copying to artifact...")
        shutil.copy2(out_file, artifact_file)
        return

    print(f"\nGenerating {filename} via 9Router ({MODEL})...", flush=True)
    payload = {
        'model': MODEL,
        'prompt': prompt,
        'n': 1,
        'size': '1024x1024'
    }

    req = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }
    )

    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            b64 = data['data'][0]['b64_json']
            img_bytes = base64.b64decode(b64)
            with open(out_file, 'wb') as f:
                f.write(img_bytes)
            shutil.copy2(out_file, artifact_file)
            dur = time.time() - t0
            print(f"  [OK] Saved {filename} ({len(img_bytes)} bytes) in {dur:.1f}s", flush=True)
    except Exception as e:
        print(f"  [ERROR] {name} failed: {e}", flush=True)
        if hasattr(e, 'read'):
            print("  Body:", e.read().decode('utf-8', errors='ignore'), flush=True)
        time.sleep(4)

def main():
    print("=== GENERATING CHANNEL BRANDING & HIGH-CTR THUMBNAILS ===", flush=True)
    for name, prompt in ASSETS_TO_GENERATE.items():
        generate_asset(name, prompt)
        time.sleep(2)  # Courteous pause between requests
    print("\n[COMPLETE] All channel branding & thumbnail assets generated!", flush=True)

if __name__ == '__main__':
    main()
