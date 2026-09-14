import React from 'react';
import {
  useCurrentFrame,
  interpolate,
  spring,
  useVideoConfig,
  Img,
  staticFile,
} from 'remotion';

import manifestData from '../../public/assets/kokoro_8min_manifest.json';

interface SceneItem {
  id: number;
  title: string;
  tag: string;
  stat: string;
  text: string;
  visual_type: string;
  visual_src: string;
  graphic_id: string;
  start_sec: number;
  duration_sec: number;
  start_frame: number;
  duration_frames: number;
}

const SCENES: SceneItem[] = manifestData.scenes;
const TOTAL_FRAMES: number = manifestData.total_frames;

// Act Theme Colors & Accents
const ACT_THEMES: Record<number, { accent: string; subAccent: string; badge: string; era: string }> = {
  1: { accent: '#ef4444', subAccent: '#f59e0b', badge: 'PREHISTORIC DISCOVERY', era: '7000 BCE — ÇATALHÖYÜK' },
  2: { accent: '#f97316', subAccent: '#fbbf24', badge: 'THERMAL TRANSFORMATION', era: 'PRIMITIVE SMELTING' },
  3: { accent: '#06b6d4', subAccent: '#38bdf8', badge: 'ANOMALOUS PHYSICS', era: 'ELEMENTAL PROPERTIES' },
  4: { accent: '#eab308', subAccent: '#dc2626', badge: 'IMPERIAL OBSESSION', era: '210 BCE — QIN MAUSOLEUM' },
  5: { accent: '#10b981', subAccent: '#6366f1', badge: 'WESTERN ALCHEMY', era: '1680 CE — TRIA PRIMA' },
  6: { accent: '#3b82f6', subAccent: '#60a5fa', badge: 'SCIENTIFIC ENLIGHTENMENT', era: '1643 CE — 1714 CE' },
  7: { accent: '#a855f7', subAccent: '#ec4899', badge: 'TOXICOLOGY & TREATY', era: '1956 CE — 2013 CE' },
  8: { accent: '#38bdf8', subAccent: '#f8fafc', badge: 'QUANTUM & COSMIC DAWN', era: '1964 CE — RELATIVISTIC' },
};

// Signature High-CTR Neon Rush Hook Headlines for Maximum Impression & Retention
const NEON_RUSH_HOOKS: Record<number, string> = {
  1: 'FOUND QUICKSILVER?',
  2: 'THE SACRED CINNABAR',
  3: 'THE RITUAL POWDER',
  4: 'DEADLIEST ROMAN MINES',
  5: 'THE CAMPFIRE ACCIDENT',
  6: 'THERMAL DISSOCIATION',
  7: 'LIVING LIQUID SILVER!',
  8: 'THE MIRROR BEADS',
  9: '13.5x HEAVIER THAN WATER!',
  10: 'SOLID IRON FLOATS?',
  11: 'THE CONVEX MENISCUS (140°)',
  12: 'GOLD DISSOLVED IN SECONDS!',
  13: 'SPANISH SILVER EMPIRE',
  14: 'THE IMMORTALITY ELIXIR',
  15: '100 MERCURY RIVERS!',
  16: 'THE FATAL OBSESSION',
  17: 'WESTERN ALCHEMY (TRIA PRIMA)',
  18: "NEWTON'S SECRET LAB",
  19: "TORRICELLI'S VACUUM (760mm)",
  20: 'THE FIRST THERMOMETER',
  21: 'MURANO MIRROR GUILDS',
  22: 'THE MAD HATTER CURSE',
  23: 'MINAMATA BAY DISASTER',
  24: 'THE GLOBAL UN BAN (2013)',
  25: 'SUPERCONDUCTIVITY AT 4.2K',
  26: 'NASA SERT-1 ION ENGINE',
  27: 'RELATIVISTIC QUANTUM METAL',
  28: 'FROM CAVE TO COSMOS',
};

function getSceneTheme(sceneId: number) {
  if (sceneId <= 4) return ACT_THEMES[1];
  if (sceneId <= 8) return ACT_THEMES[2];
  if (sceneId <= 13) return ACT_THEMES[3];
  if (sceneId <= 16) return ACT_THEMES[4];
  if (sceneId <= 18) return ACT_THEMES[5];
  if (sceneId <= 21) return ACT_THEMES[6];
  if (sceneId <= 24) return ACT_THEMES[7];
  return ACT_THEMES[8];
}

