import urllib.request
import json
import re

query = 'neon rush'
url = f'https://www.youtube.com/results?search_query={urllib.parse.quote(query)}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Find ytInitialData
idx = html.find('var ytInitialData = ')
if idx != -1:
    end_idx = html.find(';</script>', idx)
    json_str = html[idx + len('var ytInitialData = '):end_idx]
    try:
        data = json.loads(json_str)
        with open('yt_search.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print("Wrote yt_search.json")
    except Exception as e:
        print("JSON parse error:", e)
else:
    print("ytInitialData not found")
