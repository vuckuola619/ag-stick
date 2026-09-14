import urllib.request
import json
import re

url = 'https://www.youtube.com/@NeonRush-f3s/videos'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

idx = html.find('var ytInitialData = ')
if idx != -1:
    end_idx = html.find(';</script>', idx)
    data = json.loads(html[idx + len('var ytInitialData = '):end_idx])
    with open('neon_rush_channel.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print("Channel data dumped successfully.")
else:
    print("ytInitialData not found.")
