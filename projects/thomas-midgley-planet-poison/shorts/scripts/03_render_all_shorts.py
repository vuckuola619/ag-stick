import subprocess
import os
import sys
import time

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\thomas-midgley-planet-poison\shorts\export"
os.makedirs(EXPORT_DIR, exist_ok=True)

SHORTS = [
    {
        "id": "DossierShorts01",
        "output": os.path.join(EXPORT_DIR, "shorts_01_inhaled_lead_master.mp4")
    },
    {
        "id": "DossierShorts02",
        "output": os.path.join(EXPORT_DIR, "shorts_02_ozone_atom_master.mp4")
    },
    {
        "id": "DossierShorts03",
        "output": os.path.join(EXPORT_DIR, "shorts_03_strangled_machine_master.mp4")
    }
]

def render_short(composition_id: str, output_path: str):
    print(f"\n==========================================", flush=True)
    print(f"RENDERING REMOTION SHORT: {composition_id}", flush=True)
    print(f"OUTPUT: {output_path}", flush=True)
    print(f"==========================================", flush=True)

    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        composition_id,
        output_path,
        "--concurrency=8",
        "--gl=angle",
        "--overwrite"
    ]

    t0 = time.time()
    res = subprocess.run(cmd, cwd=REMOTION_DIR, shell=True)
    elapsed = time.time() - t0

    if res.returncode == 0:
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"[SUCCESS] {composition_id} rendered in {elapsed:.1f}s ({size_mb:.2f} MB)", flush=True)
        return True
    else:
        print(f"[ERROR] Failed to render {composition_id} (code {res.returncode})", flush=True)
        return False

def main():
    print("=== AUTOMATED MULTI-SHORTS RENDER RUNNER ===", flush=True)
    success = 0
    for sh in SHORTS:
        ok = render_short(sh["id"], sh["output"])
        if ok:
            success += 1

    print(f"\n[SUMMARY] Successfully rendered {success}/{len(SHORTS)} Shorts.", flush=True)

if __name__ == "__main__":
    main()
