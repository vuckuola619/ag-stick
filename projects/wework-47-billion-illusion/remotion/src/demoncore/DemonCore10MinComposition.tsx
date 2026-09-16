import React from 'react';
import {
  useCurrentFrame,
  interpolate,
  spring,
  useVideoConfig,
  Img,
  Audio,
  staticFile,
} from 'remotion';

// Import the generated synchronized manifest
import manifestData from '../../public/assets/demon_core/manifest.json';

interface SceneItem {
  scene_id: string;
  act: number;
  act_title: string;
  kinetic_hook_headline: string;
  voiceover_text: string;
  word_count: number;
  start_sec: number;
  speech_duration_sec: number;
  total_scene_duration_sec: number;
  start_frame: number;
  speech_frames: number;
  duration_frames: number;
  end_frame: number;
  audio_file: string;
  image_file: string;
  codex_image_prompt: string;
}

const SCENES: SceneItem[] = manifestData.scenes;
const TOTAL_FRAMES: number = manifestData.total_frames;

// Act Theme Palettes adhering strictly to Neon Rush 2D Color Rules & Los Alamos Aesthetic
const ACT_THEMES: Record<number, {
  accent: string;
  subAccent: string;
  badge: string;
  actName: string;
  radiationState: string;
  dosimeterRad: string;
  alertLevel: 'NORMAL' | 'ELEVATED' | 'CRITICAL' | 'LETHAL';
}> = {
  1: {
    accent: '#FFB300', // Plutonium Amber
    subAccent: '#FF5500', // Core Hazard
    badge: 'ACT I: THE THIRD CORE',
    actName: 'LOS ALAMOS 1945 — 14-LB PLUTONIUM PIT',
    radiationState: 'SUB-CRITICAL STATE (0.12 RAD/h)',
    dosimeterRad: '0.12 RAD',
    alertLevel: 'NORMAL',
  },
  2: {
    accent: '#00E5FF', // Electric Neutron Cyan
    subAccent: '#FFB300', // Tungsten Carbide
    badge: 'ACT II: TICKLING THE DRAGON\'S TAIL',
    actName: 'OMEGA SITE — TUNGSTEN REFLECTION EXPERIMENTS',
    radiationState: 'NEAR-CRITICAL THRESHOLD (k = 0.995)',
    dosimeterRad: '14.8 RAD',
    alertLevel: 'ELEVATED',
  },
  3: {
    accent: '#FF2244', // Lethal Danger Crimson
    subAccent: '#0088FF', // Ionization Blue
    badge: 'ACT III: INCIDENT 1 — HARRY DAGHLIAN',
    actName: 'AUG 21, 1945 — THE MIDNIGHT BRICK SLIP',
    radiationState: 'PROMPT CRITICAL BURST (510 REMS)',
    dosimeterRad: '510 REM',
    alertLevel: 'LETHAL',
  },
  4: {
    accent: '#00F0FF', // Cherenkov Ionization Flare
    subAccent: '#FF0033', // Flash Danger
    badge: 'ACT IV: THE SCREWDRIVER INCIDENT',
    actName: 'MAY 21, 1946 — 1-MILLIMETER SCREWDRIVER SLIP',
    radiationState: 'SUPER-CRITICAL EXCURSION (1,000+ RADS)',
    dosimeterRad: '1,000+ RAD',
    alertLevel: 'LETHAL',
  },
  5: {
    accent: '#FFAA00', // Memorial Gold
    subAccent: '#00E5FF', // Robotic Age
    badge: 'ACT V: THE AFTERMATH & LEGACY',
    actName: 'ROBOTIC CRITICALITY & PACIFIC DETONATION',
    radiationState: 'REMOTE MANIPULATION PROTOCOL ONLY',
    dosimeterRad: '0.04 RAD',
    alertLevel: 'NORMAL',
  },
};

