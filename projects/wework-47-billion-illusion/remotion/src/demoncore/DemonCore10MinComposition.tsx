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

// Historical Timeline & Era Condition Milestones matching 1945-1946 Manhattan Project
export interface EraMilestone {
  act: number;
  label: string;
  sub: string;
  location: string;
  condition: string;
  flux: string;
  startFrame: number;
  endFrame: number;
  percent: number;
  accent: string;
  subAccent: string;
  alertLevel: 'NORMAL' | 'ELEVATED' | 'CRITICAL' | 'LETHAL';
}

export const HISTORICAL_TIMELINE: EraMilestone[] = [
  {
    act: 1,
    label: '1945: PROJECT Y',
    sub: 'THE THIRD CORE (RU-30)',
    location: 'LOS ALAMOS CANYON, NM',
    condition: 'SUB-CRITICAL STATE',
    flux: '0.12 RAD/h',
    startFrame: 0,
    endFrame: 3576,
    percent: 0,
    accent: '#FFB300', // Plutonium Amber
    subAccent: '#FF5500',
    alertLevel: 'NORMAL',
  },
  {
    act: 2,
    label: "AUG '45: REFLECTION",
    sub: "DRAGON'S TAIL EXPERIMENTS",
    location: 'OMEGA SITE LAB',
    condition: 'NEAR-CRITICAL (k = 0.995)',
    flux: '14.8 RAD/h',
    startFrame: 3576,
    endFrame: 7499,
    percent: 19.6,
    accent: '#00E5FF', // Neutron Cyan
    subAccent: '#FFB300',
    alertLevel: 'ELEVATED',
  },
  {
    act: 3,
    label: "AUG 21 '45: DAGHLIAN",
    sub: 'MIDNIGHT BRICK SLIP',
    location: 'OMEGA SITE BENCH',
    condition: 'PROMPT CRITICAL FLASH',
    flux: '510 REM (LETHAL)',
    startFrame: 7499,
    endFrame: 10729,
    percent: 41.1,
    accent: '#FF2244', // Danger Crimson
    subAccent: '#0088FF',
    alertLevel: 'LETHAL',
  },
  {
    act: 4,
    label: "MAY 21 '46: SLOTIN",
    sub: '1MM FLATHEAD SLIP',
    location: 'ASSEMBLY ROOM, NM',
    condition: 'SUPER-CRITICAL BURST',
    flux: '1,000+ RAD (500µs)',
    startFrame: 10729,
    endFrame: 14646,
    percent: 58.8,
    accent: '#00F0FF', // Cherenkov Flare
    subAccent: '#FF0033',
    alertLevel: 'LETHAL',
  },
  {
    act: 5,
    label: "JULY '46+: CROSSROADS",
    sub: 'REMOTE AGE & PACIFIC DETONATION',
    location: 'BIKINI ATOLL // REMOTE',
    condition: 'REMOTE PROTOCOL ONLY',
    flux: '0.04 RAD/h',
    startFrame: 14646,
    endFrame: 18252,
    percent: 80.2,
    accent: '#FFAA00', // Memorial Gold
    subAccent: '#00E5FF',
    alertLevel: 'NORMAL',
  },
];

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

  const currentEra =
    HISTORICAL_TIMELINE.find((e) => e.act === activeScene.act) ||
    HISTORICAL_TIMELINE[0];
  const theme = currentEra;
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

  // 6. Dynamic Dosimeter RAD readout calculation matching Manhattan Project telemetry
  let currentRadDisplay = currentEra.flux;
  if (activeScene.scene_id === '16') {
    const surge = Math.min(510, Math.floor(interpolate(sceneRelativeFrame, [0, 20], [15, 510])));
    currentRadDisplay = `${surge} REM (LETHAL BURST!)`;
  } else if (activeScene.scene_id === '24') {
    const preSurge = Math.floor(interpolate(sceneRelativeFrame, [0, 25], [18, 280]));
    currentRadDisplay = `${preSurge} RAD (NEAR-CRITICAL)`;
  } else if (activeScene.scene_id === '25') {
    const microsecondRad = Math.floor(interpolate(sceneRelativeFrame, [0, 15], [280, 1000]));
    currentRadDisplay = `${microsecondRad}+ RAD (CHERENKOV FLASH!)`;
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
              'linear-gradient(to bottom, rgba(5, 8, 17, 0.85) 0%, rgba(5, 8, 17, 0.40) 70px, transparent 140px), radial-gradient(circle at center, transparent 45%, rgba(10, 12, 18, 0.5) 85%, rgba(5, 6, 10, 0.85) 100%), linear-gradient(to top, rgba(5, 8, 17, 0.90) 0%, rgba(5, 8, 17, 0.45) 28%, transparent 60%)',
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
      {/* 5. TOP HISTORICAL TELEMETRY HUD (Scientific Element & Location Telemetry - NO FIELDS) */}
      <div
        style={{
          position: 'absolute',
          top: 24,
          left: 50,
          right: 50,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 15,
          pointerEvents: 'none',
        }}
      >
        {/* Left: Scientific Element Card (Pu 94) & Channel Identifier */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          {/* Element Box Pu 94 */}
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              width: 44,
              height: 44,
              borderRadius: 4,
              background: `linear-gradient(135deg, ${currentEra.accent} 0%, ${currentEra.subAccent} 100%)`,
              color: '#050811',
              fontWeight: 900,
              fontSize: 20,
              lineHeight: 1,
              boxShadow: `0 0 14px ${currentEra.accent}66`,
            }}
          >
            Pu
            <span style={{ fontSize: 9, fontWeight: 800, marginTop: 1 }}>94</span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span
              style={{
                fontSize: 14,
                fontWeight: 900,
                color: '#ffffff',
                letterSpacing: '0.08em',
                textShadow: '2px 2px 4px #000000',
                textTransform: 'uppercase',
              }}
            >
              PLUTONIUM-239
            </span>
            <span
              style={{
                fontSize: 11,
                color: '#94a3b8',
                fontFamily: 'monospace',
                letterSpacing: '0.04em',
                textShadow: '1px 1px 2px #000000',
              }}
            >
              MASS: 6.2 KG | DENSITY: 19.84 g/cm³
            </span>
          </div>

          {/* Clean Vertical Divider */}
          <div
            style={{
              height: 28,
              width: 1,
              backgroundColor: 'rgba(255, 255, 255, 0.2)',
              margin: '0 8px',
            }}
          />

          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span
              style={{
                fontSize: 11,
                fontWeight: 800,
                color: '#94a3b8',
                letterSpacing: '0.14em',
                textTransform: 'uppercase',
                textShadow: '1px 1px 2px #000000',
              }}
            >
              NEON ATOM // EPISODE 03
            </span>
            <span
              style={{
                fontSize: 13,
                fontWeight: 900,
                color: '#ffffff',
                letterSpacing: '0.06em',
                textTransform: 'uppercase',
                textShadow: '2px 2px 4px #000000',
              }}
            >
              THE DEMON CORE
            </span>
          </div>
        </div>

        {/* Right: Real-time Era & Criticality Telemetry */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end' }}>
          <span
            style={{
              fontSize: 11,
              fontWeight: 800,
              color: '#94a3b8',
              letterSpacing: '0.12em',
              textTransform: 'uppercase',
              textShadow: '1px 1px 2px #000000',
            }}
          >
            LOCATION: {currentEra.location}
          </span>
          <span
            style={{
              fontSize: 14,
              fontWeight: 900,
              fontFamily: 'ui-monospace, "JetBrains Mono", monospace',
              color: currentEra.alertLevel === 'LETHAL' ? '#FF2244' : currentEra.accent,
              letterSpacing: '0.06em',
              textShadow: '2px 2px 4px #000000, 0 0 12px rgba(0, 0, 0, 0.9)',
              textTransform: 'uppercase',
            }}
          >
            STATE: {currentEra.condition} [{currentRadDisplay}]
          </span>
        </div>
      </div>

      {/* 6. HISTORICAL ERA TIMELINE RIBBON (1945-1946 Los Alamos / Crossroads Timeline) */}
      <div
        style={{
          position: 'absolute',
          top: 80,
          left: 50,
          right: 50,
          height: 38,
          zIndex: 14,
          pointerEvents: 'none',
        }}
      >
        {/* Base Timeline Track Line */}
        <div
          style={{
            position: 'absolute',
            top: 7,
            left: 0,
            right: 0,
            height: 2,
            backgroundColor: 'rgba(255, 255, 255, 0.15)',
          }}
        />

        {/* Active Timeline Progress Fill */}
        <div
          style={{
            position: 'absolute',
            top: 7,
            left: 0,
            width: `${progressPercent}%`,
            height: 2,
            background: `linear-gradient(to right, #FFB300, ${currentEra.accent})`,
            boxShadow: `0 0 8px ${currentEra.accent}`,
          }}
        />

        {/* 5 Historical Milestones */}
        {HISTORICAL_TIMELINE.map((m) => {
          const isActive = m.act === activeScene.act;
          const isPassed = frame >= m.endFrame;
          return (
            <div
              key={m.act}
              style={{
                position: 'absolute',
                left: `${m.percent}%`,
                top: 0,
                transform:
                  m.percent === 0
                    ? 'none'
                    : m.percent >= 80
                    ? 'translateX(-100%)'
                    : 'translateX(-50%)',
                display: 'flex',
                flexDirection: 'column',
                alignItems:
                  m.percent === 0
                    ? 'flex-start'
                    : m.percent >= 80
                    ? 'flex-end'
                    : 'center',
              }}
            >
              {/* Milestone Indicator Pip */}
              <div
                style={{
                  width: isActive ? 12 : isPassed ? 8 : 6,
                  height: isActive ? 12 : isPassed ? 8 : 6,
                  borderRadius: '50%',
                  backgroundColor: isActive
                    ? '#FFE600'
                    : isPassed
                    ? m.accent
                    : 'rgba(255, 255, 255, 0.25)',
                  boxShadow: isActive
                    ? '0 0 10px #FFE600, 0 0 20px rgba(255, 230, 0, 0.8)'
                    : isPassed
                    ? `0 0 6px ${m.accent}`
                    : 'none',
                  marginTop: isActive ? 2 : isPassed ? 4 : 5,
                  border: isActive ? '2px solid #FFFFFF' : 'none',
                }}
              />
              {/* Milestone Date & Name */}
              <span
                style={{
                  marginTop: 6,
                  fontSize: isActive ? 12 : 10,
                  fontWeight: isActive ? 900 : isPassed ? 700 : 600,
                  fontFamily: '"Montserrat", "Inter", sans-serif',
                  letterSpacing: '0.06em',
                  color: isActive
                    ? '#FFE600'
                    : isPassed
                    ? '#cbd5e1'
                    : 'rgba(255, 255, 255, 0.55)',
                  textTransform: 'uppercase',
                  textShadow: isActive
                    ? '2px 2px 4px #000000, 0 0 12px rgba(255, 230, 0, 0.9)'
                    : '1px 1px 0 #000000, -1px -1px 0 #000000, 1px -1px 0 #000000, -1px 1px 0 #000000, 0 2px 6px rgba(0, 0, 0, 0.95)',
                  whiteSpace: 'nowrap',
                }}
              >
                {m.label}
              </span>
            </div>
          );
        })}
      </div>

      {/* 7. LARGE PUNCHY EDITORIAL HEADLINE (Neon Rush / Quicksilver Impact Style - NO FIELDS) */}
      <div
        style={{
          position: 'absolute',
          top: 132,
          left: 50,
          zIndex: 15,
          opacity: headlineOpacity,
          transform: `translateY(${interpolate(headlineEntrance, [0, 1], [-16, 0])}px)`,
          pointerEvents: 'none',
        }}
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          {/* Category Tag directly on video */}
          <span
            style={{
              fontSize: 13,
              fontWeight: 800,
              letterSpacing: '0.14em',
              color: currentEra.accent,
              textTransform: 'uppercase',
              textShadow: '2px 2px 4px #000000',
            }}
          >
            ACT {activeScene.act}: {activeScene.act_title} // SCENE {activeScene.scene_id}
          </span>

          {/* Master Neon Rush Hook Headline */}
          <h1
            style={{
              margin: 0,
              fontSize: 54,
              fontWeight: 900,
              fontFamily: '"Impact", "Arial Black", "Montserrat", sans-serif',
              letterSpacing: '0.01em',
              lineHeight: 1.05,
              color: '#FFE600',
              WebkitTextStroke: '3px #000000',
              textShadow:
                '3px 3px 0 #000000, -3px -3px 0 #000000, 3px -3px 0 #000000, -3px 3px 0 #000000, 0 8px 24px rgba(0, 0, 0, 0.95)',
              textTransform: 'uppercase',
              maxWidth: 1050,
            }}
          >
            {activeScene.kinetic_hook_headline}
          </h1>
        </div>
      </div>

      {/* 8. HIGH-CONTRAST SUBTITLES DIRECTLY ON SCENE (Clean Typography - NO FIELDS) */}
      <div
        style={{
          position: 'absolute',
          bottom: 48,
          left: 70,
          right: 70,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 15,
          pointerEvents: 'none',
        }}
      >
        <p
          style={{
            margin: 0,
            maxWidth: 1420,
            fontSize: 32,
            fontWeight: 800,
            fontFamily: '"Montserrat", "Inter", -apple-system, sans-serif',
            lineHeight: 1.35,
            color: '#ffffff',
            textAlign: 'center',
            WebkitTextStroke: '2px #000000',
            textShadow:
              '2px 2px 0 #000000, -2px -2px 0 #000000, 2px -2px 0 #000000, -2px 2px 0 #000000, 0 6px 20px rgba(0, 0, 0, 0.95)',
            letterSpacing: '0.01em',
          }}
        >
          {activeScene.voiceover_text}
        </p>
      </div>

      {/* 9. MINIMALIST RUNNING PROGRESS BAR (Neon Rush Signature - Height 5px) */}
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
            background: `linear-gradient(to right, #FFB300, ${currentEra.accent})`,
            boxShadow: `0 0 10px ${currentEra.accent}`,
          }}
        />
      </div>

      {/* TIMECODE HUD (Bottom Right) */}
      <div
        style={{
          position: 'absolute',
          bottom: 12,
          right: 50,
          fontSize: 12,
          fontFamily: 'ui-monospace, "JetBrains Mono", monospace',
          color: '#94a3b8',
          letterSpacing: '0.1em',
          zIndex: 20,
          textShadow: '1px 1px 2px #000000',
        }}
      >
        {timecode} / 00:10:07:25
      </div>
    </div>
  );
};
