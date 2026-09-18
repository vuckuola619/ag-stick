import urllib.request
import json
import base64
import os
import time
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'
FALLBACK_MODEL = 'cx/gpt-5.6-luna-image'

BASE_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
os.makedirs(ASSETS_DIR, exist_ok=True)

# Master "Stickman Realistic Cinematic" Prompt Formula (Anti-AI Slop)
CINEMATIC_STICKMAN_SUFFIX = (
    ', featuring a minimalist 2D/3D hybrid stickman investigator with a solid blank circular white head (#ffffff), '
    'simple expressive wide cartoon eyes, thin black stick limbs, wearing a 1940s noir detective trench coat and black fedora hat, '
    'set inside a gritty cinematic atmospheric environment with dramatic chiaroscuro lighting, rich volumetric fog, '
    'warm amber tungsten desk light and deep cyan rim lighting, subtle 35mm film grain, anamorphic cinematic depth of field, '
    'bold clean silhouette outlines, high-contrast professional production quality, perfectly centered composition, '
    'strictly no AI slop, no deformed hands, no messy clutter, strictly no text, no letters, no words, no watermark'
)

ASSETS_TO_GENERATE = {
    'avatar_profile_raw': {
        'prompt': (
            'Cinematic close-up portrait of a minimalist stickman investigator for a true mystery documentary YouTube profile picture. '
            'The stickman has a smooth solid white circular head (#ffffff) with focused wide cartoon eyes, wearing a textured dark charcoal trench coat and black fedora hat. '
            'He holds a vintage heavy brass magnifying glass up toward the camera with real optical glass distortion. '
            'Moody cinematic noir lighting: warm tungsten key light from one side and sharp electric cyan rim light highlighting the edge of the fedora and coat. '
            'The background is a dark moody detective corkboard with declassified documents and red pins softly blurred by shallow depth of field. '
            'Professional cinematic 8k, crisp silhouette, perfectly framed for a circular avatar icon'
            + CINEMATIC_STICKMAN_SUFFIX
        ),
        'size': '1024x1024',
    },
    'channel_banner_raw': {
        'prompt': (
            'Epic wide cinematic 16:9 YouTube channel header banner for a mysterious history and declassified secrets channel named DOSSIER ZERO. '
            'In a vast shadowy subterranean archive vault with soaring concrete pillars and rows of steel filing cabinets, '
            'atmospheric shafts of dusty light beam down through industrial ceiling grates. '
            'In the center-right foreground, the minimalist stickman investigator in dark trench coat and fedora leans over an illuminated oak table '
            'covered with realistic weathered declassified dossier folders, top-secret manila envelopes, an antique brass nautical compass, and a world map. '
            'Rich chiaroscuro noir atmosphere, glowing green banker lamp on the desk, dramatic atmospheric haze, cinematic 35mm widescreen cinematography, '
            'clean left side with dark open space for typography, high contrast, zero slop'
            + CINEMATIC_STICKMAN_SUFFIX
        ),
        'size': '1672x941',
    },
    'watermark_raw': {
        'prompt': (
            'Iconic minimalist YouTube video corner watermark badge on a clean solid pure dark obsidian background (#0a0d14). '
            'A bold circular tactical reticle emblem: at the center is the minimalist stickman head in a black fedora with sharp focused eyes, '
            'encircled by a glowing circular compass ring with cardinal crosshair notches and subtle glowing cyan (#00F0FF) and caution amber (#FFE600) edges. '
            'Thick bold 12px clean black ink border, ultra-high contrast graphic vector emblem, striking visual hierarchy, '
            'designed to remain razor-sharp and instantly recognizable at small 150x150 pixel size'
            + CINEMATIC_STICKMAN_SUFFIX
        ),
        'size': '1024x1024',
    },
}

