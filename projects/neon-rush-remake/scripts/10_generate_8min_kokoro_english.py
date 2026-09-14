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

# 28 Modular Scenes tailored for Kokoro 82M to fill 8+ minutes (480s - 510s)
SCENES_8MIN = [
    {
        "id": 1,
        "title": "THE PREHISTORIC DISCOVERY",
        "tag": "ÇATALHÖYÜK, 7000 BCE",
        "stat": "DAWN OF CIVILIZATION",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_01.png",
        "text": "Nine thousand years ago, deep inside the dark limestone caverns of ancient Anatolia, primitive hunters discovered something extraordinary. Embedded in the cold rugged rock walls were glistening veins of a brilliant, blood-red crystal that seemed to glow in the flickering torchlight."
    },
    {
        "id": 2,
        "title": "THE SACRED CINNABAR",
        "tag": "MINERAL: α-HgS",
        "stat": "MOHS HARDNESS: 2.0 – 2.5",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_02.png",
        "text": "This mysterious crimson rock was cinnabar, natural mercury sulfide. To stone-age humans, red was the sacred color of life, blood, and fire. They believed this strange stone held supernatural vitality bestowed directly by the subterranean gods."
    },
    {
        "id": 3,
        "title": "THE RITUAL POWDER",
        "tag": "VERMILION PIGMENT",
        "stat": "FUNERARY SKULL BURIALS",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_03.png",
        "text": "They ground the crimson crystals with stone mortars into an ultra-fine red powder called vermilion. Ancient shamans painted running beasts and ceremonial handprints onto cave walls, and dusted the bones of their ancestors to grant them eternal life."
    },
    {
        "id": 4,
        "title": "ALMADÉN: THE DEADLIEST MINES",
        "tag": "IBERIA, 2500 YEARS ACTIVE",
        "stat": "LARGEST CINNABAR DEPOSIT",
        "visual_type": "motion_graphic",
        "graphic_id": "almaden_mine",
        "text": "In the Iberian peninsula, the mines of Almadén contained the largest concentration of cinnabar on Earth. Thousands of years later, the Roman Empire would sentence enslaved criminals to these toxic tunnels, knowing the poison dust was an inescapable death sentence."
    },
    {
        "id": 5,
        "title": "THE CAMPFIRE ACCIDENT",
        "tag": "PRIMITIVE EXPERIMENT",
        "stat": "CAMPFIRE TEMP: > 500°C",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_03.png",
        "text": "Then came the accident that changed human history. One night, around a roaring campfire exceeding five hundred degrees Celsius, a curious caveman tossed a fist-sized lump of red cinnabar directly into the burning coals to see what would happen."
    },
    {
        "id": 6,
        "title": "THERMAL DISSOCIATION",
        "tag": "2HgS + 3O₂ → 2Hg + 2SO₂↑",
        "stat": "DISSOCIATION TEMP: 357°C",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_04.png",
        "text": "Within minutes, choking yellow fumes of sulfur dioxide filled the cave, stinging their eyes. The intense heat fractured the chemical bonds of the mineral, vaporizing pure metallic mercury that drifted upward toward the ceiling."
    },
    {
        "id": 7,
        "title": "THE LIVING SILVER",
        "tag": "CONDENSATION: Hg VAPOR",
        "stat": "MELTING POINT: -38.8°C",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_05.png",
        "text": "As the hot metallic vapor touched the cold cave rocks, it condensed instantly. The burning red rock appeared to bleed bright droplets of liquid silver. When the hunter touched it, it did not wet his fingers at all, rolling across the stone like living chrome."
    },
    {
        "id": 8,
        "title": "THE MIRROR BEADS",
        "tag": "SPECULAR REFLECTION",
        "stat": "ZERO WETTING ANGLE",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_06.png",
        "text": "Resting on the dark stone floor, the silvery beads fused together seamlessly without leaving a trace of moisture. Primitive humans were utterly terrified and mesmerized. They had just unlocked quicksilver: the living silver."
    },
    {
        "id": 9,
        "title": "ANOMALOUS DENSITY",
        "tag": "DENSITY: 13.53 g/cm³",
        "stat": "13.5x HEAVIER THAN WATER",
        "visual_type": "motion_graphic",
        "graphic_id": "density_tank",
        "text": "Mercury is the only metal on the periodic table that remains liquid at room temperature. But its most shocking property is its sheer density: thirteen point five grams per cubic centimeter. A simple gallon jug of mercury weighs over one hundred and ten pounds."
    },
    {
        "id": 10,
        "title": "IRON FLOATS EFFORTLESSLY",
        "tag": "HYDROSTATIC BUOYANCY",
        "stat": "41.8% VOLUME ABOVE SURFACE",
        "visual_type": "motion_graphic",
        "graphic_id": "buoyancy_iron",
        "text": "Because mercury is far denser than most solid metals, a heavy solid cast-iron cannonball dropped into a vat of quicksilver will not sink. It bobs and floats effortlessly on the silvery surface like styrofoam on water, defying human intuition."
    },
    {
        "id": 11,
        "title": "THE CONVEX MENISCUS",
        "tag": "SURFACE TENSION: 486.5 mN/m",
        "stat": "CONTACT ANGLE: θ = 140°",
        "visual_type": "motion_graphic",
        "graphic_id": "meniscus_angle",
        "text": "Its surface tension is nearly seven times stronger than water. Inside a glass tube, mercury pushes upward into a proud convex dome, fiercely repelling the glass walls. Its cohesive atomic forces completely overpower adhesive forces."
    },
    {
        "id": 12,
        "title": "THE GOLD AMALGAMATION",
        "tag": "METALLIC DISSOLUTION",
        "stat": "AMALGAM REACTION: Au-Hg",
        "visual_type": "motion_graphic",
        "graphic_id": "gold_amalgam",
        "text": "Even more terrifying is amalgamation. When a solid pure gold ring touches liquid mercury, the silver fluid creeps upward, breaking down the crystalline lattice of the gold and devouring it into a silvery amalgamated paste within minutes."
    },
    {
        "id": 13,
        "title": "THE SPANISH SILVER EMPIRE",
        "tag": "POTOSÍ, BOLIVIA (1572)",
        "stat": "PATIO AMALGAMATION PROCESS",
        "visual_type": "motion_graphic",
        "graphic_id": "potosi_empire",
        "text": "This property changed world geopolitics. In the sixteenth century, the Spanish Empire used thousands of tons of mercury to extract silver from Potosí Bolivia. The quicksilver fueled the global silver trade, financing European wars at the cost of countless indigenous lives."
    },
    {
        "id": 14,
        "title": "EMPEROR QIN SHI HUANG",
        "tag": "CHINA, 210 BCE",
        "stat": "THE QUEST FOR IMMORTALITY",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_08.png",
        "text": "In ancient Asia, this miraculous liquid drove kings into madness. The First Emperor of unified China, Qin Shi Huang, conquered six warring states but was terrified of death. Taoist alchemists convinced him that drinking mercury was the divine secret to immortality."
    },
    {
        "id": 15,
        "title": "100 MERCURY RIVERS",
        "tag": "MAUSOLEUM AT LINTONG",
        "stat": "SOIL ANOMALY: 100x CONCENTRATION",
        "visual_type": "motion_graphic",
        "graphic_id": "qin_tomb_map",
        "text": "Beneath a colossal pyramid guarded by the Terracotta Army, builders constructed an underground miniature cosmos. Over one hundred mechanical rivers of pure flowing mercury traced the Yangtze and Yellow rivers. Modern soil tests confirm mercury vapor levels a hundred times above background."
    },
    {
        "id": 16,
        "title": "THE FATAL ELIXIR",
        "tag": "ACUTE MERCURY TOXICITY",
        "stat": "DIED AGE 49 AT SHAQIU",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_08.png",
        "text": "His quest for eternal life proved fatal. Consuming red cinnabar and mercury pills, the Emperor suffered severe brain damage, progressive tremors, and paranoid delusions. At age forty-nine, the conqueror of China died poisoned by the very metal he worshiped."
    },
    {
        "id": 17,
        "title": "WESTERN ALCHEMY",
        "tag": "PARACELSUS TRIA PRIMA",
        "stat": "SULFUR • MERCURY • SALT",
        "visual_type": "img",
        "visual_src": "assets/scenes_8min/scene_07.png",
        "text": "In medieval Europe, mercury was the sacred heart of alchemy. The Swiss physician Paracelsus declared mercury one of the three prime components of the universe, representing volatility and spirit. Alchemists spent centuries distilling quicksilver to synthesize the Philosopher's Stone."
    },
    {
        "id": 18,
        "title": "NEWTON'S SECRET LAB",
        "tag": "CAMBRIDGE, 1693",
        "stat": "HAIR FORENSICS: 197 ppm Hg",
        "visual_type": "motion_graphic",
        "graphic_id": "newton_lab",
        "text": "Even Sir Isaac Newton was secretly consumed by alchemy, writing over a million words on mercury transmutation in a dark Cambridge laboratory. In 1979, forensic tests on Newton's preserved hair revealed nearly forty times normal mercury levels, explaining his severe nervous breakdown."
    },
    {
        "id": 19,
        "title": "TORRICELLI'S BAROMETER",
        "tag": "FLORENCE, 1643",
        "stat": "760 mmHg = 101,325 Pa",
        "visual_type": "motion_graphic",
        "graphic_id": "torricelli_barometer",
        "text": "By 1643, mercury stepped from mysticism into empirical science. Galileo's student Evangelista Torricelli inverted a meter-long tube of mercury into a basin. The column stopped at exactly seventy-six centimeters, proving atmospheric pressure and creating the first artificial vacuum in history."
    },
    {
        "id": 20,
        "title": "THE PRECISION THERMOMETER",
        "tag": "FAHRENHEIT, 1714",
        "stat": "EXPANSION β = 1.81×10⁻⁴",
        "visual_type": "motion_graphic",
        "graphic_id": "fahrenheit_gauge",
        "text": "In 1714, Daniel Gabriel Fahrenheit harnessed mercury's perfectly linear thermal expansion to craft the first precision glass thermometer. For the first time, physicians could measure fever, engineers could regulate steam engines, and modern meteorology was born."
    },
    {
        "id": 21,
        "title": "MURANO MIRROR GUILDS",
        "tag": "VENICE, 17TH CENTURY",
        "stat": "TIN-MERCURY AMALGAM",
        "visual_type": "motion_graphic",
        "graphic_id": "venetian_mirror",
        "text": "In Venice, master craftsmen spread tin-mercury amalgams onto flat plate glass, inventing the first distortion-free mirrors. These dazzling luxury mirrors transformed European architecture and portraiture, though the toxic vapors claimed the lives of countless artisans."
    },
    {
        "id": 22,
        "title": "THE MAD HATTER",
        "tag": "19TH CENTURY FACTORIES",
        "stat": "ERETHISM MERCURIALIS",
        "visual_type": "motion_graphic",
        "graphic_id": "mad_hatter_syndrome",
        "text": "The industrial curse peaked in Victorian felt hat workshops. Workers used hot mercuric nitrate to soften rabbit fur. The invisible fumes caused tremors, emotional outbursts, and memory loss: a medical condition known as erethism, immortalized in Alice in Wonderland."
    },
    {
        "id": 23,
        "title": "MINAMATA BAY DISASTER",
        "tag": "JAPAN, 1956",
        "stat": "METHYLMERCURY (CH₃Hg⁺)",
        "visual_type": "motion_graphic",
        "graphic_id": "minamata_bioaccumulation",
        "text": "The twentieth century witnessed the darkest disaster in Minamata Bay, Japan. A chemical plant discharged methylmercury into the sea for decades. Concentrating ten thousand times through the marine food chain, the toxic fish caused permanent neurological paralysis across entire generations."
    },
    {
        "id": 24,
        "title": "THE MINAMATA CONVENTION",
        "tag": "UNEP TREATY, 2013",
        "stat": "GLOBAL MERCURY PHASEOUT",
        "visual_type": "motion_graphic",
        "graphic_id": "un_convention",
        "text": "This tragedy forced humanity to take global action. In 2013, over one hundred and forty nations signed the United Nations Minamata Convention on Mercury, strictly banning mercury in consumer goods, medical devices, and industrial mining worldwide."
    },
    {
        "id": 25,
        "title": "QUANTUM SUPERCONDUCTIVITY",
        "tag": "LEIDEN, APRIL 8, 1911",
        "stat": "4.2 KELVIN (-269°C)",
        "visual_type": "motion_graphic",
        "graphic_id": "superconductivity_meter",
        "text": "Yet mercury also opened the door to quantum mechanics. On April eighth, 1911, Dutch physicist Heike Kamerlingh Onnes cooled liquid mercury with liquid helium down to four point two Kelvin. Instantly, its electrical resistance dropped to absolute zero, discovering superconductivity."
    },
    {
        "id": 26,
        "title": "NASA SERT-1 ION ENGINE",
        "tag": "SPACE TEST, JULY 1964",
        "stat": "EXHAUST VELOCITY: 30 km/s",
        "visual_type": "motion_graphic",
        "graphic_id": "nasa_sert_engine",
        "text": "In 1964, NASA launched SERT-One into orbit: humanity's first successful electrostatic ion rocket engine in space. By vaporizing and ionizing heavy mercury atoms, the engine expelled an electric blue exhaust plume at thirty kilometers per second, pioneering deep space propulsion."
    },
    {
        "id": 27,
        "title": "THE QUANTUM LIQUID METAL",
        "tag": "RELATIVISTIC 6s² ORBITAL",
        "stat": "DIRAC EQUATION PHYSICS",
        "visual_type": "motion_graphic",
        "graphic_id": "quantum_dirac",
        "text": "Modern quantum electrodynamics finally solved the riddle of quicksilver. Because of Einstein's special relativity, inner electrons move near sixty percent lightspeed, contracting the outer valence shell. This prevents mercury atoms from binding tightly, keeping it liquid at room temperature."
    },
    {
        "id": 28,
        "title": "THE PARADOXICAL ELEMENT",
        "tag": "FROM CAVE TO COSMOS",
        "stat": "HYDRARGYRUM 80",
        "visual_type": "motion_graphic",
        "graphic_id": "cosmic_epilogue",
        "text": "From a crimson rock thrown into a stone-age campfire nine thousand years ago, to alchemical obsessions, imperial tombs, and electric ion thrusters orbiting the stars: mercury has mirrored the trajectory of human civilization. It is the most beautiful, deadly, and paradoxical element on Earth."
    }
]

