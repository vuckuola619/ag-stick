import json, urllib.request

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
    "Accept": "text/event-stream, application/json"
}

body = {
    "model": "gpt-5.5",
    "input": [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": "Hello, answer in 1 word: 'READY'"}]
        }
    ],
    "store": False,
    "stream": True
}

req = urllib.request.Request(
    "https://chatgpt.com/backend-api/codex/responses",
    data=json.dumps(body).encode('utf-8'),
    headers=headers
)

try:
    with urllib.request.urlopen(req, timeout=15) as res:
        print("Status:", res.status)
        first_chunk = res.read(500).decode('utf-8', errors='ignore')
        print("Response chunk:", first_chunk)
except urllib.error.HTTPError as e:
    print("HTTPError:", e.code, e.read().decode('utf-8', errors='ignore')[:300])
except Exception as e:
    print("Error:", e)
