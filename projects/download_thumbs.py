import urllib.request
import os

os.makedirs('projects/neon_rush_analysis/thumbs', exist_ok=True)

vids = {
    'tin': 'oTXtRyWqUPU',
    'iron': 'v9QbFkgYj9k',
    'cabbage': 'UWTMgo69D2o',
    'mercury': 'wFs9zy7JXfY'
}

for name, vid in vids.items():
    for quality in ['maxresdefault.jpg', 'hqdefault.jpg']:
        url = f"https://i.ytimg.com/vi/{vid}/{quality}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req).read()
            out_path = f"projects/neon_rush_analysis/thumbs/{name}_{quality}"
            with open(out_path, 'wb') as f:
                f.write(data)
            print(f"Downloaded {out_path} ({len(data)} bytes)")
            break
        except Exception as e:
            continue
