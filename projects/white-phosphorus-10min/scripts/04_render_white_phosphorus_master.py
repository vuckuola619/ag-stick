import subprocess
import os
import sys
import time
import shutil

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\white-phosphorus-10min\export"
AUDIO_FILE = r"c:\Users\bati-\Documents\AG-Stick\projects\white-phosphorus-10min\audio\voiceover_mastered.wav"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

RAW_VIDEO = os.path.join(EXPORT_DIR, "white_phosphorus_10min_raw.mp4")
FINAL_MASTER = os.path.join(EXPORT_DIR, "the_devils_element_10min_master.mp4")
ARTIFACT_DIR = r"C:\Users\bati-\.gemini\antigravity\brain\d54641ca-b865-49ff-822f-44eb805801db"
ARTIFACT_MASTER = os.path.join(ARTIFACT_DIR, "the_devils_element_10min_master.mp4")

os.makedirs(EXPORT_DIR, exist_ok=True)

def render_white_phosphorus_remotion():
    print("=======================================================================", flush=True)
    print("=== [1/2] Rendering Remotion Composition 'WhitePhosphorus10Min'     ===", flush=True)
    print("===       (18,720 frames @ 30fps | Duration: 624.0s / 10:24)        ===", flush=True)
    print("=== Specs: 1920x1080 Widescreen, 32 Scenes, Strict Neon Rush 2D     ===", flush=True)
    print("=== Engine: --gl=angle --muted --concurrency=4                     ===", flush=True)
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
        "WhitePhosphorus10Min",
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
            # Filter output for meaningful progress logging
            if any(k in line_str for k in ['Rendered', 'Rendering', 'Bundling', 'Error', 'Done', '%', 'Finished']):
                print(f"  [Remotion] {line_str}")
                sys.stdout.flush()
    
    proc.wait()
    elapsed = time.time() - start_time
    print(f"\n[OK] Raw Video Render completed in {elapsed:.1f}s ({elapsed/60:.2f} mins).")
    
    if proc.returncode != 0:
        raise RuntimeError(f"Remotion render failed with exit code {proc.returncode}")
        
    if not os.path.exists(RAW_VIDEO) or os.path.getsize(RAW_VIDEO) == 0:
        raise RuntimeError(f"Rendered video missing or empty: {RAW_VIDEO}")

def mux_broadcast_audio():
    print("\n=======================================================================", flush=True)
    print("=== [2/2] Multiplexing Video with Master Kokoro 82M Broadcast Audio ===", flush=True)
    print(f"    Raw Video : {RAW_VIDEO}")
    print(f"    Master VO : {AUDIO_FILE} (EBU R128 -16 LUFS, True Peak -1dBFS)")
    print(f"    Target    : {FINAL_MASTER}")
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
        print("FFmpeg Muxing Error:", res.stderr)
        raise RuntimeError("FFmpeg muxing failed")
        
    size_mb = os.path.getsize(FINAL_MASTER) / (1024 * 1024)
    print(f"\n[SUCCESS] Final 10-Minute Documentary Master Generated!")
    print(f"  File : {FINAL_MASTER}")
    print(f"  Size : {size_mb:.2f} MB")

    # Mirror to brain artifact directory if possible
    if os.path.exists(ARTIFACT_DIR):
        try:
            shutil.copy2(FINAL_MASTER, ARTIFACT_MASTER)
            print(f"  Synced to artifact: {ARTIFACT_MASTER}")
        except Exception as e:
            print(f"  Artifact copy note: {e}")

if __name__ == "__main__":
    render_white_phosphorus_remotion()
    mux_broadcast_audio()
