import os
import subprocess
import time

FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export"
NARRATION = os.path.join(EXPORT_DIR, "narration.mp3")

YT_RAW = os.path.join(EXPORT_DIR, "scaling_10m_youtube_v2.mp4")
YT_FINAL = os.path.join(EXPORT_DIR, "scaling_10m_youtube_final.mp4")

TT_RAW = os.path.join(EXPORT_DIR, "scaling_10m_tiktok_v1.mp4")
TT_FINAL = os.path.join(EXPORT_DIR, "scaling_10m_tiktok_final.mp4")

def remux_and_master(input_vid, output_vid, label):
    if not os.path.exists(input_vid):
        print(f"[WAIT] {label} raw video not found yet: {input_vid}")
        return False

    print(f"[START] Mastering {label}...")
    cmd = [
        FFMPEG, "-y",
        "-i", input_vid,
        "-i", NARRATION,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        "-af", "loudnorm=I=-14:LRA=11:TP=-1.0",
        "-shortest",
        output_vid
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[ERROR] {label} failed: {res.stderr}")
        return False

    size_mb = os.path.getsize(output_vid) / (1024 * 1024)
    print(f"[SUCCESS] {label} Mastered: {output_vid} ({size_mb:.2f} MB)")
    return True

if __name__ == "__main__":
    remux_and_master(YT_RAW, YT_FINAL, "YouTube 16:9")
    remux_and_master(TT_RAW, TT_FINAL, "TikTok 9:16")
