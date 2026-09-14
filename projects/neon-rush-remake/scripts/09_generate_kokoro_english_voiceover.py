import kokoro_onnx
import soundfile as sf
import subprocess
import os
import json

ONNX_MODEL = r"C:\Users\bati-\Documents\AG-VOX\models\kokoro\kokoro-v1.0.onnx"
VOICES_BIN = r"C:\Users\bati-\Documents\AG-VOX\models\kokoro\voices-v1.0.bin"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
PUBLIC_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets"

os.makedirs(EXPORT_DIR, exist_ok=True)
os.makedirs(PUBLIC_DIR, exist_ok=True)

# 18 Modular Scenes tailored for Kokoro 82M
SCENES_SCRIPT = [
    {
        "id": 1,
        "title": "THE PREHISTORIC DISCOVERY",
        "tag": "ÇATALHÖYÜK, 7000 BCE",
        "stat": "COEVAL WITH DAWN OF CIVILIZATION",
        "text": "Nine thousand years ago, deep inside the dark limestone caverns of ancient Anatolia, primitive hunters discovered something extraordinary. Embedded in the cold rock walls were veins of a brilliant, blood-red crystal that seemed to glow in the flickering torchlight."
    },
    {
        "id": 2,
        "title": "THE SACRED CINNABAR",
        "tag": "MINERAL: α-HgS",
        "stat": "MOHS HARDNESS: 2.0 – 2.5",
        "text": "This mysterious crimson rock was cinnabar, natural mercury sulfide. To stone-age humans, red was the sacred color of life, blood, and fire. They believed this strange stone held supernatural power bestowed directly by the gods."
    },
    {
        "id": 3,
        "title": "THE RITUAL POWDER",
        "tag": "VERMILION PIGMENT",
        "stat": "FUNERARY SKULL BURIALS",
        "text": "They ground the crimson crystals into an ultra-fine powder called vermilion. Ancient shamans painted running beasts and sacred handprints onto cave walls, and coated the bones of their ancestors to grant them immortality in the afterlife."
    },
    {
        "id": 4,
        "title": "THE CAMPFIRE ACCIDENT",
        "tag": "PRIMITIVE SMELTING",
        "stat": "COAL TEMP: > 500°C",
        "text": "Then came the accident that changed chemistry forever. One night, around a roaring campfire exceeding five hundred degrees Celsius, a curious caveman tossed a fist-sized lump of red cinnabar directly into the burning coals to see what would happen."
    },
    {
        "id": 5,
        "title": "THERMAL DISSOCIATION",
        "tag": "2HgS + 3O₂ → 2Hg + 2SO₂↑",
        "stat": "BOILING POINT: 356.7°C",
        "text": "Within moments, choking fumes of sulfur dioxide filled the air, stinging their eyes. The intense heat broke the chemical bonds of the mineral, releasing pure metallic mercury vapor that drifted upward toward the cool stones above."
    },
    {
        "id": 6,
        "title": "THE LIVING SILVER",
        "tag": "HYDRARGYRUM",
        "stat": "MELTING POINT: -38.8°C",
        "text": "As the hot metallic vapor touched the cold cave rocks, it condensed instantly. The burning red rock appeared to bleed bright droplets of liquid silver. When the hunter touched it, it did not wet his skin at all, rolling across the stone like living chrome."
    },
    {
        "id": 7,
        "title": "ANOMALOUS DENSITY",
        "tag": "DENSITY: 13.53 g/cm³",
        "stat": "13.5x HEAVIER THAN WATER",
        "text": "Mercury is the only stable metal on Earth that is liquid at room temperature. But its most shocking property is its sheer density: thirteen point five grams per cubic centimeter. A single gallon weighs over one hundred and ten pounds."
    },
    {
        "id": 8,
        "title": "IRON FLOATS EFFORTLESSLY",
        "tag": "HYDROSTATIC BUOYANCY",
        "stat": "41.8% VOLUME ABOVE SURFACE",
        "text": "Because mercury is so dense, a solid heavy cast-iron cannonball dropped into a pool of quicksilver will not sink. It bobs and floats on the silvery surface like a plastic toy in a swimming pool, defying everyday human intuition."
    },
    {
        "id": 9,
        "title": "THE CONVEX MENISCUS",
        "tag": "SURFACE TENSION: 486.5 mN/m",
        "stat": "CONTACT ANGLE: θ = 140°",
        "text": "Its surface tension is nearly seven times stronger than water. Inside a glass tube, mercury pushes upward into a proud convex dome, fiercely repelling the glass walls. And when it touches solid gold, it greedily dissolves the gold into a silvery amalgam."
    },
    {
        "id": 10,
        "title": "EMPEROR QIN SHI HUANG",
        "tag": "CHINA, 210 BCE",
        "stat": "THE QUEST FOR IMMORTALITY",
        "text": "This bizarre metal drove ancient emperors mad with obsession. In the third century BCE, the first Emperor of unified China, Qin Shi Huang, became terrified of death. Taoist alchemists convinced him that drinking mercury would make him physically immortal."
    },
    {
        "id": 11,
        "title": "100 MERCURY RIVERS",
        "tag": "MAUSOLEUM AT LINTONG",
        "stat": "SOIL ANOMALY: 100x CONCENTRATION",
        "text": "Inside his gargantuan subterranean tomb, guarded by thousands of terracotta warriors, engineers constructed a vast miniature map of the empire, with one hundred mechanical rivers of pure flowing liquid mercury. Modern soil surveys confirm mercury levels one hundred times above normal."
    },
    {
        "id": 12,
        "title": "THE FATAL ELIXIR",
        "tag": "ACUTE MERCURY POISONING",
        "stat": "DIED AGE 49 AT SHAQIU",
        "text": "Ironically, his quest for eternity became his death sentence. After months of consuming mercury pills, Emperor Qin suffered severe neurological damage, organ failure, and paranoid hallucinations, dying in agony at age forty-nine."
    },
    {
        "id": 13,
        "title": "WESTERN ALCHEMY",
        "tag": "PARACELSUS TRIA PRIMA",
        "stat": "SULFUR • MERCURY • SALT",
        "text": "In medieval Europe, alchemists believed mercury was the key to the Philosopher's Stone. The physician Paracelsus declared mercury the spiritual fluid that bound all matter, spending lifetimes attempting to transmute base lead into gold through endless distillations."
    },
    {
        "id": 14,
        "title": "NEWTON'S SECRET LAB",
        "tag": "CAMBRIDGE, 1693",
        "stat": "HAIR FORENSICS: 197 ppm Hg",
        "text": "Even Sir Isaac Newton secretly spent decades boiling mercury in a dark laboratory. Modern forensic tests on Newton's preserved hair revealed mercury levels nearly forty times above normal, explaining his infamous nervous breakdown and severe paranoia in 1693."
    },
    {
        "id": 15,
        "title": "TORRICELLI'S BAROMETER",
        "tag": "FLORENCE, 1643",
        "stat": "760 mmHg = 101,325 Pa",
        "text": "In 1643, Galileo's disciple Evangelista Torricelli inverted a meter-long glass tube of mercury into a dish. The column settled at exactly seventy-six centimeters, creating the first artificial vacuum in history and proving that atmospheric air has measurable weight."
    },
    {
        "id": 16,
        "title": "THE INDUSTRIAL DAWN",
        "tag": "FAHRENHEIT, 1714",
        "stat": "PRECISION EXPANSION",
        "text": "In 1714, Daniel Gabriel Fahrenheit created the first modern precision thermometer using mercury's perfectly linear thermal expansion. Suddenly, medicine could diagnose fever, steam engines could be regulated, and the Industrial Revolution gained precise measurement."
    },
    {
        "id": 17,
        "title": "THE MAD HATTER",
        "tag": "19TH CENTURY FACTORIES",
        "stat": "ERETHISM MERCURIALIS",
        "text": "Yet mercury remained a silent predator. In nineteenth-century felt hat factories, workers cured beaver fur with steaming mercuric nitrate. The invisible toxic vapors destroyed their central nervous systems, causing trembling hands, delusions, and insanity: the real-life Mad Hatter."
    },
    {
        "id": 18,
        "title": "MINAMATA BAY DISASTER",
        "tag": "JAPAN, 1956",
        "stat": "BIOACCUMULATION: 10,000x",
        "text": "The worst tragedy occurred in Minamata Bay, Japan, where industrial chemical waste released methylmercury into coastal waters. Biomagnifying ten thousand times through the marine food chain into fish, it caused severe brain damage and gave birth to the global UN Minamata Convention."
    },
    {
        "id": 19,
        "title": "QUANTUM SUPERCONDUCTIVITY",
        "tag": "LEIDEN, 1911",
        "stat": "4.2 KELVIN (-269°C)",
        "text": "Yet mercury also opened the door to modern quantum physics. In 1911, physicist Heike Kamerlingh Onnes cooled liquid mercury with liquid helium to four point two Kelvin. Instantly, its electrical resistance dropped to absolute zero, discovering superconductivity."
    },
    {
        "id": 20,
        "title": "THE SPACE AGE & BEYOND",
        "tag": "NASA SERT-1, 1964",
        "stat": "EXHAUST VELOCITY: 30 km/s",
        "text": "In 1964, NASA launched SERT-One, humanity's first successful electrostatic ion rocket engine in space, propelled by ionized mercury vapor traveling at thirty kilometers per second. From an accidental campfire nine thousand years ago to deep space propulsion, mercury remains the most paradoxical element in human history."
    }
]

