import math
import struct
import wave
import subprocess
import os
import json

FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
VOICE_FILE = os.path.join(EXPORT_DIR, "narration.mp3")
SFX_WAV = os.path.join(EXPORT_DIR, "procedural_sfx.wav")
FINAL_AUDIO = os.path.join(EXPORT_DIR, "master_soundtrack.wav")
TIMESTAMP_FILE = os.path.join(EXPORT_DIR, "sentence_timestamps.json")

SAMPLE_RATE = 48000

def get_duration():
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, encoding='utf-8') as f:
            data = json.load(f)
            return data.get('total_sec', 50.0) + 2.0
    return 52.0

TOTAL_SECONDS = get_duration()
TOTAL_SAMPLES = int(SAMPLE_RATE * TOTAL_SECONDS)

def generate_sfx_and_ambient():
    print(f"[1/3] Synthesizing prehistoric cave documentary ambient + SFX ({TOTAL_SECONDS:.2f}s)...")
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

    def add_metallic_drop(start_sec, amplitude=0.35):
        # Liquid mercury drop 'plink/bloop' sound
        start_idx = int(start_sec * SAMPLE_RATE)
        num_samples = int(0.06 * SAMPLE_RATE)
        for i in range(num_samples):
            idx = start_idx + i
            if idx >= TOTAL_SAMPLES:
                break
            t = i / SAMPLE_RATE
            freq = 1400.0 - (900.0 * (i / num_samples))
            env = math.exp(-35.0 * t)
            harm = math.sin(2 * math.pi * freq * t) + 0.3 * math.sin(2 * math.pi * (freq * 2.1) * t)
            audio[idx] += amplitude * env * harm

    def add_whoosh(start_sec, duration=0.4, amplitude=0.25):
        start_idx = int(start_sec * SAMPLE_RATE)
        num_samples = int(duration * SAMPLE_RATE)
        for i in range(num_samples):
            idx = start_idx + i
            if idx >= TOTAL_SAMPLES:
                break
            t = i / SAMPLE_RATE
            freq = 280.0 + (380.0 * math.sin(math.pi * (i / num_samples)))
            env = math.sin(math.pi * (i / num_samples))
            audio[idx] += amplitude * env * math.sin(2 * math.pi * freq * t)

    # 1. Atmospheric Cave Mystery Drone Bed (-22 dB)
    print("  -> Generating atmospheric cave resonance bed...")
    for i in range(TOTAL_SAMPLES):
        t = i / SAMPLE_RATE
        pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 1.5 * t)
        
        # Harmonic progression across narrative acts
        if t < 12.3:       # Act 1: The Dark Cave Curiosity (D minor: 146.8 Hz, 220 Hz)
            f1, f2 = 146.8, 220.0
        elif t < 25.7:     # Act 2: Fire & Shocking Reaction (F minor: 174.6 Hz, 261.6 Hz)
            f1, f2 = 174.6, 261.6
        elif t < 33.1:     # Act 3: Quicksilver Wonder (G minor: 196.0 Hz, 293.7 Hz)
            f1, f2 = 196.0, 293.7
        elif t < 41.3:     # Act 4: Chemical Heat 357°C (A minor: 220.0 Hz, 329.6 Hz)
            f1, f2 = 220.0, 329.6
        else:              # Act 5: Climax & Historical Legacy (D major: 146.8 Hz, 293.7 Hz)
            f1, f2 = 146.8, 293.7
            
        drone = (math.sin(2 * math.pi * f1 * t) * 0.038 +
                 math.sin(2 * math.pi * f2 * t) * 0.028 +
                 math.sin(2 * math.pi * (f1 * 0.5) * t) * 0.040) * (0.8 + 0.2 * pulse)
        audio[i] += drone

    # 2. SFX: Magical Cinnabar Crystal Shimmer at 3.67s
    print("  -> Adding Crystal Gemstone Shimmer at 3.67s...")
    add_tone(1567.98, 3.67, 1.2, 0.16, decay_rate=2.5) # G6
    add_tone(2093.00, 3.75, 1.0, 0.14, decay_rate=3.0) # C7
    add_tone(2637.02, 3.83, 0.8, 0.12, decay_rate=3.5) # E7

    # 3. SFX: Stone Throw & Fire Impact at 7.84s
    print("  -> Adding Fire Whoosh & Stone Throw at 7.84s...")
    add_whoosh(7.70, duration=0.35, amplitude=0.22)
    add_tone(110.0, 7.95, 0.5, 0.25, decay_rate=5.0) # thud
    add_tone(650.0, 8.00, 0.8, 0.14, decay_rate=4.0) # sizzle

    # 4. SFX: Dramatic Shock Riser at 12.33s ("Tiba-tiba hal mustahil terjadi!")
    print("  -> Adding Dramatic Suspense Riser at 12.33s...")
    add_tone(220.0, 12.33, 1.8, 0.20, decay_rate=0.8)
    add_tone(330.0, 12.45, 1.6, 0.18, decay_rate=0.8)
    add_tone(440.0, 12.60, 1.5, 0.16, decay_rate=0.8)

    # 5. SFX: Liquid Mercury Droplets Dripping & Sizzling at 15.0s to 18.5s
    print("  -> Adding Liquid Mercury Droplet Plinks at 15.0s - 18.5s...")
    droplet_times = [15.10, 15.55, 16.02, 16.48, 17.15, 17.80, 18.30]
    for dt in droplet_times:
        add_metallic_drop(dt, amplitude=0.28)

    # 6. SFX: Quicksilver Title Anthem at 25.74s ("Inilah merkuri, atau Quicksilver!")
    print("  -> Adding Quicksilver Brass Anthem at 25.74s...")
    add_tone(440.0, 25.74, 2.5, 0.24, decay_rate=1.2) # A4
    add_tone(554.37, 25.80, 2.4, 0.22, decay_rate=1.2) # C#5
    add_tone(659.25, 25.86, 2.3, 0.20, decay_rate=1.2) # E5
    add_tone(880.0, 25.92, 2.5, 0.18, decay_rate=1.0) # A5

    # 7. SFX: Scientific Thermal Meter Alarm (357°C) at 33.16s
    print("  -> Adding Thermal Reaction Pings at 33.16s...")
    for step in range(4):
        p_time = 33.16 + (step * 0.35)
        p_freq = 987.77 + (step * 180.0)
        add_tone(p_freq, p_time, 0.25, 0.15, decay_rate=4.0)

    # 8. SFX: Grand Finale Resolution Chime at 41.33s
    print("  -> Adding Grand Finale Chime at 41.33s...")
    add_tone(587.33, 41.33, 4.5, 0.22, decay_rate=0.6) # D5
    add_tone(739.99, 41.40, 4.5, 0.20, decay_rate=0.6) # F#5
    add_tone(880.00, 41.48, 4.5, 0.18, decay_rate=0.6) # A5
    add_tone(1174.66, 41.56, 5.0, 0.16, decay_rate=0.5) # D6

    # Save to WAV
    with wave.open(SFX_WAV, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        raw = bytearray()
        for sample in audio:
            clamped = max(-1.0, min(1.0, sample))
            val = int(clamped * 32767.0)
            raw.extend(struct.pack('<h', val))
        wf.writeframes(raw)
    print(f"[OK] SFX track saved: {SFX_WAV}")

def mix_with_voice():
    print("[2/3] Mixing Voiceover + Procedural SFX + Ambient Drone via FFmpeg...")
    cmd = [
        FFMPEG, "-y",
        "-i", VOICE_FILE,
        "-i", SFX_WAV,
        "-filter_complex",
        "[0:a]volume=1.05[voice];"
        "[1:a]volume=0.85[sfx];"
        "[voice][sfx]amix=inputs=2:duration=longest:dropout_transition=2[mixed];"
        "[mixed]loudnorm=I=-14:LRA=10:TP=-1.0[out]",
        "-map", "[out]",
        "-c:a", "pcm_s16le",
        FINAL_AUDIO
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("[ERROR]", res.stderr)
        return False
    print(f"[3/3] [SUCCESS] Broadcast master soundtrack ready: {FINAL_AUDIO}")
    return True

if __name__ == "__main__":
    generate_sfx_and_ambient()
    mix_with_voice()