export const DemonCore10MinComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Active scene determination based on frame ranges
  let activeScene = SCENES[0];
  for (let i = 0; i < SCENES.length; i++) {
    if (frame >= SCENES[i].start_frame) {
      activeScene = SCENES[i];
    }
  }

  const theme = ACT_THEMES[activeScene.act] || ACT_THEMES[1];
  const sceneRelativeFrame = Math.max(0, frame - activeScene.start_frame);

  // 1. Kinetic Headline Entrance Spring
  const headlineEntrance = spring({
    frame: sceneRelativeFrame,
    fps,
    config: { damping: 13, stiffness: 120, mass: 0.7 },
  });

  const headlineOpacity = interpolate(
    sceneRelativeFrame,
    [0, 10, activeScene.duration_frames - 15, activeScene.duration_frames],
    [0, 1, 1, 0.85],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // 2. Living Stickman Puppet Breathing & Camera Crawl
  const kbScale = interpolate(
    sceneRelativeFrame,
    [0, activeScene.duration_frames],
    [1.0, 1.055],
    { extrapolateRight: 'clamp' }
  );
  
  const breathingScale = 1.0 + Math.sin(frame / 26) * 0.012;
  const floatingTilt = Math.sin(frame / 42) * 0.9;
  const panX = Math.sin((frame + Number(activeScene.scene_id) * 75) / 85) * 12;
  const panY = Math.cos((frame + Number(activeScene.scene_id) * 75) / 105) * 7;

  // 3. CHERENKOV RADIATION FLASH & SCREEN SHAKE (Scenes 16 & 25)
  const isCherenkovScene = activeScene.scene_id === '16' || activeScene.scene_id === '25';
  let cherenkovFlashOpacity = 0;
  let shakeX = 0;
  let shakeY = 0;

  if (isCherenkovScene) {
    // Blinding blue flash burst in first 40 frames of scene
    cherenkovFlashOpacity = interpolate(
      sceneRelativeFrame,
      [0, 3, 12, 45],
      [0.95, 1.0, 0.65, 0.0],
      { extrapolateRight: 'clamp' }
    );
    // Violent screen shake
    if (sceneRelativeFrame < 35) {
      const shakeDecay = (35 - sceneRelativeFrame) / 35;
      shakeX = (Math.sin(sceneRelativeFrame * 2.8) * 22 + Math.cos(sceneRelativeFrame * 4.1) * 14) * shakeDecay;
      shakeY = (Math.cos(sceneRelativeFrame * 3.2) * 18 + Math.sin(sceneRelativeFrame * 5.3) * 12) * shakeDecay;
    }
  }

  // 4. Volumetric Ambient Glow Pulses
  const glowPulse1 = 0.45 + 0.15 * Math.sin(frame / 35);
  const glowPulse2 = 0.35 + 0.12 * Math.cos(frame / 48);

  // 5. Broadcast Timecode
  const totalSec = frame / fps;
  const tcH = Math.floor(totalSec / 3600);
  const tcM = Math.floor((totalSec % 3600) / 60);
  const tcS = Math.floor(totalSec % 60);
  const tcF = frame % fps;
  const timecode = `${String(tcH).padStart(2, '0')}:${String(tcM).padStart(2, '0')}:${String(tcS).padStart(2, '0')}:${String(tcF).padStart(2, '0')}`;
  const progressPercent = Math.min(100, (frame / TOTAL_FRAMES) * 100);

  // 6. Dynamic Dosimeter RAD readout calculation
  let currentRadDisplay = theme.dosimeterRad;
  if (activeScene.scene_id === '16') {
    const surge = Math.min(510, Math.floor(interpolate(sceneRelativeFrame, [0, 20], [15, 510])));
    currentRadDisplay = `${surge} REM!`;
  } else if (activeScene.scene_id === '24') {
    const preSurge = Math.floor(interpolate(sceneRelativeFrame, [0, 25], [18, 280]));
    currentRadDisplay = `${preSurge} RAD`;
  } else if (activeScene.scene_id === '25') {
    const microsecondRad = Math.floor(interpolate(sceneRelativeFrame, [0, 15], [280, 1000]));
    currentRadDisplay = `${microsecondRad}+ RAD!`;
  }

  // Scene image path
  const sceneImagePath = `assets/demon_core/scenes/scene_${activeScene.scene_id}.png`;

  return (
    <div
      style={{
        position: 'relative',
        width: 1920,
        height: 1080,
        backgroundColor: '#0c0e14',
        overflow: 'hidden',
        fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        color: '#f8fafc',
      }}
    >
      {/* 0. MASTER AUDIO TRACK (Mastered Voiceover) */}
      <Audio src={staticFile('assets/demon_core/voiceover_mastered.wav')} />

      {/* 1. LAYERED BACKGROUND ARCHITECTURE */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'radial-gradient(ellipse at 50% 35%, #141824 0%, #0c0e14 75%, #05060a 100%)',
          zIndex: 1,
        }}
      />

      {/* Volumetric Breathing Neons */}
      <div
        style={{
          position: 'absolute',
          top: -150,
          left: '20%',
          width: 950,
          height: 650,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.accent}33 0%, transparent 70%)`,
          opacity: glowPulse1,
          filter: 'blur(90px)',
          zIndex: 2,
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: -120,
          right: '18%',
          width: 850,
          height: 550,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.subAccent}28 0%, transparent 70%)`,
          opacity: glowPulse2,
          filter: 'blur(95px)',
          zIndex: 2,
          pointerEvents: 'none',
        }}
      />

      {/* Engineering Scientific Dot Grid & Crosshairs */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage:
            'radial-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1px), linear-gradient(to right, rgba(255, 255, 255, 0.015) 1px, transparent 1px), linear-gradient(to bottom, rgba(255, 255, 255, 0.015) 1px, transparent 1px)',
          backgroundSize: '45px 45px, 225px 225px, 225px 225px',
          opacity: 0.65,
          zIndex: 3,
          pointerEvents: 'none',
        }}
      />

      {/* 2. VISUAL STAGE: 2D CARTOON STICKMAN SCENE (with screen shake) */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          zIndex: 4,
          overflow: 'hidden',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          transform: `translate(${shakeX}px, ${shakeY}px)`,
        }}
      >
        <div
          style={{
            width: '100%',
            height: '100%',
            transform: `scale(${kbScale * breathingScale}) translate(${panX}px, ${panY}px) rotate(${floatingTilt}deg)`,
            transformOrigin: 'center center',
          }}
        >
          <Img
            src={staticFile(sceneImagePath)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              filter: 'contrast(1.06) brightness(1.02) saturate(1.05)',
            }}
          />
        </div>

        {/* Cinematic Vignette & Bottom Text Contrast Falloff */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background:
              'radial-gradient(circle at center, transparent 45%, rgba(10, 12, 18, 0.5) 85%, rgba(5, 6, 10, 0.85) 100%), linear-gradient(to top, rgba(5, 8, 17, 0.90) 0%, rgba(5, 8, 17, 0.45) 28%, transparent 60%)',
            pointerEvents: 'none',
          }}
        />
      </div>

      {/* 3. CHERENKOV RADIATION BLINDING BLUE BURST (Scenes 16 & 25) */}
      {cherenkovFlashOpacity > 0 && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            zIndex: 6,
            background: `radial-gradient(circle at 50% 50%, #00F0FF ${cherenkovFlashOpacity * 90}%, #0055FF 100%)`,
            opacity: cherenkovFlashOpacity,
            mixBlendMode: 'screen',
            pointerEvents: 'none',
          }}
        />
      )}

      {/* 4. FLOATING IONIZING PARTICLES & DUST */}
      <div style={{ position: 'absolute', inset: 0, zIndex: 5, pointerEvents: 'none' }}>
        {[...Array(14)].map((_, i) => {
          const speed = 1.1 + (i % 4) * 0.45;
          const yPos = 1080 - (((frame * speed + i * 90) % 1150) - 50);
          const xPos = ((i * 145 + Math.sin(frame / 25 + i) * 35) % 1880) + 20;
          const size = 3 + (i % 3) * 2;
          const opacity = 0.25 + 0.25 * Math.sin(frame / 20 + i);
          const particleColor = isCherenkovScene ? '#00E5FF' : theme.accent;
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: xPos,
                top: yPos,
                width: size,
                height: size,
                borderRadius: '50%',
                backgroundColor: particleColor,
                opacity,
                filter: `blur(${size > 4 ? 2 : 1}px) drop-shadow(0 0 6px ${particleColor})`,
              }}
            />
          );
        })}
      </div>

      {/* 5. TOP BROADCAST HEADER & RADIATION DOSIMETER HUD */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: 60,
          right: 60,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 10,
        }}
      >
        {/* Left: Channel Badge */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <div
            style={{
              padding: '6px 14px',
              backgroundColor: 'rgba(10, 14, 24, 0.85)',
              border: `1.5px solid ${theme.accent}66`,
              borderRadius: 8,
              backdropFilter: 'blur(12px)',
              boxShadow: `0 4px 20px rgba(0, 0, 0, 0.4), 0 0 15px ${theme.accent}22`,
            }}
          >
            <span
              style={{
                fontSize: 13,
                fontWeight: 900,
                letterSpacing: '0.14em',
                color: theme.accent,
                textTransform: 'uppercase',
              }}
            >
              NEON ATOM // DOCS
            </span>
          </div>
          <span
            style={{
              fontSize: 12,
              fontWeight: 700,
              letterSpacing: '0.12em',
              color: 'rgba(255, 255, 255, 0.65)',
              textTransform: 'uppercase',
            }}
          >
            EPISODE 03: THE DEMON CORE
          </span>
        </div>

        {/* Center: Act Badge */}
        <div
          style={{
            padding: '6px 18px',
            backgroundColor: 'rgba(8, 11, 20, 0.85)',
            border: `1px solid ${theme.accent}44`,
            borderRadius: 20,
            backdropFilter: 'blur(14px)',
            display: 'flex',
            alignItems: 'center',
            gap: 10,
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
              fontWeight: 800,
              letterSpacing: '0.15em',
              color: '#ffffff',
              textTransform: 'uppercase',
            }}
          >
            {theme.badge}
          </span>
        </div>

        {/* Right: Live Radiation Dosimeter HUD */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 12,
            padding: '6px 16px',
            backgroundColor: theme.alertLevel === 'LETHAL' ? 'rgba(255, 20, 50, 0.25)' : 'rgba(8, 11, 20, 0.85)',
            border: `1.5px solid ${theme.alertLevel === 'LETHAL' ? '#FF2244' : theme.accent}77`,
            borderRadius: 8,
            backdropFilter: 'blur(12px)',
            boxShadow: theme.alertLevel === 'LETHAL' ? '0 0 25px rgba(255, 34, 68, 0.5)' : 'none',
          }}
        >
          {/* Pulsing Geiger Dot */}
          <div
            style={{
              width: 10,
              height: 10,
              borderRadius: '50%',
              backgroundColor: theme.alertLevel === 'LETHAL' ? '#FF2244' : theme.accent,
              boxShadow: `0 0 12px ${theme.alertLevel === 'LETHAL' ? '#FF2244' : theme.accent}`,
              animation: 'pulse 0.8s infinite',
            }}
          />
          <span
            style={{
              fontSize: 11,
              fontWeight: 700,
              letterSpacing: '0.1em',
              color: 'rgba(255, 255, 255, 0.7)',
              textTransform: 'uppercase',
            }}
          >
            DOSIMETER:
          </span>
          <span
            style={{
              fontFamily: 'JetBrains Mono, monospace',
              fontSize: 14,
              fontWeight: 900,
              color: theme.alertLevel === 'LETHAL' ? '#FF2244' : theme.accent,
              letterSpacing: '0.08em',
            }}
          >
            {currentRadDisplay}
          </span>
        </div>
      </div>

      {/* 6. KINETIC HOOK HEADLINE OVERLAY */}
      <div
        style={{
          position: 'absolute',
          top: 108,
          left: 60,
          zIndex: 10,
          opacity: headlineOpacity,
          transform: `translateY(${interpolate(headlineEntrance, [0, 1], [-20, 0])}px)`,
        }}
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: 8,
              padding: '4px 12px',
              backgroundColor: `${theme.accent}18`,
              border: `1px solid ${theme.accent}44`,
              borderRadius: 6,
              width: 'fit-content',
            }}
          >
            <span
              style={{
                fontSize: 11,
                fontWeight: 800,
                letterSpacing: '0.14em',
                color: theme.accent,
                textTransform: 'uppercase',
              }}
            >
              SCENE {activeScene.scene_id} // {theme.actName}
            </span>
          </div>

          {/* Master Kinetic Headline */}
          <h1
            style={{
              margin: 0,
              fontSize: 38,
              fontWeight: 900,
              letterSpacing: '-0.02em',
              lineHeight: 1.1,
              color: '#ffffff',
              textShadow: `0 4px 20px rgba(0, 0, 0, 0.8), 0 0 30px ${theme.accent}33`,
              textTransform: 'uppercase',
            }}
          >
            {activeScene.kinetic_hook_headline}
          </h1>
        </div>
      </div>

      {/* 7. DYNAMIC LOWER THIRD SUBTITLES */}
      <div
        style={{
          position: 'absolute',
          bottom: 75,
          left: 80,
          right: 80,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 10,
        }}
      >
        <div
          style={{
            maxWidth: 1400,
            padding: '18px 36px',
            backgroundColor: 'rgba(7, 10, 18, 0.86)',
            border: `1.5px solid ${theme.accent}38`,
            borderRadius: 14,
            backdropFilter: 'blur(16px)',
            boxShadow: `0 12px 40px rgba(0, 0, 0, 0.7), 0 0 30px ${theme.accent}15`,
            textAlign: 'center',
          }}
        >
          <p
            style={{
              margin: 0,
              fontSize: 27,
              fontWeight: 600,
              lineHeight: 1.45,
              color: '#f8fafc',
              letterSpacing: '0.01em',
              textShadow: '0 2px 8px rgba(0, 0, 0, 0.9)',
            }}
          >
            {activeScene.voiceover_text}
          </p>
        </div>
      </div>

      {/* 8. BOTTOM BROADCAST TIMELINE PROGRESS BAR */}
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 48,
          backgroundColor: 'rgba(5, 7, 12, 0.95)',
          borderTop: '1px solid rgba(255, 255, 255, 0.08)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '0 40px',
          zIndex: 10,
        }}
      >
        {/* Left: Timecode */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          <span
            style={{
              fontFamily: 'JetBrains Mono, monospace',
              fontSize: 14,
              fontWeight: 700,
              letterSpacing: '0.08em',
              color: theme.accent,
            }}
          >
            {timecode}
          </span>
          <span
            style={{
              fontSize: 12,
              fontWeight: 600,
              letterSpacing: '0.05em',
              color: 'rgba(255, 255, 255, 0.4)',
            }}
          >
            FRAME {frame} / {TOTAL_FRAMES}
          </span>
        </div>

        {/* Center: Sleek Progress Bar Track */}
        <div
          style={{
            flex: 1,
            height: 4,
            backgroundColor: 'rgba(255, 255, 255, 0.12)',
            borderRadius: 2,
            margin: '0 40px',
            overflow: 'hidden',
            position: 'relative',
          }}
        >
          <div
            style={{
              width: `${progressPercent}%`,
              height: '100%',
              backgroundColor: theme.accent,
              boxShadow: `0 0 10px ${theme.accent}`,
              transition: 'width 0.1s linear',
            }}
          />
        </div>

        {/* Right: Radiation Status */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div
            style={{
              width: 7,
              height: 7,
              borderRadius: '50%',
              backgroundColor: theme.accent,
            }}
          />
          <span
            style={{
              fontSize: 11,
              fontWeight: 800,
              letterSpacing: '0.12em',
              color: 'rgba(255, 255, 255, 0.65)',
              textTransform: 'uppercase',
            }}
          >
            {theme.radiationState}
          </span>
        </div>
      </div>
    </div>
  );
};
