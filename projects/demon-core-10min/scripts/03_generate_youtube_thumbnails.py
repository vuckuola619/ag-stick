import urllib.request
import json
import base64
import os
import time

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

OUT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\demon-core-10min\thumbnails'
os.makedirs(OUT_DIR, exist_ok=True)

THUMBNAILS = [
    {
        'id': 'thumb_a_screwdriver_slip',
        'title': 'Variant A: The 1-Millimeter Screwdriver Slip',
        'prompt': (
            'High-CTR YouTube video thumbnail artwork in 2D cartoon vector stickman style, '
            'featuring a minimalist cartoon stick figure scientist with solid blank white circular head (#ffffff) and wide terrified cartoon eyes, '
            'holding a yellow flathead screwdriver that is slipping from between two metallic dome halves, '
            'an apocalyptic blinding radiant cobalt-blue (#00F0FF and #0055FF) Cherenkov ionization flash exploding outward with sharp shockwave rings, '
            'dark slate charcoal background (#101218) with intense glowing contrast, '
            'ultra-high CTR composition, strictly 2D vector art, bold clean outlines, no 3D CGI, no photorealism'
        )
    },
    {
        'id': 'thumb_b_tickling_the_dragon',
        'title': 'Variant B: Tickling the Dragon\'s Tail',
        'prompt': (
            'High-CTR YouTube video thumbnail artwork in 2D cartoon vector stickman style, '
            'featuring a minimalist stickman scientist with solid blank white circular head (#ffffff) standing beside a glowing silver plutonium core, '
            'nervously propping an upper metallic dome with a flathead screwdriver while a colossal shadowy sleeping dragon looms in the dark red smoky mist behind him, '
            'dramatic contrast between ominous crimson haze (#FF2244) and brilliant electric cyan (#00E5FF) radiation aura, '
            'dark charcoal background (#12141A), clean 2D vector linework, bold black strokes, no 3D CGI'
        )
    },
    {
        'id': 'thumb_c_1000_rads_flash',
        'title': 'Variant C: The 1,000 RAD Blue Flash',
        'prompt': (
            'High-CTR YouTube video thumbnail artwork in 2D cartoon vector stickman style, '
            'featuring a minimalist stickman scientist in white lab coat with solid blank white circular head (#ffffff) seen from behind in dramatic silhouette, '
            'shielding his face with an arm as a massive blinding electric cobalt-blue ionization fireball erupts from a metallic sphere on a laboratory table, '
            'casting long dramatic black vector shadows across the floor, '
            'ultra-high contrast dark slate background (#0E1117), clean flat 2D graphic art, no 3D CGI, no photorealism'
        )
    }
]

def main():
    print("=== GENERATING HIGH-CTR YOUTUBE THUMBNAIL SUITE (3 VARIANTS) ===")
    for idx, t in enumerate(THUMBNAILS):
        t_id = t['id']
        out_file = os.path.join(OUT_DIR, f"{t_id}.png")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
            print(f"[SKIP] {t_id} already exists.")
            continue
            
        print(f"[{idx+1}/3] Generating {t['title']} via 9Router (cx/gpt-5.5-image)...")
        payload = {
            'model': MODEL,
            'prompt': t['prompt'],
            'size': '1672x941'
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
                        print(f"[SUCCESS] Saved thumbnail {out_file} ({len(img_bytes)} bytes)")
        except Exception as e:
            print(f"[ERROR] Failed {t_id}: {e}")
        time.sleep(2.0)

    print("\n[FINISHED] High-CTR Thumbnail Generation Complete!")

if __name__ == '__main__':
    main()
