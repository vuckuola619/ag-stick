import React from 'react';
import {
  useCurrentFrame,
  interpolate,
  spring,
  useVideoConfig,
  Img,
  staticFile,
  Sequence,
} from 'remotion';

// Precise 8-Scene Storyboard Definition matching Audio Timestamps
export const SCENE_CONFIGS = [
  {
    id: 1,
    name: 'scene_01.png',
    startFrame: 0,
    duration: 120, // 0.0s - 4.0s
    caption: 'Bayangkan kamu adalah manusia purba 10.000 tahun lalu.',
    zoom: [1.0, 1.06],
    origin: 'center 40%',
  },
  {
    id: 2,
    name: 'scene_02.png',
    startFrame: 120,
    duration: 120, // 4.0s - 8.0s
    caption: 'Kamu menemukan sebuah batu kristal merah delima yang aneh di dalam gua gelap.',
    zoom: [1.02, 1.08],
    origin: '65% 50%',
  },
  {
    id: 3,
    name: 'scene_03.png',
    startFrame: 240,
    duration: 150, // 8.0s - 13.0s
    caption: 'Karena penasaran, kamu melemparkan batu merah itu ke dalam kobaran api unggun.',
    zoom: [1.0, 1.07],
    origin: 'center 75%',
  },
  {
    id: 4,
    name: 'scene_04.png',
    startFrame: 390,
    duration: 90, // 13.0s - 16.0s
    caption: 'Tiba-tiba hal mustahil terjadi! Batunya tidak hangus menjadi abu...',
    zoom: [1.03, 1.10],
    origin: 'center center',
  },
  {
    id: 5,
    name: 'scene_05.png',
    startFrame: 480,
    duration: 150, // 16.0s - 21.0s
    caption: 'Melainkan mulai berdarah cairan perak mengkilap yang menetes dan mengalir!',
    zoom: [1.05, 1.09],
    origin: 'center 60%',
  },
  {
    id: 6,
    name: 'scene_06.png',
    startFrame: 630,
    duration: 180, // 21.0s - 27.0s
    caption: 'Logam cair ini tidak membasahi kulitmu, memantul licin bagai cermin, dan sangat berat. Inilah merkuri!',
    zoom: [1.02, 1.08],
    origin: '50% 50%',
  },
  {
    id: 7,
    name: 'scene_07.png',
    startFrame: 810,
    duration: 300, // 27.0s - 37.0s
    caption: 'Batu merah tersebut adalah Cinabar (HgS). Panas di atas 357°C memecah kimianya, uapnya mengembun jadi air raksa.',
    zoom: [1.0, 1.07],
    origin: '55% 45%',
  },
  {
    id: 8,
    name: 'scene_08.png',
    startFrame: 1110,
    duration: 402, // 37.0s - 50.4s
    caption: 'Dari rasa penasaran manusia purba bermain api, lahirlah elemen paling mistis dalam sejarah peradaban!',
    zoom: [1.08, 1.0],
    origin: 'center center',
  },
];

