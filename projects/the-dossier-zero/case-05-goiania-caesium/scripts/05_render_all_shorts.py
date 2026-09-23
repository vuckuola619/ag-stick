import subprocess
import os
import sys
import time

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero\case-05-goiania-caesium\shorts\export"
os.makedirs(EXPORT_DIR, exist_ok=True)

SHORTS = [
    {
        "id": "GoianiaShorts01",
        "output": os.path.join(EXPORT_DIR, "goiania_short_01_glowing_girl_master.mp4")
    },
    {
        "id": "GoianiaShorts02",
        "output": os.path.join(EXPORT_DIR, "goiania_short_02_deadliest_bus_ride_master.mp4")
    },
    {
        "id": "GoianiaShorts03",
        "output": os.path.join(EXPORT_DIR, "goiania_short_03_700kg_lead_coffin_master.mp4")
    }
]

def render_short(composition_id: str, output_path: str):
    print(f"\n==========================================", flush=True)
    print(f"RENDERING GOIANIA REMOTION SHORT: {composition_id}", flush=True)
    print(f"OUTPUT: {output_path}", flush=True)
    print(f"==========================================", flush=True)

    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        composition_id,
        output_path,
        "--concurrency=4",
        "--gl=angle",
        "--overwrite"
    ]

    t0 = time.time()
    res = subprocess.run(cmd, cwd=REMOTION_DIR, shell=True)
    elapsed = time.time() - t0

    if res.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"[SUCCESS] {composition_id} rendered in {elapsed:.1f}s ({size_mb:.2f} MB)", flush=True)
        return True
    else:
        print(f"[ERROR] Failed to render {composition_id} (code {res.returncode})", flush=True)
        return False

def main():
    print("=== THE DOSSIER ZERO: GOIANIA SHORTS AUTOMATED RENDER RUNNER ===", flush=True)
    success = 0
    for sh in SHORTS:
        ok = render_short(sh["id"], sh["output"])
        if ok:
            success += 1

    print(f"\n[SUMMARY] Successfully rendered {success}/{len(SHORTS)} Goiânia Shorts.", flush=True)

if __name__ == "__main__":
    main()