def main():
    print(f"=== SYNTHESIZING FULL 8-MINUTE KOKORO 82M ENGLISH VOICEOVER ({len(SCENES_8MIN)} SCENES) ===")
    kokoro = kokoro_onnx.Kokoro(ONNX_MODEL, VOICES_BIN)
    
    scene_timings = []
    combined_samples = []
    sample_rate = 24000
    
    current_time = 0.0
    for sc in SCENES_8MIN:
        s_id = sc["id"]
        text = sc["text"]
        print(f"Synthesizing [{s_id:02d}/28] {sc['title']} ({len(text.split())} words)...")
        
        # Paced Vox style narration (speed=0.96 for clear, deep resonance)
        samples, sr = kokoro.create(text, voice="am_adam", speed=0.96, lang="en-us")
        dur_sec = len(samples) / sr
        
        # 1.0s clean pause between scenes
        pause_samples = [0.0] * int(sr * 1.0)
        
        start_sec = current_time
        end_sec = current_time + dur_sec
        start_frame = int(start_sec * 30)
        dur_frames = int(dur_sec * 30) + int(1.0 * 30)
        
        scene_timings.append({
            "id": s_id,
            "title": sc["title"],
            "tag": sc["tag"],
            "stat": sc["stat"],
            "text": text,
            "visual_type": sc["visual_type"],
            "visual_src": sc.get("visual_src", ""),
            "graphic_id": sc.get("graphic_id", ""),
            "start_sec": round(start_sec, 2),
            "duration_sec": round(dur_sec, 2),
            "start_frame": start_frame,
            "duration_frames": dur_frames
        })
        
        combined_samples.extend(samples)
        combined_samples.extend(pause_samples)
        current_time += dur_sec + 1.0

    total_sec = len(combined_samples) / sample_rate
    total_frames = int(total_sec * 30)
    minutes = total_sec / 60.0
    print(f"\n[SUMMARY] Total English Duration: {total_sec:.2f}s ({minutes:.2f} minutes), {total_frames} frames @ 30fps")
    
    # Save WAV
    raw_wav = os.path.join(EXPORT_DIR, "kokoro_english_8min_raw.wav")
    final_wav = os.path.join(EXPORT_DIR, "kokoro_english_8min_48k.wav")
    remotion_wav = os.path.join(PUBLIC_DIR, "kokoro_english_8min_48k.wav")
    
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
    timing_file = os.path.join(EXPORT_DIR, "kokoro_8min_manifest.json")
    remotion_timing = os.path.join(PUBLIC_DIR, "kokoro_8min_manifest.json")
    manifest_data = {
        "voice": "Kokoro-82M (am_adam)",
        "total_sec": round(total_sec, 2),
        "minutes": round(minutes, 2),
        "total_frames": total_frames,
        "scenes": scene_timings
    }
    with open(timing_file, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)
    shutil.copy2(timing_file, remotion_timing)
    
    print(f"[OK] Full 8-Minute English Audio & Manifest ready: {final_wav}")

if __name__ == "__main__":
    main()
