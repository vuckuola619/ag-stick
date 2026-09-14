import urllib.request
import json
import base64
import os
import shutil
from PIL import Image, ImageOps

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'
FALLBACK_MODEL = 'cx/gpt-5.6-luna-image'

ASSETS_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\assets'
REMOTION_STICKERS_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\stickers'
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(REMOTION_STICKERS_DIR, exist_ok=True)

PROMPTS = {
    'caveman_curious': (
        'A funny caveman stickman with messy wild hair, big cartoon expressive eyes, cheetah fur tunic, '
        'holding a flaming wooden torch, minimalist clean flat vector sticker, thick crisp outlines, '
        'pure white background, isolated icon, no background shadows, high contrast'
    ),
    'caveman_shocked': (
        'A funny caveman stickman with wild hair, jaw dropped wide open in extreme shock and disbelief, '
        'hands clutching cheeks, eyes popping out, cheetah fur tunic, minimalist clean flat vector sticker, '
        'thick crisp outlines, pure white background, isolated icon, no background shadows, high contrast'
    ),
    'cinnabar_crystal': (
        'A glowing intense ruby-red cinnabar mineral crystal rock, raw red vermilion gemstone with bright sparkles, '
        'minimalist clean flat vector sticker, thick crisp outlines, pure white background, isolated icon, no background shadows, high contrast'
    ),
    'prehistoric_campfire': (
        'A prehistoric campfire with rough stone circle base and bright dancing orange-yellow flames and glowing red logs, '
        'minimalist clean flat vector sticker, thick crisp outlines, pure white background, isolated icon, no background shadows, high contrast'
    ),
    'alchemist_flask': (
        'An ancient antique alchemist glass distillation flask containing shiny liquid mercury metal and glowing condensation drops, '
        'minimalist clean flat vector sticker, thick crisp outlines, pure white background, isolated icon, no background shadows, high contrast'
    ),
    'mercury_puddle': (
        'A pool of liquid metallic silver chrome quicksilver with shiny spherical droplets and mirror reflections, '
        'minimalist clean flat vector sticker, thick crisp outlines, pure white background, isolated icon, no background shadows, high contrast'
    )
}

def make_transparent(input_path, output_path):
    img = Image.open(input_path).convert('RGBA')
    datas = img.getdata()
    
    # We detect the background color from top-left corner
    corner_color = img.getpixel((5, 5))[:3]
    
    new_data = []
    for item in datas:
        # Distance to white / corner
        r, g, b, a = item
        # If very close to corner or bright white (> 240 in all channels)
        dist_corner = ((r - corner_color[0])**2 + (g - corner_color[1])**2 + (b - corner_color[2])**2) ** 0.5
        if (r > 242 and g > 242 and b > 242) or dist_corner < 22:
            new_data.append((255, 255, 255, 0))
        elif (r > 225 and g > 225 and b > 225) or dist_corner < 45:
            # Feather edge
            alpha = int(255 * (dist_corner / 45))
            new_data.append((r, g, b, min(255, max(0, alpha))))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, 'PNG')
    print(f"  [OK] Converted to transparent PNG: {output_path}")

def generate_asset(name, prompt, model=MODEL):
    raw_path = os.path.join(ASSETS_DIR, f"raw_{name}.png")
    final_path = os.path.join(ASSETS_DIR, f"{name}.png")
    remotion_path = os.path.join(REMOTION_STICKERS_DIR, f"{name}.png")

    if os.path.exists(final_path) and os.path.getsize(final_path) > 10000:
        print(f"Asset '{name}' already exists, skipping generation.")
        if not os.path.exists(remotion_path):
            shutil.copy2(final_path, remotion_path)
        return

    print(f"\n[+] Requesting 9router for '{name}' using model '{model}'...")
    payload = {
        'model': model,
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

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            b64 = data['data'][0]['b64_json']
            img_bytes = base64.b64decode(b64)
            with open(raw_path, 'wb') as f:
                f.write(img_bytes)
            print(f"  [OK] Saved raw image: {raw_path} ({len(img_bytes)} bytes)")
            
            # Post-process transparency
            make_transparent(raw_path, final_path)
            shutil.copy2(final_path, remotion_path)
            print(f"  [OK] Deployed to Remotion stickers: {remotion_path}")
    except Exception as e:
        print(f"  [ERROR] Failed to generate '{name}' with {model}: {e}")
        if model != MODEL:
            print(f"  [RETRY] Retrying with primary verified model '{MODEL}'...")
            generate_asset(name, prompt, model=MODEL)
        if hasattr(e, 'read'):
            print("  Response body:", e.read().decode('utf-8', errors='ignore'))

def main():
    print("=== 9ROUTER ASSET GENERATION PIPELINE (ANTI-SLOP) ===")
    for name, prompt in PROMPTS.items():
        generate_asset(name, prompt)
    print("\nAll visual sticker assets processed successfully!")

if __name__ == '__main__':
    main()
