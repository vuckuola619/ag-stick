"""
YTF MASTER PRODUCTION SYSTEM v2.0 - REAL ARCHIVAL ASSET DOWNLOADER & PROCESSOR
Downloads verified historical photographs from Wikimedia Commons and constructs
genuine photo cut-out puppet heads and collage elements.
"""

import os
import requests
from PIL import Image, ImageOps, ImageFilter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAR_DIR = os.path.join(BASE_DIR, "assets", "characters")
BG_DIR = os.path.join(BASE_DIR, "assets", "backgrounds")
os.makedirs(CHAR_DIR, exist_ok=True)
os.makedirs(BG_DIR, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) YTF-MasterEngine/2.0'}

downloads = [
    {
        "name": "adam_neumann_real_disrupt.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/65/TechCrunch_Disrupt_NY_2015_-_Day_2_%2817192687298%29.jpg",
        "dir": CHAR_DIR
    },
    {
        "name": "adam_neumann_real_portrait.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Mr._Adam_Neumann%2C_Founder_WeWork_%28Start_Up_India_Participant%29_call_on_the_Prime_Minister%2C_Shri_Narendra_Modi%2C_in_New_Delhi_on_January_15%2C_2016_-_cropped.jpg",
        "dir": CHAR_DIR
    },
    {
        "name": "masayoshi_son_real.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/58/Masayoshi_Son_%28P066533-522034%2C_cropped%29.jpg",
        "dir": CHAR_DIR
    },
    {
        "name": "wework_building_real_01.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b2/WeWork1UniversityAvenueToronto.jpg",
        "dir": BG_DIR
    },
    {
        "name": "wework_building_real_02.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/85/1711_Rhode_Island_Avenue_NW.jpg",
        "dir": BG_DIR
    }
]

for item in downloads:
    dest = os.path.join(item["dir"], item["name"])
    print(f"Downloading {item['name']}...")
    try:
        r = requests.get(item["url"], headers=headers, timeout=20)
        if r.status_code == 200:
            with open(dest, "wb") as f:
                f.write(r.content)
            print(f" Saved: {dest} ({len(r.content):,} bytes)")
        else:
            print(f" Failed ({r.status_code}): {item['name']}")
    except Exception as e:
        print(f" Error: {e}")

# Process real photo cut-out heads with white paper borders
def create_cutout_head(img_path, out_path, crop_box):
    if not os.path.exists(img_path):
        return
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    
    # Calculate crop coordinates
    x1, y1, x2, y2 = int(w * crop_box[0]), int(h * crop_box[1]), int(w * crop_box[2]), int(h * crop_box[3])
    cropped = img.crop((x1, y1, x2, y2))
    
    # Create elliptical paper cutout mask
    mask = Image.new("L", cropped.size, 0)
    from PIL import ImageDraw
    draw = ImageDraw.Draw(mask)
    draw.ellipse((10, 10, cropped.size[0] - 10, cropped.size[1] - 10), fill=255)
    
    # Apply mask
    cutout = Image.new("RGBA", cropped.size, (0, 0, 0, 0))
    cutout.paste(cropped, (0, 0), mask=mask)
    
    # Add tactile white paper border
    border_mask = mask.filter(ImageFilter.MaxFilter(15))
    border_img = Image.new("RGBA", cropped.size, (255, 255, 255, 255))
    
    final_head = Image.new("RGBA", cropped.size, (0, 0, 0, 0))
    final_head.paste(border_img, (0, 0), mask=border_mask)
    final_head.paste(cutout, (0, 0), mask=mask)
    
    final_head.save(out_path, "PNG")
    print(f" Created genuine photographic cut-out puppet head: {out_path}")

# Adam Neumann Head from real photo
create_cutout_head(
    os.path.join(CHAR_DIR, "adam_neumann_real_portrait.jpg"),
    os.path.join(CHAR_DIR, "adam_real_cutout_head.png"),
    [0.15, 0.05, 0.85, 0.70]
)

# Masayoshi Son Head from real photo
create_cutout_head(
    os.path.join(CHAR_DIR, "masayoshi_son_real.jpg"),
    os.path.join(CHAR_DIR, "masa_real_cutout_head.png"),
    [0.15, 0.02, 0.85, 0.70]
)

print("\n Real archival asset processing complete.")
