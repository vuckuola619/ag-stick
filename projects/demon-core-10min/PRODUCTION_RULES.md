# Neon Atom Production Rules — Visual & Motion Graphics Standards
## Episode 3: The Demon Core: How a Flathead Screwdriver Almost Blew Up Los Alamos

### 🚫 1. Critical Directive: ZERO AI Typography on Images (Strict Anti-Slop)
Starting immediately and strictly enforced across all 32 scenes:
1. **NO Text in AI Prompts**:
   - **NEVER** instruct the image generator (9Router / `cx/gpt-5.5-image`) to render text, numbers, equations, comic callouts, banners, titles, or words inside the artwork (e.g., NO *"DEMON CORE"*, NO *"510 REMS"*, NO *"DANGER!"*, NO *"k = 1.0"*).
   - AI typography looks generic ("AI slop"), produces garbled glyphs, and collides with Remotion HUD overlays, badges, and timecodes.
2. **100% Programmatic Typography in Remotion**:
   - All headlines, kinetic hooks, chapter titles, statistics, badges, dosimeter counters, and subtitles must be rendered dynamically in **Remotion React components**.
   - Use clean modern typography (`Inter`, `Montserrat`, `JetBrains Mono`), crisp CSS shadows, glassmorphism containers, and programmatic entry/exit spring animations.

---

### 🎨 2. Character Consistency (Minimalist 2D Stickman Only)
- Karakter utama dan semua figuran wajib berupa **kartun stick figure 2D minimalis**:
  - Garis outline hitam tebal bersih (vector stroke 8–10px).
  - Kepala bulat polos putih solid (`#ffffff`).
  - Mata ekspresif sederhana (titik/busur kartun), tanpa hidung/mulut kecuali saat ekspresi ekstrem.
  - Anggota badan garis stik hitam sederhana.
  - Pakaian era 1945–1946: Kemeja kantor lengan pendek/panjang, dasi, jas lab putih, kacamata horn-rimmed retro, atau seragam militer US Army Manhattan Project.
- **CENTERING**: Semua karakter utama harus berada di center frame (komposisi seimbang, tidak terpotong tepi).
- **NEGATIVE CONSTRAINTS**: NO 3D shading, NO CGI rendering, NO photorealism, NO anime face/hair, NO realistic human skin/anatomy.

---

### 🏛️ 3. Environment & Aesthetic Tone
- **Setting**: Los Alamos Omega Site (laboratorium kayu/beton New Mexico tahun 1945–1946, gurun, instrumen analog, tabung Geiger, dosimeter).
- **Key Elements**: Bola Plutonium 14 pon (6.2 kg) perak mengkilap, kubah berilium setengah lingkaran (reflector), balok tungsten karbida, obeng minus pipih (flathead screwdriver), dan efek kilatan biru radiasi ionisasi (Cherenkov radiation blue glow).
- **Palette**: Dark slate charcoal backgrounds (`#12141A`, `#161922`), vibrant hazard orange (`#FF5500`), electric blue radiation cyan (`#00E5FF` / `#0088FF`), warning amber (`#FFB300`).
- **Aspect Ratio**: 16:9 Widescreen (`1672x941` via 9Router, `1920x1080` in Remotion).

---

### 🎙️ 4. Audio & Narration Standards
- **Voice Engine**: Kokoro 82M TTS broadcast quality (`am_adam` or `am_michael` @ 1.05x speed).
- **Loudness**: EBU R128 (-16.0 LUFS ± 0.5 LUFS), True Peak limit: -1.0 dBFS.
- **Pacing**: ~150-160 WPM documentary cadence with 0.4s breathing pause between scenes.
