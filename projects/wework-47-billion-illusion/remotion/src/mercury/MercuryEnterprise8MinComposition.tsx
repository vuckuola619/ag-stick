import React from 'react';
import {
  useCurrentFrame,
  interpolate,
  spring,
  useVideoConfig,
  Img,
  staticFile,
} from 'remotion';

import timestampsData from '../../public/assets/sentence_timestamps_8min.json';
import chaptersData from '../../public/assets/chapters_8min.json';

interface SentenceItem {
  start_sec: number;
  duration_sec: number;
  start_frame: number;
  duration_frames: number;
  text: string;
}

interface ChapterItem {
  title: string;
  sentence_idx: number;
  start_sec: number;
  start_frame: number;
}

const SENTENCES: SentenceItem[] = timestampsData.sentences;
const CHAPTERS: ChapterItem[] = chaptersData;

// Chapter metadata: visual styling & themes
const CHAPTER_THEMES: Record<number, {
  accent: string;
  subAccent: string;
  badge: string;
  era: string;
  temp: string;
  diagramTitle: string;
}> = {
  0: { accent: '#ef4444', subAccent: '#f59e0b', badge: 'ARCHAEOMETRY', era: '7000 BCE — ÇATALHÖYÜK', temp: '18°C', diagramTitle: 'ELEMENT PROFILE: HYDRARGYRUM (Hg-80)' },
  1: { accent: '#f97316', subAccent: '#fbbf24', badge: 'THERMAL BREAKDOWN', era: 'PRIMITIVE SMELTING', temp: '> 500°C', diagramTitle: 'THERMAL DECOMPOSITION: 2HgS + 3O₂ → 2Hg + 2SO₂' },
  2: { accent: '#06b6d4', subAccent: '#38bdf8', badge: 'ANOMALOUS PHYSICS', era: 'QUANTUM MECHANICS', temp: '20°C (ROOM TEMP)', diagramTitle: 'HYDROSTATIC DENSITY & MENISCUS DYNAMICS' },
  3: { accent: '#eab308', subAccent: '#dc2626', badge: 'IMPERIAL OBSESSION', era: '210 BCE — QIN MAUSOLEUM', temp: '14°C', diagramTitle: 'SUBTERRANEAN 100 MERCURY RIVERS TACTICAL MAP' },
  4: { accent: '#10b981', subAccent: '#6366f1', badge: 'WESTERN ALCHEMY', era: '1680 CE — TRIA PRIMA', temp: '357°C (DISTILL)', diagramTitle: 'ALCHEMICAL TRIA PRIMA & NEWTON MANUSCRIPT' },
  5: { accent: '#3b82f6', subAccent: '#60a5fa', badge: 'SCIENTIFIC REVOLUTION', era: '1643 CE — FLORENCE & 1714 CE', temp: 'CALIBRATION', diagramTitle: 'TORRICELLI VACUUM (760 mmHg) & FAHRENHEIT SCALE' },
  6: { accent: '#a855f7', subAccent: '#ec4899', badge: 'TOXICOLOGY EPIDEMIC', era: '1956 CE — MINAMATA TRAGEDY', temp: '16°C', diagramTitle: 'TROPHIC BIOACCUMULATION & SENSORY NEUROPATHY' },
  7: { accent: '#38bdf8', subAccent: '#f8fafc', badge: 'SPACE & QUANTUM DAWN', era: '1964 CE — NASA SERT-1 & FUTURE', temp: '4.2 K (-269°C)', diagramTitle: 'NASA ION PROPULSION & QUANTUM SUPERCONDUCTIVITY' },
};

