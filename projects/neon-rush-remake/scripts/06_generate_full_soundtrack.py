import math
import struct
import wave
import subprocess
import os
import json

FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
VOICE_FILE = os.path.join(EXPORT_DIR, "narration_8min.mp3")
SFX_WAV = os.path.join(EXPORT_DIR, "soundtrack_8min_raw.wav")
FINAL_AUDIO = os.path.join(EXPORT_DIR, "master_soundtrack_8min.wav")
TIMESTAMP_FILE = os.path.join(EXPORT_DIR, "sentence_timestamps_8min.json")
CHAPTERS_FILE = os.path.join(EXPORT_DIR, "chapters_8min.json")

SAMPLE_RATE = 48000

def get_duration():
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, encoding="utf-8") as f:
            data = json.load(f)
            return data.get("total_sec", 776.6) + 3.0
    return 780.0

TOTAL_SECONDS = get_duration()
TOTAL_SAMPLES = int(SAMPLE_RATE * TOTAL_SECONDS)

def generate_multi_movement_soundtrack():
    print(f"[1/3] Generating 8-Movement Enterprise Ambient Soundtrack ({TOTAL_SECONDS:.2f}s, {TOTAL_SAMPLES} samples)...")
    audio = [0.0] * TOTAL_SAMPLES

    def add_tone(freq, start_sec, duration_sec, amplitude, decay_rate=0.0):
        start_idx = int(start_sec * SAMPLE_RATE)
        num_samples = int(duration_sec * SAMPLE_RATE)
        for i in range(num_samples):
            idx = start_idx + i
            if idx >= TOTAL_SAMPLES:
                break
            t = i / SAMPLE_RATE
            env = math.exp(-decay_rate * t) if decay_rate > 0 else 1.0
            if i < 480:
                env *= (i / 480)
            elif i > num_samples - 480:
                env *= ((num_samples - i) / 480)
            audio[idx] += amplitude * env * math.sin(2 * math.pi * freq * t)

    def add_metallic_drop(start_sec, amplitude=0.25):
        start_idx = int(start_sec * SAMPLE_RATE)
        num_samples = int(0.08 * SAMPLE_RATE)
        for i in range(num_samples):
            idx = start_idx + i
            if idx >= TOTAL_SAMPLES:
                break
            t = i / SAMPLE_RATE
            freq = 1500.0 - (950.0 * (i / num_samples))
            env = math.exp(-30.0 * t)
            harm = math.sin(2 * math.pi * freq * t) + 0.35 * math.sin(2 * math.pi * (freq * 2.2) * t)
            audio[idx] += amplitude * env * harm

    def add_whoosh(start_sec, duration=0.6, amplitude=0.18):
        start_idx = int(start_sec * SAMPLE_RATE)
        num_samples = int(duration * SAMPLE_RATE)
        for i in range(num_samples):
            idx = start_idx + i
            if idx >= TOTAL_SAMPLES:
                break
            t = i / SAMPLE_RATE
            freq = 180.0 + (320.0 * math.sin(math.pi * (i / num_samples)))
            env = math.sin(math.pi * (i / num_samples))
            audio[idx] += amplitude * env * math.sin(2 * math.pi * freq * t)

    def add_deep_strike(start_sec, freq=55.0, duration=3.5, amplitude=0.35):
        start_idx = int(start_sec * SAMPLE_RATE)
        num_samples = int(duration * SAMPLE_RATE)
        for i in range(num_samples):
            idx = start_idx + i
            if idx >= TOTAL_SAMPLES:
                break
            t = i / SAMPLE_RATE
            env = math.exp(-1.4 * t)
            strike = (math.sin(2 * math.pi * freq * t) +
                      0.5 * math.sin(2 * math.pi * (freq * 1.5) * t) +
                      0.25 * math.sin(2 * math.pi * (freq * 2.76) * t))
            audio[idx] += amplitude * env * strike

    # Harmonic drone progression matching the 8 acts
    print("  -> Computing dynamic harmonic drone layer across 8 movements...")
    for i in range(TOTAL_SAMPLES):
        t = i / SAMPLE_RATE
        
        # 8 distinct tonal movements
        if t < 93.88:        # Movement 1: Stone Age Cave Mystique (D minor: 73.4 Hz, 146.8 Hz, 220.0 Hz)
            f0, f1, f2 = 73.4, 146.8, 220.0
            amp = 0.035
        elif t < 194.48:     # Movement 2: Roaring Fire & Mercury Discovery (F minor: 87.3 Hz, 174.6 Hz, 261.6 Hz)
            f0, f1, f2 = 87.3, 174.6, 261.6
            amp = 0.040
        elif t < 304.02:     # Movement 3: Peculiar Physics & Floating Metals (G minor: 98.0 Hz, 196.0 Hz, 293.7 Hz)
            f0, f1, f2 = 98.0, 196.0, 293.7
            amp = 0.038
        elif t < 400.73:     # Movement 4: Mausoleum of Emperor Qin Shi Huang (C minor: 65.4 Hz, 130.8 Hz, 196.0 Hz)
            f0, f1, f2 = 65.4, 130.8, 196.0
            amp = 0.042
        elif t < 484.32:     # Movement 5: European Alchemy & Newton's Secret Lab (E minor: 82.4 Hz, 164.8 Hz, 246.9 Hz)
            f0, f1, f2 = 82.4, 164.8, 246.9
            amp = 0.036
        elif t < 578.34:     # Movement 6: Torricelli Barometer & Scientific Dawn (D major: 73.4 Hz, 146.8 Hz, 293.7 Hz)
            f0, f1, f2 = 73.4, 146.8, 293.7
            amp = 0.037
        elif t < 684.84:     # Movement 7: Mad Hatter & Minamata Tragedy (B minor: 61.7 Hz, 123.5 Hz, 185.0 Hz)
            f0, f1, f2 = 61.7, 123.5, 185.0
            amp = 0.042
        else:                # Movement 8: Cosmic Dawn, NASA Ion Drive & Quantum Future (C major: 65.4 Hz, 130.8 Hz, 261.6 Hz)
            f0, f1, f2 = 65.4, 130.8, 261.6
            amp = 0.045
            
        slow_lfo = 0.8 + 0.2 * math.sin(2 * math.pi * 0.25 * t)
        drone = (math.sin(2 * math.pi * f0 * t) * 0.45 +
                 math.sin(2 * math.pi * f1 * t) * 0.35 +
                 math.sin(2 * math.pi * f2 * t) * 0.20) * amp * slow_lfo
        audio[i] += drone

    # Add chapter transition gongs/strikes
    print("  -> Adding cinematic transition hits at each chapter mark...")
    chapter_times = [0.1, 93.88, 194.48, 304.02, 400.73, 484.32, 578.34, 684.84]
    for ct in chapter_times:
        add_deep_strike(ct, freq=65.0, duration=4.0, amplitude=0.30)
        add_whoosh(max(0, ct - 0.3), duration=0.7, amplitude=0.15)

    # Add recurring metallic mercury drops in Acts 2, 3, 4, 5
    print("  -> Adding liquid mercury drop cascades...")
    drop_moments = [
        105.2, 112.4, 118.6, 125.0, 132.8, 140.5, 155.2, 168.4, 180.2, # Act 2
        205.0, 218.4, 230.1, 245.5, 262.3, 278.0, 290.4,               # Act 3
        320.0, 335.2, 350.4, 368.1, 385.0,                              # Act 4
        415.0, 430.4, 448.2, 465.0,                                     # Act 5
        500.2, 520.4, 545.1, 560.0,                                     # Act 6
        700.0, 715.4, 730.2, 755.0                                      # Act 8
    ]
    for dm in drop_moments:
        if dm < TOTAL_SECONDS:
            add_metallic_drop(dm, amplitude=0.18)
            add_metallic_drop(dm + 0.12, amplitude=0.12)

    # 16-bit PCM normalization & export
    print(f"  -> Writing raw PCM soundtrack to {SFX_WAV}...")
    max_val = max(max(audio), -min(audio), 1e-6)
    scale = 26000.0 / max_val  # Keep headroom for narration

    with wave.open(SFX_WAV, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        buf = bytearray()
        for s in audio:
            val = int(max(min(s * scale, 32767), -32768))
            buf.extend(struct.pack("<h", val))
        wf.writeframes(buf)
    print(f"[OK] Raw soundtrack generated: {SFX_WAV} ({os.path.getsize(SFX_WAV)} bytes)")

def mix_with_ffmpeg():
    print("[2/3] Mixing Voiceover + 8-Movement Ambient Soundtrack with EBU R128 loudnorm...")
    remotion_public_dest = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\master_soundtrack_8min.wav"

    cmd = [
        FFMPEG, "-y",
        "-i", VOICE_FILE,
        "-i", SFX_WAV,
        "-filter_complex",
        "[0:a]volume=1.0[v];"
        "[1:a]volume=0.35,lowpass=f=4500[m];"
        "[v][m]amix=inputs=2:duration=first:dropout_transition=2[mix];"
        "[mix]loudnorm=I=-16:TP=-1.5:LRA=11[out]",
        "-map", "[out]",
        "-c:a", "pcm_s16le",
        "-ar", "48000",
        FINAL_AUDIO
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg Error:", res.stderr)
        raise RuntimeError("Failed to mix soundtrack")

    print(f"[OK] Final Broadcast Master Soundtrack: {FINAL_AUDIO} ({os.path.getsize(FINAL_AUDIO)} bytes)")
    
    # Copy to Remotion public assets
    import shutil
    shutil.copy2(FINAL_AUDIO, remotion_public_dest)
    print(f"[OK] Deployed to Remotion public assets: {remotion_public_dest}")

def main():
    generate_multi_movement_soundtrack()
    mix_with_ffmpeg()
    print("\n[COMPLETE] 8-Minute Enterprise Audio Master is ready!")

if __name__ == "__main__":
    main()