def main():
    print("=== SYNTHESIZING KOKORO 82M ENGLISH VOICEOVER ===")
    kokoro = kokoro_onnx.Kokoro(ONNX_MODEL, VOICES_BIN)
    
    scene_timings = []
    combined_samples = []
    sample_rate = 24000
    
    current_time = 0.0
    for sc in SCENES_SCRIPT:
        s_id = sc["id"]
        text = sc["text"]
        print(f"Synthesizing Scene {s_id:02d}: {sc['title']} ({len(text.split())} words)...")
        
        # Authoritative Vox documentary pacing (speed=0.98 for clarity and gravity)
        samples, sr = kokoro.create(text, voice="am_adam", speed=0.98, lang="en-us")
        dur_sec = len(samples) / sr
        
        # 0.8s pause between scenes
        pause_samples = [0.0] * int(sr * 0.8)
        
        start_sec = current_time
        end_sec = current_time + dur_sec
        start_frame = int(start_sec * 30)
        dur_frames = int(dur_sec * 30) + int(0.8 * 30)
        
        scene_timings.append({
            "id": s_id,
            "title": sc["title"],
            "tag": sc["tag"],
            "stat": sc["stat"],
            "text": text,
            "start_sec": round(start_sec, 2),
            "duration_sec": round(dur_sec, 2),
            "start_frame": start_frame,
            "duration_frames": dur_frames
        })
        
        combined_samples.extend(samples)
        combined_samples.extend(pause_samples)
        current_time += dur_sec + 0.8

    total_sec = len(combined_samples) / sample_rate
    total_frames = int(total_sec * 30)
    print(f"\n[SUMMARY] Total English Duration: {total_sec:.2f}s ({total_sec/60:.2f} minutes), {total_frames} frames @ 30fps")
    
    # Save WAV
    raw_wav = os.path.join(EXPORT_DIR, "kokoro_english_raw.wav")
    final_wav = os.path.join(EXPORT_DIR, "kokoro_english_48k.wav")
    remotion_wav = os.path.join(PUBLIC_DIR, "kokoro_english_48k.wav")
    
    sf.write(raw_wav, combined_samples, sample_rate)
    
    # Resample to 48kHz stereo using FFmpeg
    cmd = [
        FFMPEG, "-y",
        "-i", raw_wav,
        "-ar", "48000",
        "-ac", "2",
        final_wav
    ]
    subprocess.run(cmd, check=True)
    import shutil
    shutil.copy2(final_wav, remotion_wav)
    
    # Save timing manifest
    timing_file = os.path.join(EXPORT_DIR, "kokoro_scenes_manifest.json")
    remotion_timing = os.path.join(PUBLIC_DIR, "kokoro_scenes_manifest.json")
    manifest_data = {
        "voice": "Kokoro-82M (am_adam)",
        "total_sec": round(total_sec, 2),
        "total_frames": total_frames,
        "scenes": scene_timings
    }
    with open(timing_file, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)
    shutil.copy2(timing_file, remotion_timing)
    
    print(f"[OK] Audio & Timing manifest ready: {final_wav}")

if __name__ == "__main__":
    main()
