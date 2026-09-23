import urllib.request
import urllib.error
import json
import time

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.6-luna-image'

with open('projects/the-dossier-zero/case-05-goiania-caesium/script/storyboard_48_scenes.json', 'r', encoding='utf-8') as f:
    sb = json.load(f)

sc = sb['scenes'][0]

payload = {
    'model': MODEL,
    'prompt': sc['codex_image_prompt'],
    'size': '1672x941',
    'n': 1
}

req = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
)

print("Sending request to 9router...", flush=True)
try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        print("Success:", resp.status)
        data = json.loads(resp.read().decode('utf-8'))
        print("Data keys:", list(data.keys()), flush=True)
        if 'data' in data and len(data['data']) > 0:
            import base64, shutil
            item = data['data'][0]
            raw = base64.b64decode(item['b64_json'])
            out1 = 'projects/the-dossier-zero/case-05-goiania-caesium/assets/scenes/scene_01.png'
            out2 = 'projects/wework-47-billion-illusion/remotion/public/assets/goiania_caesium_137/scenes/scene_01.png'
            with open(out1, 'wb') as f:
                f.write(raw)
            shutil.copyfile(out1, out2)
            print(f"[OK] Saved scene_01.png ({len(raw)} bytes)!", flush=True)
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8', errors='ignore')
    print(f"HTTPError {e.code}:\n{err_body}", flush=True)
except Exception as e:
    print(f"Error: {e}", flush=True)
