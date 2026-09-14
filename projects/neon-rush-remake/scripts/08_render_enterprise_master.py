import subprocess
import os
import sys
import time

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

RAW_VIDEO = os.path.join(EXPORT_DIR, "mercury_enterprise_raw.mp4")
AUDIO_FILE = os.path.join(EXPORT_DIR, "master_soundtrack_8min.wav")
FINAL_MASTER = os.path.join(EXPORT_DIR, "neon_rush_mercury_8min_enterprise_master.mp4")

os.makedirs(EXPORT_DIR, exist_ok=True)

def render_remotion():
    print("[1/2] Rendering Remotion Composition 'MercuryEnterprise8Min' (23,359 frames @ 30fps)...")
    print("      Using --gl=angle --muted --concurrency=4 for maximum stability...")
    
    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        "MercuryEnterprise8Min",
        RAW_VIDEO,
        "--gl=angle",
        "--muted",
        "--concurrency=4"
    ]
    
    start_time = time.time()
    proc = subprocess.Popen(cmd, cwd=REMOTION_DIR, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
    
    for line in iter(proc.stdout.readline, ''):
        if line:
            line_str = line.strip()
            if any(k in line_str for k in ['Rendered', 'Rendering', 'Bundling', 'Error', 'Done', '%']):
                print(f"  [Remotion] {line_str}")
                sys.stdout.flush()
    
    proc.wait()
    elapsed = time.time() - start_time
    print(f"\n[OK] Remotion raw render finished in {elapsed:.1f}s ({elapsed/60:.2f} mins).")
    
    if proc.returncode != 0:
        raise RuntimeError(f"Remotion render failed with exit code {proc.returncode}")

def mux_audio():
    print("[2/2] Multiplexing Video with Broadcast Master Audio (AAC 320k, 48kHz)...")
    
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
        print("FFmpeg Error:", res.stderr)
        raise RuntimeError("Failed to multiplex audio")
        
    size_mb = os.path.getsize(FINAL_MASTER) / (1024 * 1024)
    print(f"\n[SUCCESS] Final 8-Minute Enterprise Master Video Created!")
    print(f"  File: {FINAL_MASTER}")
    print(f"  Size: {size_mb:.2f} MB")

def main():
    render_remotion()
    mux_audio()

if __name__ == "__main__":
    main()