export const MercuryEnglish8MinComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Find active scene based on frame
  let activeScene = SCENES[0];
  for (let i = 0; i < SCENES.length; i++) {
    if (frame >= SCENES[i].start_frame) {
      activeScene = SCENES[i];
    }
  }

  const theme = getSceneTheme(activeScene.id);
  const sceneRelativeFrame = frame - activeScene.start_frame;

  // Title Card Spring Animation (Punchy Editorial Reveal)
  const titleEntrance = spring({
    frame: sceneRelativeFrame,
    fps,
    config: { damping: 14, stiffness: 100, mass: 0.8 },
  });

  const titleCardOpacity = interpolate(
    sceneRelativeFrame,
    [0, 12, activeScene.duration_frames - 20, activeScene.duration_frames],
    [0, 1, 1, 0.85],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // Subtle Cinematic Ken Burns Pan/Zoom for Images
  const kbZoom = interpolate(
    sceneRelativeFrame,
    [0, activeScene.duration_frames],
    [1.0, 1.07],
    { extrapolateRight: 'clamp' }
  );
  const kbPanX = Math.sin((frame + activeScene.id * 80) / 90) * 14;
  const kbPanY = Math.cos((frame + activeScene.id * 80) / 110) * 8;

  // Atmospheric spotlight pulsing
  const spotPulse1 = 0.5 + 0.15 * Math.sin(frame / 40);
  const spotPulse2 = 0.4 + 0.12 * Math.cos(frame / 55);

  // Timecode formatting
  const totalSec = frame / fps;
  const tcH = Math.floor(totalSec / 3600);
  const tcM = Math.floor((totalSec % 3600) / 60);
  const tcS = Math.floor(totalSec % 60);
  const tcF = frame % fps;
  const timecode = `${String(tcH).padStart(2, '0')}:${String(tcM).padStart(2, '0')}:${String(tcS).padStart(2, '0')}:${String(tcF).padStart(2, '0')}`;

  // Video progress bar percent
  const progressPercent = Math.min(100, (frame / TOTAL_FRAMES) * 100);

  // Dynamic Scene Visual Renderer (100% Authentic Neon Rush 2D Cartoon Stickman Art)
  const renderVisual = () => {
    const sceneFileName = `assets/scenes_neon_rush/scene_${String(activeScene.id).padStart(2, '0')}.png`;
    return (
      <div
        style={{
          position: 'absolute',
          inset: 0,
          overflow: 'hidden',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <div
          style={{
            width: '100%',
            height: '100%',
            transform: `scale(${kbZoom}) translate(${kbPanX}px, ${kbPanY}px)`,
            transformOrigin: 'center center',
          }}
        >
          <Img
            src={staticFile(sceneFileName)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              filter: 'brightness(1.02) contrast(1.05) saturate(1.06)',
            }}
          />
        </div>
        {/* Subtle bottom shadow to guarantee high text contrast without muddying bright art */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background:
              'linear-gradient(to top, rgba(5, 8, 17, 0.85) 0%, rgba(5, 8, 17, 0.35) 26%, transparent 60%)',
            pointerEvents: 'none',
          }}
        />
      </div>
    );
  };

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

      {/* Volumetric Breathing Spotlight */}
      <div
        style={{
          position: 'absolute',
          top: -120,
          left: '25%',
          width: 900,
          height: 600,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.accent}33 0%, transparent 70%)`,
          opacity: spotPulse1,
          filter: 'blur(80px)',
          zIndex: 2,
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: -100,
          right: '20%',
          width: 800,
          height: 500,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.subAccent}26 0%, transparent 70%)`,
          opacity: spotPulse2,
          filter: 'blur(90px)',
          zIndex: 2,
          pointerEvents: 'none',
        }}
      />

      {/* Engineering Blueprint Grid */}
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

      {/* 2. DYNAMIC VISUAL STAGE (Dedicated per Scene, ZERO Repetition) */}
      <div style={{ position: 'absolute', inset: 0, zIndex: 4 }}>
        {renderVisual()}
      </div>

      {/* 3. GLASSMORPHIC TOP TELEMETRY HUD */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: 48,
          right: 48,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 10,
        }}
      >
        {/* Left: Brand Badge & Active Era */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 8,
              padding: '8px 16px',
              borderRadius: 8,
              background: 'rgba(15, 23, 42, 0.85)',
              border: `1px solid ${theme.accent}88`,
              backdropFilter: 'blur(16px)',
            }}
          >
            <div
              style={{
                width: 10,
                height: 10,
                borderRadius: '50%',
                backgroundColor: theme.accent,
                boxShadow: `0 0 12px ${theme.accent}`,
              }}
            />
            <span
              style={{
                fontSize: 13,
                fontWeight: 800,
                letterSpacing: '0.12em',
                color: '#f8fafc',
                textTransform: 'uppercase',
              }}
            >
              NEON RUSH DOCS
            </span>
          </div>

          <div
            style={{
              padding: '8px 14px',
              borderRadius: 8,
              background: 'rgba(30, 41, 59, 0.75)',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              fontSize: 12,
              fontWeight: 700,
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
            background: 'rgba(15, 23, 42, 0.85)',
            border: '1px solid rgba(255, 255, 255, 0.15)',
            backdropFilter: 'blur(16px)',
          }}
        >
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              width: 40,
              height: 40,
              borderRadius: 6,
              background: `linear-gradient(135deg, ${theme.accent} 0%, ${theme.subAccent} 100%)`,
              color: '#050811',
              fontWeight: 900,
              fontSize: 19,
              lineHeight: 1,
            }}
          >
            Hg
            <span style={{ fontSize: 9, fontWeight: 700, marginTop: 1 }}>80</span>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span style={{ fontSize: 13, fontWeight: 800, color: '#f8fafc', letterSpacing: '0.04em' }}>
              MERCURY (HYDRARGYRUM)
            </span>
            <span style={{ fontSize: 11, color: '#94a3b8', fontFamily: 'monospace' }}>
              DENSITY: 13.53 g/cm³ | ATOMIC MASS: 200.59
            </span>
          </div>
        </div>
      </div>

      {/* 4. LARGE PUNCHY EDITORIAL HEADLINE (Clean Typography, NO SUBTITLES) */}
      <div
        style={{
          position: 'absolute',
          bottom: 70,
          left: 48,
          right: 48,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'flex-end',
          zIndex: 10,
          opacity: titleCardOpacity,
          transform: `translateY(${(1 - titleEntrance) * 16}px)`,
        }}
      >
        {/* Left Column: Punchy Scene Title & Category Tag */}
        <div style={{ maxWidth: 1100 }}>
          {/* Category Tag */}
          <div
            style={{
              display: 'inline-block',
              padding: '6px 14px',
              borderRadius: 6,
              background: `${theme.accent}26`,
              border: `1px solid ${theme.accent}88`,
              fontSize: 13,
              fontWeight: 800,
              letterSpacing: '0.12em',
              color: theme.accent,
              marginBottom: 10,
              textTransform: 'uppercase',
            }}
          >
            {activeScene.tag}
          </div>

          {/* Neon Rush YouTube High-CTR Headline */}
          <div
            style={{
              fontSize: 56,
              fontWeight: 900,
              fontFamily: '"Impact", "Arial Black", "Montserrat", sans-serif',
              letterSpacing: '0.01em',
              lineHeight: 1.05,
              color: '#FFE600',
              WebkitTextStroke: '3px #000000',
              textShadow:
                '3px 3px 0 #000000, -3px -3px 0 #000000, 3px -3px 0 #000000, -3px 3px 0 #000000, 0 8px 24px rgba(0, 0, 0, 0.95)',
              textTransform: 'uppercase',
            }}
          >
            {NEON_RUSH_HOOKS[activeScene.id] || activeScene.title}
          </div>
        </div>

        {/* Right Column: High-Contrast Scientific Stat Badge */}
        <div
          style={{
            padding: '14px 24px',
            borderRadius: 14,
            background: 'rgba(15, 23, 42, 0.9)',
            border: `2px solid ${theme.accent}`,
            boxShadow: `0 8px 32px rgba(0, 0, 0, 0.5), 0 0 20px ${theme.accent}33`,
            backdropFilter: 'blur(20px)',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'flex-end',
          }}
        >
          <span style={{ fontSize: 11, fontWeight: 700, color: '#94a3b8', letterSpacing: '0.1em', textTransform: 'uppercase' }}>
            SCIENTIFIC METRIC
          </span>
          <span style={{ fontSize: 24, fontWeight: 900, color: theme.accent, marginTop: 2, letterSpacing: '0.02em' }}>
            {activeScene.stat}
          </span>
        </div>
      </div>

      {/* 5. MINIMALIST BOTTOM RUNNING TIMELINE PROGRESS */}
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 5,
          backgroundColor: 'rgba(255, 255, 255, 0.08)',
          zIndex: 20,
        }}
      >
        <div
          style={{
            width: `${progressPercent}%`,
            height: '100%',
            background: `linear-gradient(to right, ${theme.accent}, ${theme.subAccent})`,
            boxShadow: `0 0 10px ${theme.accent}`,
          }}
        />
      </div>

      {/* TIMECODE HUD (Bottom Right) */}
      <div
        style={{
          position: 'absolute',
          bottom: 16,
          right: 48,
          fontSize: 12,
          fontFamily: 'ui-monospace, "JetBrains Mono", monospace',
          color: '#64748b',
          letterSpacing: '0.1em',
          zIndex: 20,
        }}
      >
        {timecode} / 00:08:14:13
      </div>
    </div>
  );
};
