# Neon Atom Production Rules — Visual & Motion Graphics Standards
## Episode: The Man Who Accidentally Poisoned the Entire Planet (Thomas Midgley Jr. / Lead & CFC)

### 🚫 1. Critical Directive: ZERO AI Typography on Images (Strict Anti-Slop)
Strictly enforced across all 32 scenes:
1. **NO Text in AI Prompts**:
   - **NEVER** instruct the image generator (9Router / `cx/gpt-5.5-image`) to render text, numbers, chemical equations, comic callouts, banners, titles, or words inside the artwork (e.g., NO *"ETHYL"*, NO *"LEAD GAS"*, NO *"FREON"*, NO *"OZONE HOLE"*, NO *"Pb(C2H5)4"*).
   - AI typography produces distorted glyphs, looks amateurish, and collides with dynamic Remotion HUD overlays, badges, and timecodes.
2. **100% Programmatic Typography in Remotion**:
   - All headlines, kinetic hooks, chapter titles, statistics, badges, telemetry monitors, and chemical cards must be rendered dynamically in **Remotion React components**.
   - Use clean modern typography (`Inter`, `Montserrat`, `JetBrains Mono`), crisp CSS drop-shadows, glassmorphism containers, and programmatic entry/exit spring animations.

---

### 🎨 2. Character Consistency (Minimalist 2D Stickman Only)
- Main character (Thomas Midgley Jr.) and supporting scientists/workers must be **minimalist 2D cartoon stick figures**:
  - Garis outline hitam tebal bersih (vector stroke 8–10px).
  - Kepala bulat polos putih solid (`#ffffff`).
  - Mata ekspresif sederhana (titik/busur kartun), ekspresi penasaran/panik/bangga yang jelas.
  - Anggota badan garis stik hitam sederhana.
  - Midgley's Attire: Kemeja berkerah era 1920-an, dasi kupu-kupu atau dasi panjang vintage, kacamata bundar retro hitam (`spectacles`), dan jas lab putih saat di laboratorium.
- **Framing**: Centered cinematic composition (subjek di 1/3 tengah atau rule-of-thirds seimbang, tidak terpotong tepi).
- **Negative Constraints**: NO 3D shading, NO CGI rendering, NO photorealism, NO anime face/hair, NO realistic human skin/anatomy.

---

### 🏛️ 3. Environment & Aesthetic Tone
- **Era & Settings**:
  - 1921 Dayton, Ohio GM / Delco Research Lab (brass pipes, antique car engines, glass retorts).
  - 1924 Deep River / Bayway, New Jersey TEL Refinery (industrial smoke, chemical vats, hazardous vapors).
  - 1928 Frigidaire laboratory (vintage electric refrigerator compressors, condensation, frost).
  - 1974–1985 Stratospheric atmosphere & Antarctic research stations (deep ultraviolet blue sky, solar radiation rays, ice sheets).
- **Palette**:
  - Industrial Amber (`#F59E0B`), Toxic Hazard Emerald (`#10B981` / `#059669`), Blood Lead Crimson (`#EF4444`), Ozone Ultraviolet Cyan & Violet (`#06B6D4` / `#8B5CF6`), Dark Slate Charcoal background (`#0B0F19`, `#0F172A`).
- **Aspect Ratio**: 16:9 Widescreen (`1672x941` via 9Router, `1920x1080` in Remotion).

---

### 🎙️ 4. Audio & Narration Standards
- **Voice Engine**: Kokoro 82M TTS broadcast quality (`am_adam` @ 1.05x speed).
- **Loudness**: EBU R128 (-16.0 LUFS ± 0.5 LUFS), True Peak limit: -1.0 dBFS.
- **Pacing**: ~150-160 WPM documentary cadence with 0.4s breathing pause between scenes.