def generate_image(name: str, config: dict, max_retries: int = 3) -> str:
    out_path = os.path.join(ASSETS_DIR, f"{name}.png")
    if os.path.exists(out_path) and os.path.getsize(out_path) > 50000:
        print(f"[SKIP] {name}.png already exists ({os.path.getsize(out_path)} bytes).", flush=True)
        return out_path

    payload = {
        'model': MODEL,
        'prompt': config['prompt'],
        'size': config['size'],
    }

    for attempt in range(1, max_retries + 1):
        try:
            print(f"[GEN] {name} | Attempt {attempt}/{max_retries} with {payload['model']}...", flush=True)
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
                        with open(out_path, 'wb') as f:
                            f.write(img_bytes)
                        dt = time.time() - t0
                        print(f"[SUCCESS] {name} saved in {dt:.1f}s ({len(img_bytes)} bytes)", flush=True)
                        return out_path
                    else:
                        print(f"[WARN] {name} returned empty image data.", flush=True)
        except Exception as e:
            print(f"[ERROR] {name} attempt {attempt} failed: {e}", flush=True)
            if attempt == 2:
                payload['model'] = FALLBACK_MODEL
                print(f"[INFO] Switching to fallback model {FALLBACK_MODEL}", flush=True)
            time.sleep(3 * attempt)

    raise RuntimeError(f"Failed to generate {name} after {max_retries} attempts.")

def postprocess_avatar(raw_path: str):
    print("\n--- Processing YouTube Profile Avatar (800x800) ---", flush=True)
    img = Image.open(raw_path).convert('RGBA')
    avatar = img.resize((800, 800), Image.Resampling.LANCZOS)
    
    out_square = os.path.join(ASSETS_DIR, 'dossier_zero_profile_800x800.png')
    avatar.save(out_square, 'PNG')
    print(f"[OK] Saved square profile: {out_square}", flush=True)

    # Circular cropped preview
    mask = Image.new('L', (800, 800), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, 800, 800), fill=255)
    
    avatar_circ = Image.new('RGBA', (800, 800), (0, 0, 0, 0))
    avatar_circ.paste(avatar, (0, 0), mask=mask)
    
    # Elegant cinematic rim stroke
    draw_circ = ImageDraw.Draw(avatar_circ)
    draw_circ.ellipse((3, 3, 797, 797), outline='#00F0FF', width=5)
    draw_circ.ellipse((7, 7, 793, 793), outline='#FFE600', width=2)
    
    out_circ = os.path.join(ASSETS_DIR, 'dossier_zero_profile_circular_preview.png')
    avatar_circ.save(out_circ, 'PNG')
    print(f"[OK] Saved circular preview: {out_circ}", flush=True)

