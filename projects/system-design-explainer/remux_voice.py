import os
import subprocess

OUTPUT_AUDIO = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\narration.mp3"
INPUT_VIDEO = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\scaling_10m_master.mp4"
FINAL_VIDEO = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\scaling_10m_master_voiced.mp4"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

print("[1/2] Remuxing with explicit stream mapping (-map 0:v:0 -map 1:a:0)...")
cmd = [
    FFMPEG, "-y",
    "-i", INPUT_VIDEO,
    "-i", OUTPUT_AUDIO,
    "-map", "0:v:0",
    "-map", "1:a:0",
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "320k",
    "-af", "loudnorm=I=-14:LRA=11:TP=-1.0",
    "-shortest",
    FINAL_VIDEO
]
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("[ERROR]", res.stderr)
else:
    size_mb = os.path.getsize(FINAL_VIDEO) / (1024 * 1024)
    print(f"[2/2] [SUCCESS] Final voiced video ready: {FINAL_VIDEO} ({size_mb:.2f} MB)")
