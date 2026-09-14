import subprocess
import os
import shutil

FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
PUBLIC_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets"

VOICE_WAV = os.path.join(EXPORT_DIR, "kokoro_english_8min_48k.wav")
MUSIC_WAV = os.path.join(EXPORT_DIR, "soundtrack_8min_raw.wav")
OUT_MIX = os.path.join(EXPORT_DIR, "master_soundtrack_english_8min.wav")
PUBLIC_MIX = os.path.join(PUBLIC_DIR, "master_soundtrack_english_8min.wav")

def mix_broadcast_audio():
    print("[MIX] Blending Kokoro 82M English Voiceover with 8-Minute Cinematic Ambient Soundtrack...")
    
    # Filter graph:
    # 1. Voice [0:a] is normalized and boosted slightly for clear presence (amplify 1.15)
    # 2. Music [1:a] is trimmed to match voice length (494.45s + 2s tail), volume lowered to -18dB (0.13), fade in 2s, fade out last 3s
    # 3. amix combines them
    # 4. loudnorm standardizes to -16 LUFS for YouTube broadcast
    
    duration = 494.45
    fade_out_start = duration
    total_dur = duration + 2.5
    
    filter_complex = (
        f"[0:a]volume=1.2[v];"
        f"[1:a]atrim=0:{total_dur},asetpts=PTS-STARTPTS,volume=0.14,afade=t=in:ss=0:d=2.0,afade=t=out:st={fade_out_start}:d=2.5[m];"
        f"[v][m]amix=inputs=2:duration=first:dropout_transition=2[mix];"
        f"[mix]loudnorm=I=-16:TP=-1.5:LRA=11[out]"
    )
    
    cmd = [
        FFMPEG, "-y",
        "-i", VOICE_WAV,
        "-i", MUSIC_WAV,
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-ar", "48000",
        "-ac", "2",
        OUT_MIX
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg Error:", res.stderr)
        raise RuntimeError("FFmpeg mixing failed")
        
    shutil.copy2(OUT_MIX, PUBLIC_MIX)
    print(f"[OK] Master Broadcast Audio ready: {OUT_MIX}")
    print(f"[OK] Copied to Remotion Assets: {PUBLIC_MIX}")

if __name__ == "__main__":
    mix_broadcast_audio()
