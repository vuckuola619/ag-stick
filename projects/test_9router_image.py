import urllib.request
import json
import base64
import os

url = 'http://127.0.0.1:20128/v1/images/generations'
api_key = 'sk-c4f2444795b190b3-kzvd4h-ea839762'

payload = {
    'model': 'cx/gpt-5.5-image',
    'prompt': 'A funny caveman stickman with messy wild brown hair, big cartoon expressive eyes, holding a glowing red cinnabar crystal stone, thick crisp outlines, pure white background, high contrast, clean vector style',
    'size': '1024x1024'
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
)

print("Sending request to 9router cx/gpt-5.5-image...")
try:
    with urllib.request.urlopen(req, timeout=90) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("Success! Keys:", list(res.keys()))
        if 'data' in res and len(res['data']) > 0:
            item = res['data'][0]
            print("Data item keys:", list(item.keys()))
            if 'b64_json' in item:
                img_data = base64.b64decode(item['b64_json'])
                os.makedirs('projects/neon_rush_analysis/test_gen', exist_ok=True)
                with open('projects/neon_rush_analysis/test_gen/test_stickman.png', 'wb') as f:
                    f.write(img_data)
                print(f"Saved test image ({len(img_data)} bytes)")
            elif 'url' in item:
                print("Image URL:", item['url'])
except Exception as e:
    print("Error:", e)
    if hasattr(e, 'read'):
        print("Error body:", e.read().decode('utf-8', errors='ignore'))