def postprocess_watermark(raw_path: str):
    print("\n--- Processing YouTube Video Watermarks (512x512 & 150x150) ---", flush=True)
    img = Image.open(raw_path).convert('RGBA')
    
    # 512x512 Master
    wm_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    out_512 = os.path.join(ASSETS_DIR, 'dossier_zero_watermark_512x512.png')
    wm_512.save(out_512, 'PNG')
    print(f"[OK] Saved {out_512}", flush=True)

    # 150x150 Standard YouTube
    wm_150 = img.resize((150, 150), Image.Resampling.LANCZOS)
    out_150 = os.path.join(ASSETS_DIR, 'dossier_zero_watermark_150x150.png')
    wm_150.save(out_150, 'PNG')
    print(f"[OK] Saved {out_150}", flush=True)

    # Transparent Circular Badge
    mask = Image.new('L', (512, 512), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((8, 8, 504, 504), fill=255)
    
    wm_circ = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    wm_circ.paste(wm_512, (0, 0), mask=mask)
    draw_circ = ImageDraw.Draw(wm_circ)
    draw_circ.ellipse((8, 8, 504, 504), outline='#FFE600', width=7)
    draw_circ.ellipse((14, 14, 498, 498), outline='#00F0FF', width=3)
    
    out_circ_512 = os.path.join(ASSETS_DIR, 'dossier_zero_watermark_transparent_circle_512x512.png')
    wm_circ.save(out_circ_512, 'PNG')
    out_circ_150 = os.path.join(ASSETS_DIR, 'dossier_zero_watermark_transparent_circle_150x150.png')
    wm_circ.resize((150, 150), Image.Resampling.LANCZOS).save(out_circ_150, 'PNG')
    print(f"[OK] Saved transparent circle watermarks", flush=True)

def postprocess_banner(raw_path: str):
    print("\n--- Processing YouTube Channel Banner (2560x1440 Standard) ---", flush=True)
    # YouTube Official Banner Specs: 2560 x 1440 px
    # Safe Area (Visible on all devices): 1546 x 423 px in center (X: 507 to 2053, Y: 508 to 931)
    
    banner_canvas = Image.new('RGBA', (2560, 1440), '#0a0d14')
    raw_art = Image.open(raw_path).convert('RGBA')
    
    # Scale raw art to 2560 width
    raw_w, raw_h = raw_art.size
    aspect = raw_w / raw_h
    target_w = 2560
    target_h = int(target_w / aspect)
    art_scaled = raw_art.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Center vertically
    offset_y = (1440 - target_h) // 2
    banner_canvas.paste(art_scaled, (0, offset_y))
    
    # Save clean unbranded 2560x1440 art
    out_clean = os.path.join(ASSETS_DIR, 'dossier_zero_banner_clean_art_2560x1440.png')
    banner_canvas.save(out_clean, 'PNG')
    print(f"[OK] Saved clean banner art: {out_clean}", flush=True)

    # Branded Banner (No container field boxes, clean high-CTR outline typography)
    impact_path = r'C:\Windows\Fonts\impact.ttf'
    arialbd_path = r'C:\Windows\Fonts\arialbd.ttf'
    
    title_font = ImageFont.truetype(impact_path, 98) if os.path.exists(impact_path) else ImageFont.load_default()
    sub_font = ImageFont.truetype(arialbd_path, 25) if os.path.exists(arialbd_path) else ImageFont.load_default()
    sch_font = ImageFont.truetype(arialbd_path, 18) if os.path.exists(arialbd_path) else ImageFont.load_default()

    ch_name = "DOSSIER ZERO"
    ch_tag = "UNSOLVED WORLD EVENTS & DECLASSIFIED MYSTERIES"
    ch_sch = "NEW INVESTIGATION EVERY THURSDAY • @THEDOSSIERZERO"

    def draw_cinematic_text(d, pos, text, font, fill, stroke_fill='#000000', stroke_w=5, shadow_dist=5):
        x, y = pos
        # Deep cinematic drop shadow
        d.text((x + shadow_dist, y + shadow_dist), text, font=font, fill='#000000')
        # Crisp black stroke
        for dx in range(-stroke_w, stroke_w + 1):
            for dy in range(-stroke_w, stroke_w + 1):
                if dx != 0 or dy != 0:
                    d.text((x + dx, y + dy), text, font=font, fill=stroke_fill)
        # Main fill
        d.text((x, y), text, font=font, fill=fill)

    branded = banner_canvas.copy()
    draw = ImageDraw.Draw(branded)

    # Position on left within safe area (X: 525, Y: 535)
    x_pos = 525
    y_name = 530
    y_tag = y_name + 98
    y_sch = y_tag + 38

    draw_cinematic_text(draw, (x_pos, y_name), ch_name, title_font, '#FFE600', '#000000', 5, 6)
    draw_cinematic_text(draw, (x_pos, y_tag), ch_tag, sub_font, '#FFFFFF', '#000000', 3, 4)
    draw_cinematic_text(draw, (x_pos, y_sch), ch_sch, sch_font, '#00F0FF', '#000000', 2, 3)

    out_branded = os.path.join(ASSETS_DIR, 'dossier_zero_banner_branded_2560x1440.png')
    branded.save(out_branded, 'PNG')
    print(f"[OK] Saved branded banner: {out_branded}", flush=True)

def main():
    print("=======================================================================", flush=True)
    print("=== THE DOSSIER ZERO: BRAND ASSET GENERATOR (cx/gpt-5.5-image)       ===", flush=True)
    print("=== Stickman + Realistic Cinematic Aesthetic | Anti-AI Slop         ===", flush=True)
    print("=======================================================================\n", flush=True)

    raw_paths = {}
    for name, config in ASSETS_TO_GENERATE.items():
        raw_paths[name] = generate_image(name, config)
        time.sleep(1.0)

    if 'avatar_profile_raw' in raw_paths:
        postprocess_avatar(raw_paths['avatar_profile_raw'])

    if 'watermark_raw' in raw_paths:
        postprocess_watermark(raw_paths['watermark_raw'])

    if 'channel_banner_raw' in raw_paths:
        postprocess_banner(raw_paths['channel_banner_raw'])

    print("\n[COMPLETE] All The Dossier Zero Brand Assets Successfully Generated!", flush=True)

if __name__ == '__main__':
    main()
