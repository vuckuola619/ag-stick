import subprocess
import os
import sys
import time
import shutil

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\demon-core-10min"
EXPORT_DIR = os.path.join(PROJECT_DIR, "export")
AUDIO_FILE = os.path.join(PROJECT_DIR, "audio", "voiceover_mastered.wav")
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

RAW_VIDEO = os.path.join(EXPORT_DIR, "demon_core_10min_raw.mp4")
FINAL_MASTER = os.path.join(EXPORT_DIR, "the_demon_core_10min_master.mp4")

os.makedirs(EXPORT_DIR, exist_ok=True)

def render_demon_core_remotion():
    print("=======================================================================", flush=True)
    print("=== [1/2] Rendering Remotion Composition 'DemonCore10Min'           ===", flush=True)
    print("===       (~18,000 frames @ 30fps | Duration: ~10:00)               ===", flush=True)
    print("=== Specs: 1920x1080 Widescreen, 32 Scenes, Strict 2D Stickman      ===", flush=True)
    print("=== Engine: --gl=angle --muted --concurrency=4                      ===", flush=True)
    print("=======================================================================\n", flush=True)
    
    if os.path.exists(RAW_VIDEO):
        try:
            os.remove(RAW_VIDEO)
            print(f"[CLEANUP] Removed prior raw video: {RAW_VIDEO}", flush=True)
        except Exception as e:
            print(f"[WARN] Could not remove prior raw video: {e}", flush=True)

    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        "DemonCore10Min",
        RAW_VIDEO,
        "--gl=angle",
        "--muted",
        "--concurrency=4"
    ]
    
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
            line_str = line.strip()
            if any(k in line_str for k in ['Rendered', 'Rendering', 'Bundling', 'Error', 'Done', '%', 'Finished']):
                print(f"  [Remotion] {line_str}", flush=True)
    
    proc.wait()
    elapsed = time.time() - start_time
    print(f"\n[OK] Raw Video Render completed in {elapsed:.1f}s ({elapsed/60:.2f} mins).", flush=True)
    
    if proc.returncode != 0:
        raise RuntimeError(f"Remotion render failed with exit code {proc.returncode}")
        
    if not os.path.exists(RAW_VIDEO) or os.path.getsize(RAW_VIDEO) == 0:
        raise RuntimeError(f"Rendered video missing or empty: {RAW_VIDEO}")

def mux_broadcast_audio():
    print("\n=======================================================================", flush=True)
    print("=== [2/2] Multiplexing Video with Master Kokoro 82M Broadcast Audio ===", flush=True)
    print(f"    Raw Video : {RAW_VIDEO}", flush=True)
    print(f"    Master VO : {AUDIO_FILE} (EBU R128 -16 LUFS, True Peak -1dBFS)", flush=True)
    print(f"    Target    : {FINAL_MASTER}", flush=True)
    print("=======================================================================\n", flush=True)
    
    cmd = [
        FFMPEG, "-y",
        "-i", RAW_VIDEO,
        "-i", AUDIO_FILE,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        "-shortest",
        FINAL_MASTER
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg Muxing Error:", res.stderr, flush=True)
        raise RuntimeError("FFmpeg muxing failed")
        
    size_mb = os.path.getsize(FINAL_MASTER) / (1024 * 1024)
    print(f"\n[SUCCESS] Final 10-Minute Documentary Master Generated!", flush=True)
    print(f"  File : {FINAL_MASTER}", flush=True)
    print(f"  Size : {size_mb:.2f} MB", flush=True)

def main():
    render_demon_core_remotion()
    mux_broadcast_audio()

if __name__ == '__main__':
    main()
