import subprocess
import os
import sys
import time

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

RAW_VIDEO = os.path.join(EXPORT_DIR, "mercury_english_8min_raw.mp4")
AUDIO_FILE = os.path.join(EXPORT_DIR, "master_soundtrack_english_8min.wav")
FINAL_MASTER = os.path.join(EXPORT_DIR, "neon_rush_mercury_english_8min_master.mp4")

os.makedirs(EXPORT_DIR, exist_ok=True)

def render_english_remotion():
    print("=== [1/2] Rendering Remotion Composition 'MercuryEnglish8Min' (14,833 frames @ 30fps) ===", flush=True)
    print("    Specs: 1920x1080, Kokoro 82M English Voiceover Sync, Titanium Glassmorphic HUD, 100% Consistent 9Router AI Concept Art", flush=True)
    print("    Using --gl=angle --muted --concurrency=4 for peak Windows stability...\n", flush=True)
    
    if os.path.exists(RAW_VIDEO):
        try:
            os.remove(RAW_VIDEO)
            print(f"Removed previous raw video: {RAW_VIDEO}", flush=True)
        except Exception as e:
            print(f"Could not remove previous raw video: {e}", flush=True)

    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        "MercuryEnglish8Min",
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
            if any(k in line_str for k in ['Rendered', 'Rendering', 'Bundling', 'Error', 'Done', '%']):
                print(f"  [Remotion] {line_str}")
                sys.stdout.flush()
    
    proc.wait()
    elapsed = time.time() - start_time
    print(f"\n[OK] English Video Render completed in {elapsed:.1f}s ({elapsed/60:.2f} mins).")
    
    if proc.returncode != 0:
        raise RuntimeError(f"Remotion render failed with exit code {proc.returncode}")

def mux_broadcast_audio():
    print("\n=== [2/2] Multiplexing Video with Master English Broadcast Audio ===")
    print(f"    Audio: {AUDIO_FILE} (AAC 320k, 48kHz Stereo, -16 LUFS)")
    print(f"    Output: {FINAL_MASTER}")
    
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
    print(f"\n[SUCCESS] Final 8-Minute English Enterprise Master Generated!")
    print(f"  Path: {FINAL_MASTER}")
    print(f"  Size: {size_mb:.2f} MB")

    # Copy to brain artifact directory
    artifact_master = r"C:\Users\bati-\.gemini\antigravity\brain\f39d64bf-6e51-40b4-92eb-7bf63798ce0e\neon_rush_mercury_english_8min_master.mp4"
    try:
        import shutil
        shutil.copy2(FINAL_MASTER, artifact_master)
        print(f"  Synced to artifact: {artifact_master}")
    except Exception as e:
        print(f"  Artifact copy note: {e}")

if __name__ == "__main__":
    render_english_remotion()
    mux_broadcast_audio()
