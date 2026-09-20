# AG-Stick: Animated Stickman Science & History Documentaries 🧪✨

> An enterprise-grade AI automated animation & video production pipeline inspired by the viral visual style of **Neon Rush** (`@Neon-Rush-3D`), engineered with **Remotion (React)**, **Kokoro 82M English TTS**, and **9Router Codex Image Generation**.

---

## 🎬 Featured Projects

### 1. The 9,000-Year Curse of Quicksilver (Mercury)
* **Format**: 16:9 Widescreen (1920x1080)
* **Duration**: 8 minutes 14 seconds (14,833 frames)
* **Visual Style**: 2D Cartoon Stickman with bold black ink outlines, expressive cartoon eyes, saturated colors, and high-CTR neon yellow typography (`#FFE600`).
* **Audio Track**: Kokoro 82M English voiceover (`am_adam`) synchronized to timeline, broadcast mixed at `-16 LUFS`.

### 2. The Man Who Accidentally Poisoned the Entire Planet (Thomas Midgley Jr.)
* **Format**: 16:9 Widescreen (1920x1080 Full HD @ 30fps)
* **Duration**: 9 minutes 43 seconds (17,507 frames)
* **Visual Style**: Strict Anti-Slop 2D Cartoon Stickman (Zero AI typography on artwork, 100% programmatic kinetic typography in Remotion, 32 custom scenes, smooth 15-frame crossfades, Toxic Emerald & UV Ozone bursts).
* **Audio Track**: Kokoro 82M English voiceover (`am_adam`) synchronized with 0.4s breathing pauses, EBU R128 (-16.0 LUFS) master mix.
* **Telemetry**: Live blood lead concentration ($\mu g/dL$), ozone integrity ($DU$), and molecular structure cards ($Pb(C_2H_5)_4$, $CCl_2F_2$, $Cl + O_3 \to ClO + O_2$).

---

## 📁 Repository Structure

```
AG-Stick/
├── projects/
│   ├── thomas-midgley-planet-poison/  # Complete 10-min documentary pipeline
│   │   ├── PRODUCTION_RULES.md        # Strict Zero-AI-Text & character consistency rules
│   │   ├── script/                    # 32-scene script & synchronized manifest
│   │   ├── scripts/                   # Automation scripts (01 audio, 02 9router art, 03 thumbs, 04 master render)
│   │   ├── assets/scenes/             # 32 custom 2D stickman scenes
│   │   ├── thumbnails/                # 3 High-CTR viral thumbnails
│   │   └── packaging/                 # YouTube titles, 32-chapter timestamps, tags & pinned comment
│   ├── demon-core-10min/              # The Demon Core documentary
│   ├── white-phosphorus-10min/        # The Devil's Element documentary
│   ├── neon-rush-remake/              # Quicksilver Mercury documentary
│   ├── wework-47-billion-illusion/
│   │   └── remotion/                  # Master Remotion React composition engine
│   │       ├── src/midgley/           # ThomasMidgley10MinComposition.tsx
│   │       ├── src/demoncore/         # DemonCoreV2Composition.tsx
│   │       ├── src/mercury/           # MercuryEnglish8MinComposition.tsx
│   │       └── public/assets/         # Static assets and Kokoro manifests
│   └── neon_rush_analysis/            # Channel benchmarking & style reverse-engineering
└── README.md
```

---

## 🚀 Key Production Scripts

All scripts are located in [`projects/neon-rush-remake/scripts/`](projects/neon-rush-remake/scripts/):

1. **`15_generate_all_28_neon_rush_style.py`**: Batch generates all 28 custom 2D stickman scenes using 9Router Codex (`cx/gpt-5.5-image`).
2. **`16_render_level_1_review.py`**: Fast renderer for Act 1 / Level 1 clips for quality inspection.
3. **`13_render_english_8min_master.py`**: Renders all 14,833 frames of `MercuryEnglish8Min` and multiplexes with broadcast audio.
4. **`17_generate_channel_branding_and_thumbs.py`**: Generates high-CTR thumbnail variants, profile picture avatar, and channel banner.

---

## 🏷️ Channel Branding

* **Recommended Name**: **Neon Atom** (`@NeonAtomTV`)
* **Tagline**: *"Weird Science. Untold History. Pure Chemistry."*
* **Profile Picture**: Electric cyan atomic ring stickman mascot with bubbling mercury flask.
* **Banner**: 2560x1440 panoramic evolution from stone age fire to interstellar ion propulsion.

---

## 🛠️ Tech Stack

* **Video Engine**: [Remotion](https://remotion.dev) (React + TypeScript)
* **Voice Synthesis**: Kokoro 82M (`am_adam`)
* **Visual Synthesis**: 9Router Codex (`cx/gpt-5.5-image`)
* **Audio Engineering**: Python SoundFile, SciPy, Pyloudnorm (-16 LUFS)
* **Video Multiplexing**: FFmpeg (H.264 High Profile, AAC 320k 48kHz)
