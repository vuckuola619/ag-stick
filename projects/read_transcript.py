import json

transcript_path = r'C:\Users\bati-\.gemini\antigravity\brain\a926fc75-5442-4599-8c8a-2e999219b029\.system_generated\logs\transcript.jsonl'

with open(transcript_path, encoding='utf-8') as f:
    for line in f:
        item = json.loads(line)
        idx = item.get('step_index')
        if idx in range(695, 715):
            print(f"--- STEP {idx} ({item.get('type')}) ---")
            if 'tool_calls' in item:
                for tc in item['tool_calls']:
                    print(f"Tool: {tc.get('name')}")
                    args = tc.get('args', {})
                    if 'CommandLine' in args:
                        print("CMD:", args['CommandLine'][:500])
            if item.get('type') == 'GENERIC':
                print("CONTENT:", item.get('content')[:300])
