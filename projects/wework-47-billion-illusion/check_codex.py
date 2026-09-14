import re

with open(r'C:\Users\bati-\AppData\Roaming\npm\node_modules\9router\app\.next-cli-build\server\chunks\8236.js', 'r', encoding='utf-8') as f:
    s = f.read()

m = re.search(r'\{id:"codex",[^;]+\}', s)
if m:
    print(m.group(0)[:1500])
else:
    matches = [m.start() for m in re.finditer(r'id:"codex"', s)]
    print('Matches:', matches)
    for idx in matches:
        print(s[idx-50:idx+600])
        print('='*50)
