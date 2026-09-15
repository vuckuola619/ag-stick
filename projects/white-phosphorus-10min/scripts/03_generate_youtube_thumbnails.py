import urllib.request
import json
import base64
import os
import time

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

OUT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\white-phosphorus-10min\thumbnails'
os.makedirs(OUT_DIR, exist_ok=True)

THUMBNAILS = [
    {
        'id': 'thumb_a_1500_gallons',
        'title': 'Variant A: The 1,500 Gallons Hook',
        'prompt': (
            'High-CTR YouTube video thumbnail illustration in 2D cartoon vector stickman style, '
            'featuring a minimalist cartoon stickman with solid blank white circular head (#ffffff) and shocked expressive eyes, '
            'holding up a glowing translucent flask filled with intensely radiant toxic phosphor green (#00FF66) liquid cold fire, '
            'standing next to a massive towering wall of wooden barrels leaking amber fluid, '
            'giant bold punchy text in 3D neon yellow with black outline reading "1,500 GALLONS?!", '
            'dark slate background (#12141A) with vibrant toxic green and orange rim lighting, '
            'ultra-high contrast, 16:9 widescreen composition, no 3D CGI, clean 2D vector lines'
        )
    },
    {
        'id': 'thumb_b_glowing_jaw',
        'title': 'Variant B: Phossy Jaw Horror Hook',
        'prompt': (
            'High-CTR YouTube video thumbnail illustration in 2D cartoon vector stickman style, '
            'featuring a minimalist stickman character with solid blank white circular head (#ffffff) sitting in pitch black darkness, '
            'its lower jaw and teeth intensely radiating a brilliant fluorescent toxic phosphor green (#00FF66) glow, '
            'surrounded by a scientific medical crossbones warning sign, '
            'giant bold punchy typography in bright neon yellow with thick black outline reading "WHY DID IT GLOW?!", '
            'dark slate textured background (#0E1015), eerie green radioactive lighting, '
            'ultra-high contrast, 16:9 widescreen framing, no realistic human gore, clean 2D vector style'
        )
    },
    {
        'id': 'thumb_c_devils_element',
        'title': 'Variant C: The Dual Nature Hook',
        'prompt': (
            'High-CTR YouTube video thumbnail illustration in 2D cartoon vector stickman style, '
            'dramatic split-screen concept: a minimalist stickman with solid blank white circular head (#ffffff) holding an Element 15 flask, '
            'left half engulfed in raging hazard orange (#FF6B00) and toxic green fire with falling bombs, '
            'right half blooming with vibrant green wheat crops and electric cyan (#00E5FF) DNA double helix, '
            'giant bold punchy text in bright flame warning yellow with black stroke reading "FEEDS 4 BILLION?!", '
            'dark charcoal background (#12141A), maximum visual contrast, 16:9 widescreen, clean 2D vector stickman style'
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
            
        print(f"[{idx+1}/3] Generating {t['title']}...")
        payload = {
            'model': MODEL,
            'prompt': t['prompt'],
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

    print("All thumbnails generated successfully!")

if __name__ == '__main__':
    main()
