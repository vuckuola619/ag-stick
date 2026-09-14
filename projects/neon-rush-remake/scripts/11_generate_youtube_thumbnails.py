import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
THUMBNAIL_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\thumbnails"
os.makedirs(THUMBNAIL_DIR, exist_ok=True)

# Helper for fonts
try:
    font_xl = ImageFont.truetype("arialbd.ttf", 86)
    font_lg = ImageFont.truetype("arialbd.ttf", 64)
    font_md = ImageFont.truetype("arialbd.ttf", 40)
    font_badge = ImageFont.truetype("arialbd.ttf", 28)
except:
    font_xl = ImageFont.load_default()
    font_lg = ImageFont.load_default()
    font_md = ImageFont.load_default()
    font_badge = ImageFont.load_default()

# -------------------------------------------------------------
# THUMBNAIL VARIANT 1: "THE LIVING SILVER" (High-CTR Curiosity)
# -------------------------------------------------------------
def create_thumb_v1():
    base_path = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\scenes\scene_05.png"
    img = Image.open(base_path).convert("RGBA").resize((1280, 720), Image.Resampling.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(1.22)
    img = ImageEnhance.Color(img).enhance(1.20)
    
    overlay = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Left dark gradient to make text pop
    for x in range(750):
        alpha = int(220 * (1.0 - (x / 750.0) ** 1.3))
        draw.line([(x, 0), (x, 720)], fill=(5, 8, 17, alpha))
        
    # Top Category Badge (Crimson Red with White Text)
    draw.rectangle([60, 50, 310, 94], fill=(239, 68, 68, 255))
    draw.text((75, 58), "SCIENCE MYSTERY", font=font_badge, fill=(255, 255, 255, 255))
    
    # Yellow Highlight Box 1: THE FORBIDDEN
    draw.rectangle([64, 114, 694, 204], fill=(0, 0, 0, 220))
    draw.rectangle([60, 110, 690, 200], fill=(250, 204, 21, 255))
    draw.text((80, 118), "THE FORBIDDEN", font=font_xl, fill=(0, 0, 0, 255))
    
    # White Highlight Box 2: LIQUID METAL
    draw.rectangle([64, 218, 634, 308], fill=(0, 0, 0, 220))
    draw.rectangle([60, 214, 630, 304], fill=(255, 255, 255, 255))
    draw.text((80, 222), "LIQUID METAL", font=font_xl, fill=(10, 15, 30, 255))
    
    # Stat Pill (Bottom Left)
    draw.rounded_rectangle([60, 580, 480, 650], radius=12, fill=(15, 23, 42, 230), outline=(250, 204, 21, 255), width=2)
    draw.text((80, 600), "● 13.5x HEAVIER THAN WATER", font=font_badge, fill=(250, 204, 21, 255))
    
    # Element Chip (Top Right)
    draw.rounded_rectangle([1120, 50, 1220, 150], radius=14, fill=(15, 23, 42, 240), outline=(255, 255, 255, 180), width=3)
    draw.text((1142, 60), "Hg", font=font_lg, fill=(255, 255, 255, 255))
    draw.text((1152, 118), "80", font=font_badge, fill=(239, 68, 68, 255))
    
    final_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_file = os.path.join(THUMBNAIL_DIR, "thumbnail_v1_forbidden_liquid_metal.jpg")
    final_img.save(out_file, quality=95)
    print(f"[OK] Created Thumbnail V1: {out_file}")

# -------------------------------------------------------------
# THUMBNAIL VARIANT 2: "DEFIES GRAVITY" (Density / Physics Focus)
# -------------------------------------------------------------
def create_thumb_v2():
    base_path = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\scenes\scene_06.png"
    img = Image.open(base_path).convert("RGBA").resize((1280, 720), Image.Resampling.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(1.25)
    img = ImageEnhance.Color(img).enhance(1.15)
    
    overlay = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    for x in range(800):
        alpha = int(225 * (1.0 - (x / 800.0) ** 1.3))
        draw.line([(x, 0), (x, 720)], fill=(6, 10, 20, alpha))
        
    draw.rectangle([60, 50, 320, 94], fill=(6, 182, 212, 255))
    draw.text((75, 58), "IMPOSSIBLE PHYSICS", font=font_badge, fill=(5, 8, 17, 255))
    
    draw.rectangle([64, 114, 624, 204], fill=(0, 0, 0, 220))
    draw.rectangle([60, 110, 620, 200], fill=(239, 68, 68, 255))
    draw.text((80, 118), "IRON FLOATS", font=font_xl, fill=(255, 255, 255, 255))
    
    draw.rectangle([64, 218, 584, 308], fill=(0, 0, 0, 220))
    draw.rectangle([60, 214, 580, 304], fill=(255, 255, 255, 255))
    draw.text((80, 222), "ON THIS.", font=font_xl, fill=(10, 15, 30, 255))
    
    draw.rounded_rectangle([60, 580, 440, 650], radius=12, fill=(15, 23, 42, 230), outline=(6, 182, 212, 255), width=2)
    draw.text((80, 600), "● DENSITY: 13.53 g/cm³", font=font_badge, fill=(6, 182, 212, 255))
    
    draw.rounded_rectangle([1120, 50, 1220, 150], radius=14, fill=(15, 23, 42, 240), outline=(6, 182, 212, 255), width=3)
    draw.text((1142, 60), "Hg", font=font_lg, fill=(255, 255, 255, 255))
    draw.text((1152, 118), "80", font=font_badge, fill=(6, 182, 212, 255))
    
    final_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_file = os.path.join(THUMBNAIL_DIR, "thumbnail_v2_iron_floats.jpg")
    final_img.save(out_file, quality=95)
    print(f"[OK] Created Thumbnail V2: {out_file}")

# -------------------------------------------------------------
# THUMBNAIL VARIANT 3: "THE EMPEROR'S CURSE" (Historical / Imperial)
# -------------------------------------------------------------
def create_thumb_v3():
    base_path = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\scenes\scene_08.png"
    img = Image.open(base_path).convert("RGBA").resize((1280, 720), Image.Resampling.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(1.24)
    img = ImageEnhance.Color(img).enhance(1.25)
    
    overlay = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    for x in range(800):
        alpha = int(230 * (1.0 - (x / 800.0) ** 1.3))
        draw.line([(x, 0), (x, 720)], fill=(7, 10, 22, alpha))
        
    draw.rectangle([60, 50, 310, 94], fill=(234, 179, 8, 255))
    draw.text((75, 58), "SECRET HISTORY", font=font_badge, fill=(10, 15, 30, 255))
    
    draw.rectangle([64, 114, 694, 204], fill=(0, 0, 0, 220))
    draw.rectangle([60, 110, 690, 200], fill=(255, 255, 255, 255))
    draw.text((80, 118), "100 RIVERS OF", font=font_xl, fill=(10, 15, 30, 255))
    
    draw.rectangle([64, 218, 594, 308], fill=(0, 0, 0, 220))
    draw.rectangle([60, 214, 590, 304], fill=(234, 179, 8, 255))
    draw.text((80, 222), "MERCURY", font=font_xl, fill=(0, 0, 0, 255))
    
    draw.rounded_rectangle([60, 580, 480, 650], radius=12, fill=(15, 23, 42, 230), outline=(234, 179, 8, 255), width=2)
    draw.text((80, 600), "● TOMB OF QIN SHI HUANG", font=font_badge, fill=(234, 179, 8, 255))
    
    draw.rounded_rectangle([1120, 50, 1220, 150], radius=14, fill=(15, 23, 42, 240), outline=(234, 179, 8, 255), width=3)
    draw.text((1142, 60), "Hg", font=font_lg, fill=(255, 255, 255, 255))
    draw.text((1152, 118), "80", font=font_badge, fill=(234, 179, 8, 255))
    
    final_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_file = os.path.join(THUMBNAIL_DIR, "thumbnail_v3_100_mercury_rivers.jpg")
    final_img.save(out_file, quality=95)
    print(f"[OK] Created Thumbnail V3: {out_file}")

def main():
    create_thumb_v1()
    create_thumb_v2()
    create_thumb_v3()
    print("\nAll 3 High-CTR YouTube Thumbnails successfully generated!")

if __name__ == "__main__":
    main()
