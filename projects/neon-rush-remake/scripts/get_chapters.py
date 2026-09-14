import json

with open(r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export\sentence_timestamps_8min.json", encoding="utf-8") as f:
    d = json.load(f)

act_triggers = [
    ("BABAK 1: BATU MERAH DARAH & OBSESI PURBA", "Pernahkah kalian membayangkan"),
    ("BABAK 2: TRAGEDI API UNGGUN & LAHIRNYA PERAK HIDUP", "Malam itu, di dalam sebuah gua batu"),
    ("BABAK 3: FISIKA ANEH AIR RAKSA: LOGAM YANG MELAWAN LOGIKA", "Apa yang sebenarnya membuat air raksa"),
    ("BABAK 4: AMBISI KEABADIAN KAISAR QIN SHI HUANG", "Keajaiban fisik inilah yang membuat para penguasa"),
    ("BABAK 5: MISTERI ALKIMIA BARAT & BATU BERTUAH", "Sementara di belahan dunia Barat"),
    ("BABAK 6: REVOLUSI INDUSTRI: MENIMBANG ANGIN & MENGUKUR SUHU", "Memasuki abad ketujuh belas"),
    ("BABAK 7: KUTUKAN RACUN TAK KASAT MATA: MAD HATTER & MINAMATA", "Namun, di balik semua jasa besarnya"),
    ("BABAK 8: ERA ANTARIKSA & MASA DEPAN MERKURI", "Meski kini penggunaan air raksa dibatasi")
]

chapters = []
for title, trigger in act_triggers:
    found = False
    for i, s in enumerate(d["sentences"]):
        if trigger.lower() in s["text"].lower():
            chapters.append({
                "title": title,
                "sentence_idx": i,
                "start_sec": s["start_sec"],
                "start_frame": s["start_frame"]
            })
            found = True
            break
    if not found:
        print("NOT FOUND:", title)

print("\n--- CHAPTER BREAKDOWN ---")
for c in chapters:
    sec = c["start_sec"]
    m = int(sec // 60)
    s = int(sec % 60)
    print(f"{m:02d}:{s:02d} ({sec:6.2f}s) | Frame {c['start_frame']:5d} | {c['title']}")

with open(r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export\chapters_8min.json", "w", encoding="utf-8") as f:
    json.dump(chapters, f, indent=2)

remotion_dest = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\chapters_8min.json"
with open(remotion_dest, "w", encoding="utf-8") as f:
    json.dump(chapters, f, indent=2)

print("\n[OK] Chapters saved and deployed to Remotion public assets!")
