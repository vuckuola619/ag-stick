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
import { SCENE_CONFIGS } from './MercurySceneRemakeComposition';

export const MercurySceneTikTokComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const activeScene =
    SCENE_CONFIGS.find(
      (s) => frame >= s.startFrame && frame < s.startFrame + s.duration
    ) || SCENE_CONFIGS[SCENE_CONFIGS.length - 1];

  const temperature = interpolate(
    frame,
    [0, 240, 390, 480, 810, 1110, 1512],
    [25, 30, 210, 365, 380, 420, 25],
    { extrapolateRight: 'clamp' }
  );

  const isShake = frame >= 390 && frame < 540;
  const shakeX = isShake ? Math.sin(frame * 2.5) * 8 : 0;
  const shakeY = isShake ? Math.cos(frame * 2.0) * 6 : 0;

  const outroFade = interpolate(frame, [1475, 1512], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'relative',
        width: 1080,
        height: 1920,
        overflow: 'hidden',
        backgroundColor: '#05070e',
        transform: `translate(${shakeX}px, ${shakeY}px)`,
        opacity: outroFade,
        fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
      }}
    >
      {/* 1. SCENE SEQUENCE */}
      {SCENE_CONFIGS.map((scene) => {
        return (
          <Sequence
            key={scene.id}
            from={scene.startFrame}
            durationInFrames={scene.duration}
          >
            <ScenePanelVertical scene={scene} fps={fps} />
          </Sequence>
        );
      })}

      {/* 2. AMBIENT PARTICLES OVERLAY */}
      <div style={{ position: 'absolute', inset: 0, pointerEvents: 'none', zIndex: 10 }}>
        {Array.from({ length: 30 }).map((_, i) => {
          const speed = 0.6 + (i % 4) * 0.3;
          const y = (100 - ((frame * speed + i * 14) % 110));
          const x = (i * 39) % 100 + Math.sin(frame * 0.04 + i) * 10;
          const size = 3 + (i % 4);
          const opacity = Math.sin((y / 100) * Math.PI) * 0.8;
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
                boxShadow: '0 0 8px rgba(251, 191, 36, 0.9)',
                opacity,
              }}
            />
          );
        })}
      </div>

      {/* 3. VIGNETTE OVERLAY */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'radial-gradient(ellipse at center, transparent 40%, rgba(0,0,0,0.65) 85%, rgba(0,0,0,0.92) 100%)',
          pointerEvents: 'none',
          zIndex: 12,
        }}
      />

      {/* 4. TOP HUD (Pill topic + Temperature Gauge) */}
      <div
        style={{
          position: 'absolute',
          top: '80px',
          left: '40px',
          right: '40px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 20,
          pointerEvents: 'none',
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            backgroundColor: 'rgba(15, 23, 42, 0.9)',
            backdropFilter: 'blur(12px)',
            border: '1.5px solid rgba(251, 191, 36, 0.6)',
            borderRadius: '999px',
            padding: '8px 18px',
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
            Misteri Air Raksa
          </span>
        </div>

        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            backgroundColor:
              temperature >= 357
                ? 'rgba(239, 68, 68, 0.45)'
                : 'rgba(15, 23, 42, 0.9)',
            backdropFilter: 'blur(12px)',
            border: `1.5px solid ${temperature >= 357 ? '#ef4444' : 'rgba(148, 163, 184, 0.4)'}`,
            borderRadius: '12px',
            padding: '8px 16px',
          }}
        >
          <span style={{ fontSize: '18px' }}>🔥</span>
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

      {/* 5. TITLES & BADGES */}
      {frame >= 10 && frame < 115 && (
        <div
          style={{
            position: 'absolute',
            top: '200px',
            left: '50%',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 10, fps, config: { damping: 12 } })})`,
            textAlign: 'center',
            width: '90%',
            zIndex: 25,
          }}
        >
          <h1
            style={{
              color: '#ffffff',
              fontSize: '56px',
              fontWeight: 900,
              margin: 0,
              textShadow:
                '0 8px 30px rgba(0,0,0,0.9), 0 0 25px rgba(239, 68, 68, 0.6)',
              lineHeight: 1.15,
            }}
          >
            BAGAIMANA MANUSIA MENEMUKAN <br />
            <span style={{ color: '#38bdf8', textShadow: '0 0 25px rgba(56, 189, 248, 0.9)' }}>
              AIR RAKSA?
            </span>
          </h1>
        </div>
      )}

      {/* 6. BOTTOM KINETIC CAPTIONS */}
      <div
        style={{
          position: 'absolute',
          bottom: '160px',
          left: '50%',
          transform: 'translateX(-50%)',
          width: '90%',
          display: 'flex',
          justifyContent: 'center',
          zIndex: 30,
          pointerEvents: 'none',
        }}
      >
        <div
          style={{
            backgroundColor: 'rgba(10, 15, 30, 0.92)',
            backdropFilter: 'blur(16px)',
            border: '2px solid #fbbf24',
            borderRadius: '18px',
            padding: '18px 28px',
            textAlign: 'center',
            boxShadow: '0 12px 36px rgba(0,0,0,0.9), 0 0 20px rgba(251, 191, 36, 0.3)',
          }}
        >
          <span
            style={{
              color: '#ffffff',
              fontSize: '32px',
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

const ScenePanelVertical: React.FC<{
  scene: (typeof SCENE_CONFIGS)[0];
  fps: number;
}> = ({ scene, fps }) => {
  const frame = useCurrentFrame();

  const scale = interpolate(
    frame,
    [0, scene.duration],
    [scene.zoom[0] * 1.05, scene.zoom[1] * 1.05],
    { extrapolateRight: 'clamp' }
  );

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        overflow: 'hidden',
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