export const MercurySceneRemakeComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Find active scene
  const activeScene =
    SCENE_CONFIGS.find(
      (s) => frame >= s.startFrame && frame < s.startFrame + s.duration
    ) || SCENE_CONFIGS[SCENE_CONFIGS.length - 1];

  // Dynamic Temperature ramp
  const temperature = interpolate(
    frame,
    [0, 240, 390, 480, 810, 1110, 1512],
    [25, 30, 210, 365, 380, 420, 25],
    { extrapolateRight: 'clamp' }
  );

  // Screen shake on dramatic moments (Scene 4-5)
  const isShake = frame >= 390 && frame < 540;
  const shakeX = isShake ? Math.sin(frame * 2.5) * 5 : 0;
  const shakeY = isShake ? Math.cos(frame * 2.0) * 4 : 0;

  // Global outro fade
  const outroFade = interpolate(frame, [1475, 1512], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'relative',
        width: 1920,
        height: 1080,
        overflow: 'hidden',
        backgroundColor: '#05070e',
        transform: `translate(${shakeX}px, ${shakeY}px)`,
        opacity: outroFade,
        fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
      }}
    >
      {/* 1. SCENE SEQUENCE WITH KEN BURNS CINEMATIC CAMERA */}
      {SCENE_CONFIGS.map((scene) => {
        return (
          <Sequence
            key={scene.id}
            from={scene.startFrame}
            durationInFrames={scene.duration}
          >
            <ScenePanel scene={scene} fps={fps} />
          </Sequence>
        );
      })}

      {/* 2. AMBIENT DRIFTING PARTICLES OVERLAY */}
      <div style={{ position: 'absolute', inset: 0, pointerEvents: 'none', zIndex: 10 }}>
        {Array.from({ length: 25 }).map((_, i) => {
          const speed = 0.5 + (i % 4) * 0.25;
          const y = (100 - ((frame * speed + i * 14) % 110));
          const x = (i * 39) % 100 + Math.sin(frame * 0.04 + i) * 8;
          const size = 2 + (i % 3);
          const opacity = Math.sin((y / 100) * Math.PI) * 0.7;
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: `${x}%`,
                top: `${y}%`,
                width: `${size}px`,
                height: `${size}px`,
                borderRadius: '50%',
                backgroundColor: i % 2 === 0 ? '#fbbf24' : '#f97316',
                boxShadow: '0 0 6px rgba(251, 191, 36, 0.8)',
                opacity,
              }}
            />
          );
        })}
      </div>

      {/* 3. CINEMATIC VIGNETTE */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'radial-gradient(ellipse at center, transparent 55%, rgba(0,0,0,0.55) 90%, rgba(0,0,0,0.85) 100%)',
          pointerEvents: 'none',
          zIndex: 12,
        }}
      />

      {/* 4. TOP HUD (Pill topic + Temperature Gauge) */}
      <div
        style={{
          position: 'absolute',
          top: '36px',
          left: '50px',
          right: '50px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 20,
          pointerEvents: 'none',
        }}
      >
        {/* Topic Badge */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            backgroundColor: 'rgba(15, 23, 42, 0.85)',
            backdropFilter: 'blur(12px)',
            border: '1.5px solid rgba(251, 191, 36, 0.5)',
            borderRadius: '999px',
            padding: '8px 20px',
            boxShadow: '0 8px 24px rgba(0,0,0,0.5)',
          }}
        >
          <div
            style={{
              width: '10px',
              height: '10px',
              borderRadius: '50%',
              backgroundColor: '#ef4444',
              boxShadow: '0 0 10px #ef4444',
            }}
          />
          <span
            style={{
              color: '#fbbf24',
              fontWeight: 800,
              fontSize: '15px',
              letterSpacing: '0.08em',
              textTransform: 'uppercase',
            }}
          >
            NEON RUSH REMAKE // AIR RAKSA
          </span>
        </div>

        {/* Dynamic Temperature Meter */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            backgroundColor:
              temperature >= 357
                ? 'rgba(239, 68, 68, 0.35)'
                : 'rgba(15, 23, 42, 0.85)',
            backdropFilter: 'blur(12px)',
            border: `1.5px solid ${temperature >= 357 ? '#ef4444' : 'rgba(148, 163, 184, 0.4)'}`,
            borderRadius: '12px',
            padding: '8px 18px',
            boxShadow: '0 8px 24px rgba(0,0,0,0.5)',
          }}
        >
          <span style={{ fontSize: '18px' }}>🔥</span>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span
              style={{
                color: temperature >= 357 ? '#fca5a5' : '#94a3b8',
                fontSize: '10px',
                fontWeight: 600,
                letterSpacing: '0.05em',
                textTransform: 'uppercase',
              }}
            >
              Suhu Api Unggun
            </span>
            <span
              style={{
                color: temperature >= 357 ? '#ef4444' : '#f8fafc',
                fontSize: '20px',
                fontWeight: 900,
                fontFamily: 'monospace',
              }}
            >
              {Math.round(temperature)}°C
            </span>
          </div>
        </div>
      </div>

      {/* 5. DYNAMIC CALLOUT BADGES */}
      {/* Scene 1: Main Title */}
      {frame >= 10 && frame < 115 && (
        <div
          style={{
            position: 'absolute',
            top: '120px',
            left: '50%',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 10, fps, config: { damping: 12 } })})`,
            textAlign: 'center',
            zIndex: 25,
            pointerEvents: 'none',
          }}
        >
          <h1
            style={{
              color: '#ffffff',
              fontSize: '52px',
              fontWeight: 900,
              margin: 0,
              textShadow:
                '0 8px 30px rgba(0,0,0,0.9), 0 0 25px rgba(239, 68, 68, 0.5)',
              lineHeight: 1.15,
            }}
          >
            BAGAIMANA MANUSIA MENEMUKAN <br />
            <span
              style={{
                color: '#38bdf8',
                textShadow: '0 0 25px rgba(56, 189, 248, 0.8)',
              }}
            >
              AIR RAKSA (QUICKSILVER)?
            </span>
          </h1>
        </div>
      )}

      {/* Scene 4: Boiling Point Alert */}
      {frame >= 395 && frame < 475 && (
        <div
          style={{
            position: 'absolute',
            top: '130px',
            left: '50%',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 395, fps, config: { damping: 10 } })})`,
            backgroundColor: 'rgba(239, 68, 68, 0.9)',
            border: '2px solid #ffffff',
            borderRadius: '12px',
            padding: '10px 24px',
            color: '#ffffff',
            fontWeight: 900,
            fontSize: '22px',
            letterSpacing: '0.08em',
            boxShadow: '0 8px 30px rgba(239, 68, 68, 0.7)',
            zIndex: 25,
          }}
        >
          ⚠️ TITIK DIDIH TERCAPAI: 357°C ⚠️
        </div>
      )}

      {/* Scene 6: Physics Badges */}
      {frame >= 640 && frame < 800 && (
        <div
          style={{
            position: 'absolute',
            right: '60px',
            top: '160px',
            display: 'flex',
            flexDirection: 'column',
            gap: '14px',
            zIndex: 25,
            pointerEvents: 'none',
          }}
        >
          {[
            { icon: '💧', label: 'TIDAK MEMBASAHI BATU', sub: 'Tegangan permukaan ekstrim' },
            { icon: '🪞', label: 'MEMANTUL SEPERTI CERMIN', sub: 'Reflektansi logam 100%' },
            { icon: '⚖️', label: 'DENSITAS 13.5x AIR', sub: 'Sangat padat & berat' },
          ].map((b, idx) => {
            const bSpring = spring({
              frame: Math.max(0, frame - 640 - idx * 25),
              fps,
              config: { damping: 12 },
            });
            return (
              <div
                key={idx}
                style={{
                  transform: `scale(${bSpring})`,
                  backgroundColor: 'rgba(15, 23, 42, 0.92)',
                  border: '2px solid #38bdf8',
                  borderRadius: '14px',
                  padding: '12px 20px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '14px',
                  boxShadow: '0 10px 25px rgba(0,0,0,0.7)',
                  width: '340px',
                }}
              >
                <span style={{ fontSize: '28px' }}>{b.icon}</span>
                <div>
                  <div style={{ color: '#38bdf8', fontWeight: 800, fontSize: '15px' }}>
                    {b.label}
                  </div>
                  <div style={{ color: '#94a3b8', fontSize: '12px', fontWeight: 500 }}>
                    {b.sub}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Scene 7: Chemical Formula */}
      {frame >= 825 && frame < 1100 && (
        <div
          style={{
            position: 'absolute',
            top: '130px',
            left: '50%',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 825, fps, config: { damping: 12 } })})`,
            backgroundColor: 'rgba(15, 23, 42, 0.92)',
            border: '2px solid #38bdf8',
            borderRadius: '16px',
            padding: '14px 32px',
            boxShadow: '0 10px 30px rgba(56, 189, 248, 0.3)',
            zIndex: 25,
          }}
        >
          <div style={{ color: '#38bdf8', fontSize: '11px', fontWeight: 800, letterSpacing: '0.12em', textAlign: 'center', marginBottom: '4px' }}>
            REAKSI TERMAL ALKIMIA
          </div>
          <div style={{ color: '#ffffff', fontSize: '22px', fontWeight: 900, fontFamily: 'monospace' }}>
            <span style={{ color: '#ef4444' }}>HgS (Cinabar)</span> + <span style={{ color: '#fbbf24' }}>Kalor (&gt;357°C)</span> ➔ <span style={{ color: '#38bdf8' }}>Hg (Merkuri)</span> + SO₂
          </div>
        </div>
      )}

      {/* 6. BOTTOM KINETIC CAPTIONS */}
      <div
        style={{
          position: 'absolute',
          bottom: '36px',
          left: '50%',
          transform: 'translateX(-50%)',
          width: '85%',
          display: 'flex',
          justifyContent: 'center',
          zIndex: 30,
          pointerEvents: 'none',
        }}
      >
        <div
          style={{
            backgroundColor: 'rgba(10, 15, 30, 0.9)',
            backdropFilter: 'blur(16px)',
            border: '2px solid #fbbf24',
            borderRadius: '16px',
            padding: '14px 36px',
            textAlign: 'center',
            boxShadow: '0 12px 36px rgba(0,0,0,0.85), 0 0 20px rgba(251, 191, 36, 0.25)',
          }}
        >
          <span
            style={{
              color: '#ffffff',
              fontSize: '28px',
              fontWeight: 900,
              lineHeight: 1.35,
              letterSpacing: '0.02em',
              textShadow: '0 2px 6px rgba(0,0,0,0.9)',
            }}
          >
            {activeScene.caption}
          </span>
        </div>
      </div>
    </div>
  );
};

// Sub-component: Scene Panel with Ken Burns Slow Zoom
const ScenePanel: React.FC<{ scene: (typeof SCENE_CONFIGS)[0]; fps: number }> = ({
  scene,
  fps,
}) => {
  const frame = useCurrentFrame();

  const scale = interpolate(
    frame,
    [0, scene.duration],
    [scene.zoom[0], scene.zoom[1]],
    { extrapolateRight: 'clamp' }
  );

  // Soft crossfade-in on transition
  const fadeIn = interpolate(frame, [0, 8], [0.85, 1], {
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        overflow: 'hidden',
        opacity: fadeIn,
      }}
    >
      <Img
        src={staticFile(`assets/scenes/${scene.name}`)}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transform: `scale(${scale})`,
          transformOrigin: scene.origin,
        }}
      />
    </div>
  );
};
