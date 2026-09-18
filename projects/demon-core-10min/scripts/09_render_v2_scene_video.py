"""
Render AG-Stick v2 Single Scene / Level Video.

Renders DemonCoreV2Scene24 (The 9-Beat 'One Millimeter Slip' Sequence)
with synchronized Kokoro VO audio and dynamic camera/character choreography.
"""

import subprocess
import os
import sys
import time

ROOT_DIR = r"c:\Users\bati-\Documents\AG-Stick"
REMOTION_DIR = os.path.join(ROOT_DIR, "projects", "wework-47-billion-illusion", "remotion")
EXPORT_DIR = os.path.join(ROOT_DIR, "projects", "demon-core-10min", "export")
TARGET_MP4 = os.path.join(EXPORT_DIR, "demon_core_v2_scene24_9beats.mp4")

os.makedirs(EXPORT_DIR, exist_ok=True)


def render_scene_video(composition_id: str = "DemonCoreV2Scene24", output_file: str = TARGET_MP4):
    print("=======================================================================", flush=True)
    print(f"=== AG-Stick v2: Rendering 1 Scene Video: '{composition_id}'      ===", flush=True)
    print("=== Format: 1920x1080 @ 30fps | Multi-Beat 2D Animation Engine      ===", flush=True)
    print("=======================================================================\n", flush=True)

    if os.path.exists(output_file):
        try:
            os.remove(output_file)
            print(f"[CLEANUP] Removed prior video: {output_file}", flush=True)
        except Exception as e:
            print(f"[WARN] Could not remove prior video: {e}", flush=True)

    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        composition_id,
        output_file,
        "--gl=angle",
        "--concurrency=4"
    ]

    print(f"Executing: {' '.join(cmd)}", flush=True)
    start_time = time.time()
    
    proc = subprocess.Popen(
        cmd,
        cwd=REMOTION_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    for line in iter(proc.stdout.readline, ''):
        if line:
            l = line.strip()
            if any(k in l for k in ['Rendered', 'Rendering', 'Bundling', 'Error', 'Done', '%', 'Finished', 'Output', 'Copying']):
                if '%' in l or 'Rendered' in l or 'Done' in l or 'Output' in l:
                    print(f"  [Remotion] {l}", flush=True)

    proc.wait()
    elapsed = time.time() - start_time

    if proc.returncode != 0:
        raise RuntimeError(f"Remotion render failed with code {proc.returncode}")

    if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
        raise RuntimeError(f"Rendered video is missing or empty: {output_file}")

    size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print("\n=======================================================================", flush=True)
    print(f"[SUCCESS] Scene Video Render Complete in {elapsed:.1f}s!", flush=True)
    print(f"  Target File : {output_file}", flush=True)
    print(f"  File Size   : {size_mb:.2f} MB", flush=True)
    print("=======================================================================", flush=True)
    return output_file


if __name__ == "__main__":
    render_scene_video()
