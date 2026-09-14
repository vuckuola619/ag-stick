import json, urllib.request, uuid, base64, os

with open(r'C:\Users\bati-\.codex\auth.json', 'r') as f:
    codex_auth = json.load(f)

tokens = codex_auth.get('tokens', {})
acc_tok = tokens.get('access_token')
account_id = tokens.get('account_id')

headers = {
    "Authorization": f"Bearer {acc_tok}",
    "Content-Type": "application/json",
    "chatgpt-account-id": account_id,
    "originator": "codex_cli_rs",
    "User-Agent": "codex_cli_rs/0.136.0",
    "session_id": str(uuid.uuid4()),
    "x-client-request-id": str(uuid.uuid4()),
    "Accept": "text/event-stream, application/json"
}

prompt = (
    "A vintage tactile paper cutout editorial collage representing financial asset-liability mismatch: "
    "a massive crumbling corporate office building anchored to a giant heavy 15-year iron chain, "
    "balanced precariously on a see-saw against a tiny ticking 30-day stopwatch and fragile paper contracts blowing away in the wind. "
    "Tactile torn paper edges, vintage financial ledger textures, high contrast dramatic lighting, isolated on dark charcoal background, "
    "editorial documentary art style, no random gibberish text."
)

tool_def = {
    "type": "image_generation",
    "output_format": "png",
    "size": "1024x1024"
}

body = {
    "model": "gpt-5.5",
    "instructions": "",
    "input": [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": prompt}]
        }
    ],
    "tools": [tool_def],
    "tool_choice": "auto",
    "parallel_tool_calls": False,
    "prompt_cache_key": str(uuid.uuid4()),
    "stream": True,
    "store": False,
    "reasoning": None
}

req = urllib.request.Request(
    "https://chatgpt.com/backend-api/codex/responses",
    data=json.dumps(body).encode('utf-8'),
    headers=headers
)

print("Generating Scene 17 asset via Codex...")
with urllib.request.urlopen(req, timeout=90) as res:
    found_image = False
    while True:
        line = res.readline()
        if not line:
            break
        line_str = line.decode('utf-8', errors='ignore').strip()
        if line_str.startswith('data:') and 'image_generation_call' in line_str:
            try:
                d = json.loads(line_str[5:].strip())
                item = d.get('item', {})
                if item.get('type') == 'image_generation_call' and item.get('result'):
                    b64 = item['result']
                    out_path = os.path.join("remotion", "public", "assets", "images", "scene_17_sprite.png")
                    with open(out_path, "wb") as img_f:
                        img_f.write(base64.b64decode(b64))
                    print(f"SUCCESS! Saved Scene 17 sprite to {out_path} ({len(b64)} bytes)")
                    found_image = True
            except Exception as e:
                print("Error parsing image chunk:", e)

if not found_image:
    print("Failed to find image in stream.")
