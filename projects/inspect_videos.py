import urllib.request
import json
import re

def inspect_video(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    
    # Title
    t_match = re.search(r'<title>(.*?)</title>', html)
    title = t_match.group(1) if t_match else "Unknown"
    
    # Description
    d_match = re.search(r'"shortDescription":"(.*?)"', html)
    desc = d_match.group(1) if d_match else ""
    
    # View count
    v_match = re.search(r'"viewCount":"(\d+)"', html)
    views = v_match.group(1) if v_match else "0"
    
    print(f"VIDEO ID: {video_id}")
    print(f"TITLE: {title}")
    print(f"VIEWS: {views}")
    print(f"DESC: {desc[:400]}")
    print("-" * 50)

inspect_video("v9QbFkgYj9k") # Besi
inspect_video("wFs9zy7JXfY") # Merkuri
inspect_video("oTXtRyWqUPU") # Timah
inspect_video("UWTMgo69D2o") # Kubis
