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

BASE_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\chrono-vault-branding'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
os.makedirs(ASSETS_DIR, exist_ok=True)

# Master Neon Rush 2D Cartoon Style Formula
STYLE_SUFFIX = (
    ', in the signature 2D vector cartoon illustration style of YouTube channel Neon Rush, '
    'featuring the iconic minimalist stickman character with a blank solid white circular head (#ffffff), '
    'simple expressive wide cartoon eyes, thin black stick limbs with bold ink strokes, '
    'bold crisp 8-10px black ink outlines on every character, object, and environment, '
    'clean flat cel-shading, vibrant high-contrast colors, '
    'punchy high CTR YouTube framing, perfectly centered cinematic composition, '
    'strictly no 3D CGI, no photorealism, no realistic human faces, no chrome ray-tracing, '
    'no photographic textures, strictly no text, no letters, no labels, no watermark'
)

ASSETS_TO_GENERATE = {
    'avatar_profile_raw': {
        'prompt': (
            'Centered iconic YouTube channel profile avatar for a mysterious history and unsolved world events documentary channel. '
            'Close-up bust shot of a minimalist 2D cartoon stickman investigator with a solid blank white circular head (#ffffff), '
            'expressive wide curious cartoon eyes with comic ink pupils, wearing a dark 1940s detective trench coat and a stylish tilted fedora hat. '
            'The stickman holds a glowing retro magnifying glass that casts intense vibrant cyan (#00F0FF) and warm amber (#FFAA00) rim highlights across his face. '
            'Dark mysterious midnight navy circular background (#0c0f1d) with subtle glowing compass rose reticle and coordinates in dark slate'
            + STYLE_SUFFIX
        ),
        'size': '1024x1024',
    },
    'channel_banner_raw': {
        'prompt': (
            'Epic wide YouTube channel banner illustration for a mysterious history and unsolved world events documentary channel. '
            'Centered cinematic wide composition: a minimalist 2D cartoon stickman investigator with a solid white circular head (#ffffff) '
            'in a detective trench coat standing in a cavernous secret underground archive vault, examining a huge glowing wooden planning table '
            'strewn with ancient nautical maps, classified dossier folders, and strange glowing artifacts. '
            'The background is filled with towering archive bookshelves, giant chalkboards with timeline diagrams and mysterious symbols, '
            'faint silhouettes of ancient pyramids and the Mariana Trench in deep atmospheric mist. '
            'High contrast lighting with glowing lantern amber (#FFAA00) and electric spectral cyan (#00F0FF), dark midnight charcoal architecture (#0d101b)'
            + STYLE_SUFFIX
        ),
        'size': '1672x941',
    },
    'watermark_raw': {
        'prompt': (
            'Minimalist YouTube video branding corner watermark badge icon on a solid dark slate background (#111420). '
            'Centered graphic symbol: a 2D cartoon minimalist stickman head with a blank solid white circle (#ffffff), '
            'sharp wide cartoon eyes, wearing a black detective fedora hat, set inside a bold glowing circular nautical compass crosshair ring '
            'with bright neon cyan (#00F0FF) and gold amber (#FFE600) accents. '
            'Ultra-bold 12px black ink borders, clean flat vector logo emblem, designed for maximum visibility at small thumbnail size'
            + STYLE_SUFFIX
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
    # Resize with high quality Lanczos to standard 800x800 YouTube profile
    avatar = img.resize((800, 800), Image.Resampling.LANCZOS)
    
    # Save standard square 800x800
    out_square = os.path.join(ASSETS_DIR, 'youtube_profile_800x800.png')
    avatar.save(out_square, 'PNG')
    print(f"[OK] Saved {out_square}", flush=True)

    # Also create circular cropped preview for YouTube preview
    mask = Image.new('L', (800, 800), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, 800, 800), fill=255)
    
    avatar_circ = Image.new('RGBA', (800, 800), (0, 0, 0, 0))
    avatar_circ.paste(avatar, (0, 0), mask=mask)
    
    # Add subtle cyan/amber border rim around the circle
    draw_circ = ImageDraw.Draw(avatar_circ)
    draw_circ.ellipse((3, 3, 797, 797), outline='#00F0FF', width=6)
    
    out_circ = os.path.join(ASSETS_DIR, 'youtube_profile_circular_preview.png')
    avatar_circ.save(out_circ, 'PNG')
    print(f"[OK] Saved {out_circ}", flush=True)

def postprocess_watermark(raw_path: str):
    print("\n--- Processing YouTube Video Watermarks (512x512 & 150x150) ---", flush=True)
    img = Image.open(raw_path).convert('RGBA')
    
    # 512x512 Master Watermark
    wm_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    out_512 = os.path.join(ASSETS_DIR, 'youtube_watermark_512x512.png')
    wm_512.save(out_512, 'PNG')
    print(f"[OK] Saved {out_512}", flush=True)

    # 150x150 Official YouTube Corner Watermark
    wm_150 = img.resize((150, 150), Image.Resampling.LANCZOS)
    out_150 = os.path.join(ASSETS_DIR, 'youtube_watermark_150x150.png')
    wm_150.save(out_150, 'PNG')
    print(f"[OK] Saved {out_150}", flush=True)

    # Circular Transparent Watermark Badge Option
    mask = Image.new('L', (512, 512), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((10, 10, 502, 502), fill=255)
    
    wm_circ = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    wm_circ.paste(wm_512, (0, 0), mask=mask)
    draw_circ = ImageDraw.Draw(wm_circ)
    draw_circ.ellipse((10, 10, 502, 502), outline='#FFE600', width=8)
    draw_circ.ellipse((16, 16, 496, 496), outline='#00F0FF', width=4)
    
    out_circ_512 = os.path.join(ASSETS_DIR, 'youtube_watermark_transparent_circle_512x512.png')
    wm_circ.save(out_circ_512, 'PNG')
    out_circ_150 = os.path.join(ASSETS_DIR, 'youtube_watermark_transparent_circle_150x150.png')
    wm_circ.resize((150, 150), Image.Resampling.LANCZOS).save(out_circ_150, 'PNG')
    print(f"[OK] Saved transparent circle watermarks", flush=True)

def postprocess_banner(raw_path: str):
    print("\n--- Processing YouTube Channel Banner (2560x1440 Standard) ---", flush=True)
    # YouTube Official Banner Specs:
    # Canvas Size: 2560 x 1440 px (16:9)
    # Desktop & Mobile Safe Area (Guaranteed visible everywhere): 1546 x 423 px in center
    # Safe area coordinates:
    # X: (2560 - 1546) / 2 = 507 px to 2053 px
    # Y: (1440 - 423) / 2 = 508 px to 931 px
    
    banner_canvas = Image.new('RGBA', (2560, 1440), '#0c0f1a')
    
    # Open raw generated art
    raw_art = Image.open(raw_path).convert('RGBA')
    
    # Scale raw art to cover 2560 width (height becomes ~1440)
    raw_w, raw_h = raw_art.size
    aspect = raw_w / raw_h
    target_w = 2560
    target_h = int(target_w / aspect)
    
    art_scaled = raw_art.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Paste onto center of canvas
    offset_y = (1440 - target_h) // 2
    banner_canvas.paste(art_scaled, (0, offset_y))
    
    # Add top and bottom subtle cinematic gradient vignette
    vignette = Image.new('RGBA', (2560, 1440), (0, 0, 0, 0))
    draw_vig = ImageDraw.Draw(vignette)
    
    # Safe area boundaries
    safe_left = 507
    safe_right = 2053
    safe_top = 508
    safe_bottom = 931
    
    # Save clean unbranded 2560x1440 banner
    out_clean = os.path.join(ASSETS_DIR, 'youtube_banner_clean_art_2560x1440.png')
    banner_canvas.save(out_clean, 'PNG')
    print(f"[OK] Saved clean banner art: {out_clean}", flush=True)

    # Try loading Windows Impact & Arial fonts
    impact_path = r'C:\Windows\Fonts\impact.ttf'
    arialbd_path = r'C:\Windows\Fonts\arialbd.ttf'
    
    # Helper to draw text with heavy black outline and deep drop shadow (NO BOX/FIELD)
    def draw_cinematic_text(d, pos, text, font, fill, stroke_fill='#000000', stroke_w=4, shadow_dist=4):
        x, y = pos
        # Drop shadow
        d.text((x + shadow_dist, y + shadow_dist), text, font=font, fill='#000000')
        # Multi-directional stroke
        for dx in range(-stroke_w, stroke_w + 1):
            for dy in range(-stroke_w, stroke_w + 1):
                if dx != 0 or dy != 0:
                    d.text((x + dx, y + dy), text, font=font, fill=stroke_fill)
        # Main fill
        d.text((x, y), text, font=font, fill=fill)

    # --- VERSION 1: Centered Archway Placement (Above Character Head) ---
    branded_top = banner_canvas.copy()
    draw_top = ImageDraw.Draw(branded_top)
    
    title_font_top = ImageFont.truetype(impact_path, 80) if os.path.exists(impact_path) else ImageFont.load_default()
    sub_font_top = ImageFont.truetype(arialbd_path, 22) if os.path.exists(arialbd_path) else ImageFont.load_default()
    sch_font_top = ImageFont.truetype(arialbd_path, 16) if os.path.exists(arialbd_path) else ImageFont.load_default()

    ch_name = "CHRONO VAULT"
    ch_tag = "UNSOLVED WORLD EVENTS & BIZARRE HISTORY"
    ch_sch = "NEW DOCUMENTARY EVERY THURSDAY • @CHRONOVAULTDOCS"

    # Centered horizontally at 1280
    bb_t = draw_top.textbbox((0, 0), ch_name, font=title_font_top)
    w_t = bb_t[2] - bb_t[0]
    
    bb_s = draw_top.textbbox((0, 0), ch_tag, font=sub_font_top)
    w_s = bb_s[2] - bb_s[0]
    
    bb_c = draw_top.textbbox((0, 0), ch_sch, font=sch_font_top)
    w_c = bb_c[2] - bb_c[0]

    # Y: inside safe zone (508 - 931), just above the stickman head (head is at ~620)
    y_t = 525
    y_s = y_t + 78
    y_c = y_s + 32

    draw_cinematic_text(draw_top, (1280 - w_t // 2, y_t), ch_name, title_font_top, '#FFE600', '#000000', 4, 5)
    draw_cinematic_text(draw_top, (1280 - w_s // 2, y_s), ch_tag, sub_font_top, '#FFFFFF', '#000000', 3, 4)
    draw_cinematic_text(draw_top, (1280 - w_c // 2, y_c), ch_sch, sch_font_top, '#00F0FF', '#000000', 2, 3)

    out_top = os.path.join(ASSETS_DIR, 'youtube_banner_branded_archway_2560x1440.png')
    branded_top.save(out_top, 'PNG')
    print(f"[OK] Saved archway branded banner: {out_top}", flush=True)

    # --- VERSION 2: Left-Flanked Editorial Placement (Safe Zone Compliant) ---
    branded_left = banner_canvas.copy()
    draw_left = ImageDraw.Draw(branded_left)

    title_font_l = ImageFont.truetype(impact_path, 94) if os.path.exists(impact_path) else ImageFont.load_default()
    sub_font_l = ImageFont.truetype(arialbd_path, 23) if os.path.exists(arialbd_path) else ImageFont.load_default()
    sch_font_l = ImageFont.truetype(arialbd_path, 17) if os.path.exists(arialbd_path) else ImageFont.load_default()

    x_l = 525
    y_tl = 530
    y_sl = y_tl + 94
    y_cl = y_sl + 35

    draw_cinematic_text(draw_left, (x_l, y_tl), ch_name, title_font_l, '#FFE600', '#000000', 5, 6)
    draw_cinematic_text(draw_left, (x_l, y_sl), ch_tag, sub_font_l, '#FFFFFF', '#000000', 3, 4)
    draw_cinematic_text(draw_left, (x_l, y_cl), ch_sch, sch_font_l, '#00F0FF', '#000000', 2, 3)

    out_left = os.path.join(ASSETS_DIR, 'youtube_banner_branded_left_2560x1440.png')
    branded_left.save(out_left, 'PNG')
    # Also save as main branded banner
    branded_left.save(os.path.join(ASSETS_DIR, 'youtube_banner_branded_2560x1440.png'), 'PNG')
    print(f"[OK] Saved left-flanked branded banner: {out_left}", flush=True)

def main():
    print("=======================================================================", flush=True)
    print("=== CHRONO VAULT: YOUTUBE BRAND ASSET GENERATOR (9Router cx/gpt-5.5) ===", flush=True)
    print("=== Target: Profile Avatar, 2560x1440 Banner, Video Watermarks       ===", flush=True)
    print("=======================================================================\n", flush=True)

    # 1. Generate Raw Assets via 9Router
    raw_paths = {}
    for name, config in ASSETS_TO_GENERATE.items():
        raw_paths[name] = generate_image(name, config)
        time.sleep(1.0)

    # 2. Post-Process Production Deliverables
    if 'avatar_profile_raw' in raw_paths:
        postprocess_avatar(raw_paths['avatar_profile_raw'])

    if 'watermark_raw' in raw_paths:
        postprocess_watermark(raw_paths['watermark_raw'])

    if 'channel_banner_raw' in raw_paths:
        postprocess_banner(raw_paths['channel_banner_raw'])

    print("\n[COMPLETE] All YouTube Brand Assets Generated and Processed Successfully!", flush=True)

if __name__ == '__main__':
    main()
