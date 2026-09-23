import urllib.request
import json
import time

payload = {
    'model': 'cx/gpt-5.6-luna-image',
    'prompt': 'A minimalist stickman character with round white head holding glowing blue crystal on black background, 2D vector style',
    'size': '1024x1024'
}

req = urllib.request.Request(
    'http://127.0.0.1:20128/v1/images/generations',
    data=json.dumps(payload).encode(),
    headers={
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-c4f2444795b190b3-kzvd4h-ea839762'
    }
)

t0 = time.time()
print("Testing cx/gpt-5.6-luna-image...", flush=True)
try:
    with urllib.request.urlopen(req, timeout=90) as resp:
        print(f"Status: {resp.status} in {time.time() - t0:.1f}s", flush=True)
        d = json.loads(resp.read().decode())
        print("Received items:", len(d.get('data', [])))
except Exception as e:
    print("Error:", e, flush=True)
    if hasattr(e, 'read'):
        print("Body:", e.read().decode('utf-8', errors='ignore'), flush=True)
