# AG-Stick: Animated Stickman Science & History Documentaries 🧪✨

> An enterprise-grade AI automated animation & video production pipeline inspired by the viral visual style of **Neon Rush** (`@Neon-Rush-3D`), engineered with **Remotion (React)**, **Kokoro 82M English TTS**, and **9Router Codex Image Generation**.

---

## 🎬 Featured Project: The 9,000-Year Curse of Quicksilver (Mercury)

A complete 8-minute 14-second Full HD (1080p @ 30fps) animated science & history documentary covering **Element 80 (Hydrargyrum / Mercury)** across 28 fully customized 2D stickman scenes:

* **Format**: 16:9 Widescreen (1920x1080)
* **Duration**: 8 minutes 14 seconds (14,833 frames)
* **Visual Style**: 2D Cartoon Stickman with bold black ink outlines, expressive cartoon eyes, saturated colors, and high-CTR neon yellow typography (`#FFE600`).
* **Audio Track**: Kokoro 82M English voiceover (`am_adam`) synchronized to timeline, broadcast mixed at `-16 LUFS` with cinematic sound design.
* **Telemetry**: Titanium glassmorphic HUD showing active era, element metrics, and running timecode.

---

## 📁 Repository Structure

```
AG-Stick/
├── projects/
│   ├── neon-rush-remake/
│   │   ├── branding/                  # PFP Avatar, 2560x1440 Banner, 3 High-CTR Thumbnails
│   │   ├── scenes_neon_rush/          # 28 Custom 2D cartoon stickman scene illustrations
│   │   ├── scripts/                   # Production automation scripts (01 to 17)
│   │   ├── CHANNEL_BRANDING_GUIDE.md  # Channel naming, handles, bio & CTR strategy
│   │   ├── YOUTUBE_METADATA.md        # Titles, 28-chapter timestamps, tags & pinned comment
│   │   └── export/                    # Render output directory (ignored by git)
│   ├── wework-47-billion-illusion/
│   │   └── remotion/                  # Remotion React video composition engine
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
