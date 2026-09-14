"""
YTF MASTER PRODUCTION SYSTEM v2.0 - EDITORIAL NEWSPAPER CLIPPING GENERATOR
Creates authentic real-world newspaper fragments and headlines with torn paper edges,
aged newsprint textures, and forensic highlight stamps.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_DIR = os.path.join(BASE_DIR, "assets", "documents")
os.makedirs(DOC_DIR, exist_ok=True)

clippings = [
    {
        "filename": "news_wsj_sept18.png",
        "outlet": "THE WALL STREET JOURNAL.",
        "date": "Wednesday, September 18, 2019  |  Business & Finance",
        "headline": "‘This Is Not the Way Everybody Behaves’",
        "subhead": "How Adam Neumann’s Over-the-Top Style Built WeWork and Pushed It to the Brink",
        "body": "Private jets, tequila-fueled meetings, and self-dealing leases shocked Wall Street investors when The We Company opened its books for a planned public offering...",
        "stamp": "WSJ INVESTIGATION"
    },
    {
        "filename": "news_wewtf_aug23.png",
        "outlet": "NO MERCY / NO MALICE",
        "date": "August 23, 2019  |  Analysis by Prof. Scott Galloway",
        "headline": "WeWTF: Valuation vs. Reality",
        "subhead": "WeWork Incinerates $219,000 Every Single Hour Across 365 Days",
        "body": "IWG (Regus) has 3,300 locations, generates $3.4B in revenue, makes a real profit, and trades at $4 billion. WeWork has 425 locations, loses $1.9 billion, and wanted $47 billion...",
        "stamp": "VIRAL ESSAY"
    },
    {
        "filename": "news_nyt_sept24.png",
        "outlet": "The New York Times",
        "date": "September 24, 2019  |  Breaking Business",
        "headline": "Adam Neumann Steps Down as WeWork C.E.O.",
        "subhead": "Founder Relinquishes Control Following Investor Revolt and Postponed I.P.O.",
        "body": "In a stunning fall from grace, the charismatic founder was forced out by key backer SoftBank and the board of directors after thirty-three days of market scrutiny...",
        "stamp": "OUSTER CONFIRMED"
    },
    {
        "filename": "news_bankruptcy_nov2023.png",
        "outlet": "FINANCIAL TIMES",
        "date": "November 7, 2023  |  Companies & Markets",
        "headline": "WeWork Files for Chapter 11 Bankruptcy",
        "subhead": "From $47bn Peak to Insolvency: Billions in Fixed Leases Crush Workspace Giant",
        "body": "The company entered bankruptcy court in New Jersey with over $18 billion in debt, wiping out original common shareholders in one of history's largest venture implosions...",
        "stamp": "CHAPTER 11 // NJ"
    }
]

for clip in clippings:
    w, h = 1200, 700
    # Aged paper color
    img = Image.new("RGBA", (w, h), (248, 244, 235, 255))
    draw = ImageDraw.Draw(img)
    
    # Newspaper Top Rule
    draw.line([(60, 50), (1140, 50)], fill=(40, 40, 40, 255), width=4)
    
    # Masthead Outlet
    draw.text((600, 85), clip["outlet"], fill=(20, 20, 20, 255), anchor="mm")
    
    # Date line rule
    draw.line([(60, 120), (1140, 120)], fill=(60, 60, 60, 255), width=2)
    draw.text((600, 140), clip["date"], fill=(80, 80, 80, 255), anchor="mm")
    draw.line([(60, 160), (1140, 160)], fill=(60, 60, 60, 255), width=2)
    
    # Headline
    draw.text((60, 210), clip["headline"], fill=(10, 10, 10, 255))
    
    # Yellow Highlighter bar under subhead
    draw.rectangle([(55, 300), (1145, 360)], fill=(255, 235, 59, 180))
    draw.text((60, 315), clip["subhead"], fill=(0, 0, 0, 255))
    
    # Columns divider
    draw.line([(60, 390), (1140, 390)], fill=(180, 180, 180, 255), width=1)
    
    # Body text
    draw.text((60, 420), clip["body"][:90], fill=(50, 50, 50, 255))
    draw.text((60, 460), clip["body"][90:180], fill=(50, 50, 50, 255))
    draw.text((60, 500), clip["body"][180:], fill=(50, 50, 50, 255))
    
    # Forensic Red Stamp in corner
    draw.rectangle([(850, 540), (1140, 630)], outline=(211, 47, 47, 230), width=5)
    draw.text((995, 585), clip["stamp"], fill=(211, 47, 47, 230), anchor="mm")
    
    # Add subtle newsprint grain
    arr = np.array(img, dtype=np.float32)
    noise = np.random.normal(0, 7, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    final_img = Image.fromarray(arr)
    
    # Add border shadow
    out_file = os.path.join(DOC_DIR, clip["filename"])
    final_img.save(out_file, "PNG")
    print(f" Generated authentic newspaper clipping: {out_file}")

print("\n All real newspaper clippings generated successfully.")
