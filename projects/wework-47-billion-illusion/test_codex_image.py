import json, urllib.request, uuid

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
            "content": [
                {
                    "type": "input_text",
                    "text": "A vintage retro paper cut-out collage illustration of a collapsing corporate skyscraper made of playing cards and financial documents, editorial magazine style, rich colors, high contrast, isolated on black background"
                }
            ]
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

print("Sending image generation request to Codex backend...")
try:
    with urllib.request.urlopen(req, timeout=60) as res:
        print("Status:", res.status)
        found_image = False
        while True:
            line = res.readline()
            if not line:
                break
            line_str = line.decode('utf-8', errors='ignore').strip()
            if line_str.startswith('event:'):
                event_name = line_str[6:].strip()
                if event_name in ['response.image_generation_call.partial_image', 'response.output_item.done', 'response.done']:
                    print("Event:", event_name)
            elif line_str.startswith('data:'):
                data_str = line_str[5:].strip()
                if 'image_generation_call' in data_str:
                    print("Detected image_generation_call data!")
                    try:
                        d = json.loads(data_str)
                        item = d.get('item', {})
                        if item.get('type') == 'image_generation_call' and item.get('result'):
                            b64 = item['result']
                            print(f"SUCCESS! Received image result, length={len(b64)}")
                            found_image = True
                            import base64
                            with open("test_generated_image.png", "wb") as img_f:
                                img_f.write(base64.b64decode(b64))
                            print("Saved to test_generated_image.png")
                    except Exception as e:
                        print("Parse error:", e)
        print("Stream ended. Found image:", found_image)
except urllib.error.HTTPError as e:
    print("HTTPError:", e.code, e.read().decode('utf-8', errors='ignore'))
except Exception as e:
    print("Error:", e)