// 18 Visual Sequences mapped across 23,359 frames (~13 min)
const VISUAL_SEQUENCES = [
  { id: 1, img: 'assets/scenes_8min/scene_01.png', start: 0, dur: 1400, caption: 'Penemuan bongkahan mineral Sinabar di dinding gua gelap zaman purba' },
  { id: 2, img: 'assets/scenes_8min/scene_02.png', start: 1400, dur: 1416, caption: 'Inspeksi kristal merah delima yang memantulkan kilauan torchlight' },
  { id: 3, img: 'assets/scenes_8min/scene_03.png', start: 2816, dur: 1500, caption: 'Pembuatan bubuk vermilion sakral untuk ritual manusia gua' },
  { id: 4, img: 'assets/scenes_8min/scene_04.png', start: 4316, dur: 1518, caption: 'Batu sinabar dipanggang di bara api unggun di atas 500 derajat Celsius' },
  { id: 5, img: 'assets/scenes_8min/scene_05.png', start: 5834, dur: 1600, caption: 'Batu mulai berdarah cairan perak murni yang menetes ke batu ceper' },
  { id: 6, img: 'assets/scenes_8min/scene_06.png', start: 7434, dur: 1686, caption: 'Tetesan merkuri memantul licin tanpa membasahi permukaan batu' },
  { id: 7, img: 'assets/scenes_8min/scene_06.png', start: 9120, dur: 1400, caption: 'Bola besi seberat kilogram mengapung santai di atas danau air raksa' },
  { id: 8, img: 'assets/scenes_8min/scene_08.png', start: 10520, dur: 1501, caption: 'Mausoleum kolosal Kaisar Qin Shi Huang dengan 100 sungai merkuri mekanis' },
  { id: 9, img: 'assets/scenes_8min/scene_07.png', start: 12021, dur: 1250, caption: 'Distilasi alkimia abad pertengahan dalam labu kaca alembik' },
  { id: 10, img: 'assets/scenes_8min/scene_07.png', start: 13271, dur: 1258, caption: 'Eksperimen rahasia Sir Isaac Newton dengan uap air raksa di Cambridge' },
  { id: 11, img: 'assets/scenes_8min/scene_08.png', start: 14529, dur: 1400, caption: 'Evangelista Torricelli menciptakan barometer dan membuktikan ruang hampa udara' },
  { id: 12, img: 'assets/scenes_8min/scene_08.png', start: 15929, dur: 1421, caption: 'Daniel Gabriel Fahrenheit menciptakan termometer merkuri modern pertama' },
  { id: 13, img: 'assets/scenes_8min/scene_05.png', start: 17350, dur: 1600, caption: 'Sindrom Mad as a Hatter pada industri topi wol abad ke-19' },
  { id: 14, img: 'assets/scenes_8min/scene_01.png', start: 18950, dur: 1595, caption: 'Tragedi metilmerkuri di Teluk Minamata & Konvensi PBB 2013' },
  { id: 15, img: 'assets/scenes_8min/scene_06.png', start: 20545, dur: 1400, caption: 'Penemuan superkonduktivitas pada 4.2 Kelvin oleh Kamerlingh Onnes' },
  { id: 16, img: 'assets/scenes_8min/scene_08.png', start: 21945, dur: 1414, caption: 'Misi NASA SERT-1 dengan pendorong ion merkuri melintasi orbit bumi' }
];

export const MercuryEnterprise8MinComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  // Active Chapter Detection
  let currentChapterIdx = 0;
  for (let i = 0; i < CHAPTERS.length; i++) {
    if (frame >= CHAPTERS[i].start_frame) {
      currentChapterIdx = i;
    }
  }
  const currentChapter = CHAPTERS[currentChapterIdx];
  const theme = CHAPTER_THEMES[currentChapterIdx] || CHAPTER_THEMES[0];

  // Chapter Relative Frame & Transition
  const chapterRelativeFrame = frame - currentChapter.start_frame;
  const isChapterTitleVisible = chapterRelativeFrame >= 0 && chapterRelativeFrame < 150; // 5 seconds intro card
  const titleCardOpacity = interpolate(
    chapterRelativeFrame,
    [0, 15, 120, 150],
    [0, 1, 1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );
  const titleCardScale = interpolate(
    chapterRelativeFrame,
    [0, 15, 150],
    [0.96, 1.0, 1.03],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // Active Visual Sequence
  const activeSeq = VISUAL_SEQUENCES.find(
    (s) => frame >= s.start && frame < s.start + s.dur
  ) || VISUAL_SEQUENCES[VISUAL_SEQUENCES.length - 1];

  const seqRelativeFrame = frame - activeSeq.start;

  // Cinematic Ken Burns Multi-Axis Camera Pan & Zoom
  const kbZoom = interpolate(
    seqRelativeFrame,
    [0, activeSeq.dur],
    [1.0, 1.09],
    { extrapolateRight: 'clamp' }
  );
  const kbPanX = Math.sin((frame + activeSeq.id * 100) / 75) * 16;
  const kbPanY = Math.cos((frame + activeSeq.id * 100) / 90) * 10;
  const kbRot = Math.sin(frame / 120) * 0.25;

  // Active Subtitle Detection
  const activeSentence = SENTENCES.find(
    (s) => frame >= s.start_frame && frame < s.start_frame + s.duration_frames
  );

  // Timecode formatting
  const totalSec = frame / fps;
  const tcH = Math.floor(totalSec / 3600);
  const tcM = Math.floor((totalSec % 3600) / 60);
  const tcS = Math.floor(totalSec % 60);
  const tcF = frame % fps;
  const timecode = `${String(tcH).padStart(2, '0')}:${String(tcM).padStart(2, '0')}:${String(tcS).padStart(2, '0')}:${String(tcF).padStart(2, '0')}`;

  // Atmospheric ambient volumetric spotlight pulsation
  const spotPulse1 = 0.55 + 0.15 * Math.sin(frame / 45);
  const spotPulse2 = 0.45 + 0.12 * Math.cos(frame / 60);

  // Progress Bar percentage (0 to 100)
  const totalCompositionFrames = 23359;
  const progressPercent = Math.min(100, (frame / totalCompositionFrames) * 100);

  return (
    <div
      style={{
        position: 'relative',
        width: 1920,
        height: 1080,
        backgroundColor: '#050811',
        overflow: 'hidden',
        fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        color: '#f8fafc',
      }}
    >
      {/* 1. LAYERED BACKGROUND ARCHITECTURE */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'radial-gradient(ellipse at 50% 30%, #0d1b2a 0%, #060a14 70%, #020408 100%)',
          zIndex: 1,
        }}
      />

      {/* Volumetric Breathing Lights */}
      <div
        style={{
          position: 'absolute',
          top: -150,
          left: '20%',
          width: 900,
          height: 600,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.accent}33 0%, transparent 70%)`,
          opacity: spotPulse1,
          filter: 'blur(70px)',
          zIndex: 2,
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: -100,
          right: '15%',
          width: 800,
          height: 500,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.subAccent}26 0%, transparent 70%)`,
          opacity: spotPulse2,
          filter: 'blur(80px)',
          zIndex: 2,
          pointerEvents: 'none',
        }}
      />

      {/* Blueprint Grid & Crosshairs */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage:
            'radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px), linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px), linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px)',
          backgroundSize: '40px 40px, 200px 200px, 200px 200px',
          opacity: 0.6,
          zIndex: 3,
          pointerEvents: 'none',
        }}
      />

      {/* 2. CINEMATIC ILLUSTRATION STAGE (Ken Burns Pan & Zoom) */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 4,
          overflow: 'hidden',
        }}
      >
        <div
          style={{
            width: '100%',
            height: '100%',
            transform: `scale(${kbZoom}) translate(${kbPanX}px, ${kbPanY}px) rotate(${kbRot}deg)`,
            transformOrigin: 'center center',
            transition: 'transform 0.05s linear',
          }}
        >
          <Img
            src={staticFile(activeSeq.img)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              filter: 'brightness(1.02) contrast(1.06) saturate(1.05)',
            }}
          />
        </div>

        {/* Cinematic Vignette Shadow */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background:
              'radial-gradient(circle at center, transparent 40%, rgba(5, 8, 17, 0.65) 85%, rgba(3, 5, 12, 0.92) 100%)',
            pointerEvents: 'none',
          }}
        />

        {/* Ambient Top & Bottom Film Letterbox Gradients */}
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            height: 180,
            background: 'linear-gradient(to bottom, rgba(5, 8, 17, 0.92) 0%, transparent 100%)',
            pointerEvents: 'none',
          }}
        />
        <div
          style={{
            position: 'absolute',
            bottom: 0,
            left: 0,
            right: 0,
            height: 220,
            background: 'linear-gradient(to top, rgba(5, 8, 17, 0.95) 0%, transparent 100%)',
            pointerEvents: 'none',
          }}
        />
      </div>

      {/* 3. ENTERPRISE GLASSMORPHIC HUD TELEMETRY OVERLAYS */}
      {/* TOP STATUS BAR */}
      <div
        style={{
          position: 'absolute',
          top: 32,
          left: 48,
          right: 48,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 10,
        }}
      >
        {/* Left: Broadcast Brand & Active Era */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 8,
              padding: '6px 14px',
              borderRadius: 8,
              background: 'rgba(15, 23, 42, 0.75)',
              border: `1px solid ${theme.accent}66`,
              backdropFilter: 'blur(12px)',
            }}
          >
            <div
              style={{
                width: 8,
                height: 8,
                borderRadius: '50%',
                backgroundColor: theme.accent,
                boxShadow: `0 0 10px ${theme.accent}`,
              }}
            />
            <span
              style={{
                fontSize: 12,
                fontWeight: 700,
                letterSpacing: '0.12em',
                color: '#f8fafc',
                textTransform: 'uppercase',
              }}
            >
              NEON RUSH ENTERPRISE DOCS
            </span>
          </div>

          <div
            style={{
              padding: '6px 12px',
              borderRadius: 6,
              background: 'rgba(30, 41, 59, 0.65)',
              border: '1px solid rgba(255, 255, 255, 0.1)',
              fontSize: 11,
              fontWeight: 600,
              letterSpacing: '0.08em',
              color: '#94a3b8',
            }}
          >
            {theme.era}
          </div>
        </div>

        {/* Right: Scientific Element Card (Hg 80) */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 12,
            padding: '6px 16px',
            borderRadius: 10,
            background: 'rgba(15, 23, 42, 0.82)',
            border: '1px solid rgba(255, 255, 255, 0.15)',
            backdropFilter: 'blur(16px)',
            boxShadow: '0 8px 32px rgba(0, 0, 0, 0.4)',
          }}
        >
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              width: 38,
              height: 38,
              borderRadius: 6,
              background: `linear-gradient(135deg, ${theme.accent} 0%, ${theme.subAccent} 100%)`,
              color: '#050811',
              fontWeight: 900,
              fontSize: 18,
              lineHeight: 1,
            }}
          >
            Hg
            <span style={{ fontSize: 9, fontWeight: 700, marginTop: 1 }}>80</span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span style={{ fontSize: 13, fontWeight: 700, color: '#f1f5f9', letterSpacing: '0.04em' }}>
              MERCURY (HYDRARGYRUM)
            </span>
            <div style={{ display: 'flex', gap: 10, fontSize: 10, color: '#94a3b8', marginTop: 2 }}>
              <span>MASS: <b>200.59 u</b></span>
              <span>DENSITY: <b>13.53 g/cm³</b></span>
              <span>MP: <b>-38.83°C</b></span>
              <span>TEMP: <b style={{ color: theme.accent }}>{theme.temp}</b></span>
            </div>
          </div>
        </div>
      </div>

      {/* TOP-LEFT TIMECODE & FRAME TELEMETRY */}
      <div
        style={{
          position: 'absolute',
          top: 86,
          left: 48,
          fontSize: 11,
          fontFamily: 'ui-monospace, "JetBrains Mono", Menlo, Consolas, monospace',
          color: '#64748b',
          letterSpacing: '0.1em',
          zIndex: 10,
        }}
      >
        <span>TC {timecode}</span>
        <span style={{ margin: '0 8px' }}>|</span>
        <span>FRAME {String(frame).padStart(5, '0')} / 23359</span>
        <span style={{ margin: '0 8px' }}>|</span>
        <span style={{ color: theme.accent }}>ACT {currentChapterIdx + 1}/8</span>
      </div>

      {/* 4. CHAPTER INTRO TITLE CARD OVERLAY */}
      {isChapterTitleVisible && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 15,
            opacity: titleCardOpacity,
            transform: `scale(${titleCardScale})`,
            pointerEvents: 'none',
          }}
        >
          <div
            style={{
              padding: '36px 64px',
              borderRadius: 20,
              background: 'rgba(7, 12, 24, 0.88)',
              border: `1px solid ${theme.accent}88`,
              backdropFilter: 'blur(24px)',
              boxShadow: `0 20px 60px rgba(0, 0, 0, 0.6), 0 0 40px ${theme.accent}22`,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              textAlign: 'center',
              maxWidth: 1100,
            }}
          >
            <div
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: 8,
                padding: '4px 14px',
                borderRadius: 20,
                background: `${theme.accent}22`,
                border: `1px solid ${theme.accent}`,
                fontSize: 12,
                fontWeight: 800,
                color: theme.accent,
                letterSpacing: '0.15em',
                textTransform: 'uppercase',
                marginBottom: 16,
              }}
            >
              BABAK {currentChapterIdx + 1} DARI 8
            </div>

            <h1
              style={{
                margin: 0,
                fontSize: 40,
                fontWeight: 900,
                color: '#f8fafc',
                letterSpacing: '-0.02em',
                lineHeight: 1.2,
                textTransform: 'uppercase',
              }}
            >
              {currentChapter.title.replace(/^BABAK \d+:\s*/i, '')}
            </h1>

            <div
              style={{
                marginTop: 16,
                fontSize: 14,
                fontWeight: 600,
                color: '#94a3b8',
                letterSpacing: '0.06em',
              }}
            >
              {theme.diagramTitle}
            </div>
          </div>
        </div>
      )}

      {/* 5. LIVE TECHNICAL INFOGRAPHIC TELEMETRY CARD (Bottom Left) */}
      <div
        style={{
          position: 'absolute',
          bottom: 120,
          left: 48,
          maxWidth: 440,
          padding: '16px 20px',
          borderRadius: 12,
          background: 'rgba(11, 19, 36, 0.82)',
          border: '1px solid rgba(255, 255, 255, 0.12)',
          backdropFilter: 'blur(16px)',
          boxShadow: '0 12px 36px rgba(0, 0, 0, 0.45)',
          zIndex: 10,
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 8 }}>
          <span
            style={{
              fontSize: 10,
              fontWeight: 800,
              letterSpacing: '0.14em',
              color: theme.accent,
              textTransform: 'uppercase',
            }}
          >
            [ SCIENTIFIC TELEMETRY ]
          </span>
          <span style={{ fontSize: 9, color: '#64748b', fontFamily: 'monospace' }}>SEC {totalSec.toFixed(1)}s</span>
        </div>

        <div style={{ fontSize: 13, fontWeight: 700, color: '#f1f5f9', lineHeight: 1.35, marginBottom: 8 }}>
          {theme.diagramTitle}
        </div>

        {/* Dynamic Micro Infographic Graphic based on current Act */}
        {currentChapterIdx === 0 && (
          <div style={{ display: 'flex', gap: 6, fontSize: 10, color: '#94a3b8', fontFamily: 'monospace' }}>
            <span style={{ background: 'rgba(239, 68, 68, 0.15)', padding: '3px 6px', borderRadius: 4, color: '#fca5a5' }}>HgS (Cinnabar)</span>
            <span style={{ background: 'rgba(255, 255, 255, 0.06)', padding: '3px 6px', borderRadius: 4 }}>Mohs: 2.0–2.5</span>
            <span style={{ background: 'rgba(255, 255, 255, 0.06)', padding: '3px 6px', borderRadius: 4 }}>SG: 8.176</span>
          </div>
        )}

        {currentChapterIdx === 1 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4, fontSize: 11, fontFamily: 'monospace', color: '#fed7aa' }}>
            <div>ΔH = +357°C (Thermal Dissociation)</div>
            <div style={{ color: '#fb923c' }}>HgS + O₂ → Hg(vapor)↑ + SO₂(gas)↑</div>
          </div>
        )}

        {currentChapterIdx === 2 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4, fontSize: 11, fontFamily: 'monospace', color: '#a5f3fc' }}>
            <div>Surface Tension: 486.5 mN/m (Extremely High)</div>
            <div>Contact Angle: θ = 140° (Convex Meniscus)</div>
          </div>
        )}

        {currentChapterIdx === 3 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4, fontSize: 11, fontFamily: 'monospace', color: '#fef08a' }}>
            <div>Tomb Scale: 78 meters deep, 100+ channels</div>
            <div>Mechanical continuous pump siphon cycle</div>
          </div>
        )}

        {currentChapterIdx === 4 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4, fontSize: 11, fontFamily: 'monospace', color: '#a7f3d0' }}>
            <div>Tria Prima: Sulfur (Soul) + Mercury (Spirit) + Salt (Body)</div>
            <div>Distillation: Cinnabar sublimation retorts</div>
          </div>
        )}

        {currentChapterIdx === 5 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4, fontSize: 11, fontFamily: 'monospace', color: '#bfdbfe' }}>
            <div>Atmospheric Pressure: P = ρgh = 760 mmHg</div>
            <div>1 atm = 101,325 Pascals (Torricelli Vacuum Void)</div>
          </div>
        )}

        {currentChapterIdx === 6 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4, fontSize: 11, fontFamily: 'monospace', color: '#e9d5ff' }}>
            <div>Toxic Compound: CH₃Hg⁺ (Methylmercury)</div>
            <div>Bioaccumulation: 10,000x trophic amplification</div>
          </div>
        )}

        {currentChapterIdx === 7 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4, fontSize: 11, fontFamily: 'monospace', color: '#bae6fd' }}>
            <div>NASA SERT-1 (1964): Electrostatic Mercury Ion Propulsion</div>
            <div>Superconductivity: R = 0.00 Ω at T = 4.2 K</div>
          </div>
        )}
      </div>

      {/* 6. SWISS KINETIC SUBTITLE BAR (Bottom Center) */}
      <div
        style={{
          position: 'absolute',
          bottom: 48,
          left: 48,
          right: 48,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          zIndex: 20,
        }}
      >
        {activeSentence && (
          <div
            style={{
              padding: '16px 32px',
              borderRadius: 16,
              background: 'rgba(10, 16, 30, 0.88)',
              border: `1px solid ${theme.accent}55`,
              backdropFilter: 'blur(20px)',
              boxShadow: '0 12px 40px rgba(0, 0, 0, 0.65)',
              maxWidth: 1360,
              textAlign: 'center',
            }}
          >
            <p
              style={{
                margin: 0,
                fontSize: 22,
                fontWeight: 700,
                color: '#f8fafc',
                lineHeight: 1.45,
                letterSpacing: '-0.01em',
              }}
            >
              {activeSentence.text}
            </p>
          </div>
        )}

        {/* 7. PROGRESS BAR & CHAPTER SCRUBBER */}
        <div
          style={{
            width: '100%',
            maxWidth: 1400,
            marginTop: 16,
            height: 4,
            background: 'rgba(255, 255, 255, 0.1)',
            borderRadius: 2,
            position: 'relative',
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              height: '100%',
              width: `${progressPercent}%`,
              background: `linear-gradient(to right, ${theme.accent}, ${theme.subAccent})`,
              borderRadius: 2,
              boxShadow: `0 0 8px ${theme.accent}`,
            }}
          />
        </div>
      </div>
    </div>
  );
};
