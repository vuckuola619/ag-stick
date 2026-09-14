import React, { useMemo } from 'react';
import { useCurrentFrame, interpolate } from 'remotion';

export interface MercuryCaveBackgroundProps {
  intensity?: number;
  fireActive?: boolean;
}

export const MercuryCaveBackground: React.FC<MercuryCaveBackgroundProps> = ({
  intensity = 1.0,
  fireActive = true,
}) => {
  const frame = useCurrentFrame();

  // Campfire warm light harmonic flicker
  const flicker1 = Math.sin(frame / 6) * 0.12;
  const flicker2 = Math.cos(frame / 11) * 0.08;
  const flicker3 = Math.sin(frame / 17 + 2) * 0.05;
  const fireGlowOpacity = fireActive ? Math.max(0.2, Math.min(0.85, (0.55 + flicker1 + flicker2 + flicker3) * intensity)) : 0.15;

  // Floating embers and ash particles
  const emberParticles = useMemo(() => {
    return Array.from({ length: 30 }).map((_, i) => ({
      id: i,
      x: (i * 37) % 100, // percentage width
      startY: 70 + (i % 25), // start near bottom
      size: 2 + (i % 4),
      speed: 0.6 + ((i % 5) * 0.25),
      sway: 8 + (i % 12),
      phase: i * 1.7,
      color: i % 3 === 0 ? '#fbbf24' : i % 3 === 1 ? '#f97316' : '#ef4444',
    }));
  }, []);

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        overflow: 'hidden',
        backgroundColor: '#070913',
        fontFamily: 'Inter, system-ui, sans-serif',
      }}
    >
      {/* 1. Base Cave Wall Rock Texture & Gradient Mesh */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `
            radial-gradient(circle at 50% 65%, rgba(45, 22, 12, 0.45) 0%, rgba(18, 12, 22, 0.7) 45%, rgba(6, 8, 16, 0.95) 85%),
            linear-gradient(180deg, #05070e 0%, #110d18 50%, #060810 100%)
          `,
        }}
      />

      {/* 2. Volumetric Campfire Spotlight Glow */}
      <div
        style={{
          position: 'absolute',
          bottom: '-10%',
          left: '50%',
          width: '1400px',
          height: '900px',
          transform: 'translateX(-50%)',
          borderRadius: '50%',
          background: `radial-gradient(ellipse at center, rgba(249, 115, 22, ${fireGlowOpacity * 0.7}) 0%, rgba(234, 179, 8, ${fireGlowOpacity * 0.35}) 35%, rgba(239, 68, 68, ${fireGlowOpacity * 0.15}) 60%, transparent 80%)`,
          filter: 'blur(60px)',
          pointerEvents: 'none',
          transition: 'opacity 0.2s ease',
        }}
      />

      {/* 3. Prehistoric Cave Art Petroglyphs (Silhouette SVGs) */}
      <svg
        style={{
          position: 'absolute',
          inset: 0,
          width: '100%',
          height: '100%',
          opacity: 0.14,
          pointerEvents: 'none',
        }}
        viewBox="0 0 1920 1080"
        fill="none"
      >
        {/* Cave Bison / Mammoth Left */}
        <path
          d="M 220 320 Q 260 270 340 280 Q 400 290 440 340 Q 450 370 420 410 Q 370 440 310 430 Q 250 420 220 380 Z"
          stroke="#f59e0b"
          strokeWidth="3.5"
          fill="none"
          strokeLinecap="round"
        />
        <path d="M 240 380 L 230 460 M 270 390 L 260 470 M 380 400 L 390 480 M 410 380 L 430 470" stroke="#f59e0b" strokeWidth="3" strokeLinecap="round" />
        <path d="M 220 320 Q 180 340 160 380 Q 150 410 180 400" stroke="#f59e0b" strokeWidth="3.5" fill="none" strokeLinecap="round" />

        {/* Prehistoric Handprint Stencil Center-Left */}
        <g transform="translate(480, 220) scale(0.6)" stroke="#ef4444" strokeWidth="4" fill="rgba(239,68,68,0.15)" strokeLinecap="round" strokeLinejoin="round">
          <path d="M 50 140 C 30 110 20 80 25 50 C 30 20 45 20 50 50 L 52 80 M 55 75 L 55 30 C 55 10 70 10 70 30 L 70 80 M 75 75 L 75 25 C 75 5 90 5 90 25 L 90 85 M 95 85 L 105 45 C 110 30 125 35 120 55 L 110 110 C 105 140 85 160 50 160 Z" />
        </g>

        {/* Prehistoric Running Hunter Stickman Right */}
        <g transform="translate(1500, 280) scale(0.9)" stroke="#fbbf24" strokeWidth="4" fill="none" strokeLinecap="round">
          <circle cx="50" cy="30" r="14" fill="#fbbf24" fillOpacity="0.2" />
          <line x1="50" y1="44" x2="50" y2="90" />
          <line x1="50" y1="58" x2="20" y2="40" />
          <line x1="20" y1="40" x2="5" y2="20" />
          <line x1="50" y1="58" x2="80" y2="70" />
          <line x1="80" y1="70" x2="110" y2="60" />
          {/* Spear */}
          <line x1="5" y1="15" x2="130" y2="68" stroke="#ef4444" strokeWidth="3" />
          <line x1="50" y1="90" x2="20" y2="135" />
          <line x1="50" y1="90" x2="85" y2="130" />
        </g>
      </svg>

      {/* 4. Drifting Fire Embers & Ash Particles */}
      {fireActive && (
        <div style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
          {emberParticles.map((p) => {
            const age = (frame * p.speed + p.phase * 20) % 180;
            const progress = age / 180; // 0 to 1
            const y = interpolate(progress, [0, 1], [p.startY, 10]);
            const xSway = Math.sin(frame * 0.05 + p.phase) * p.sway;
            const opacity = interpolate(progress, [0, 0.2, 0.8, 1], [0, 0.9, 0.7, 0]);

            return (
              <div
                key={p.id}
                style={{
                  position: 'absolute',
                  left: `calc(${p.x}% + ${xSway}px)`,
                  top: `${y}%`,
                  width: `${p.size}px`,
                  height: `${p.size}px`,
                  borderRadius: '50%',
                  backgroundColor: p.color,
                  boxShadow: `0 0 8px ${p.color}`,
                  opacity,
                }}
              />
            );
          })}
        </div>
      )}

      {/* 5. Cinematic Vignette Falloff */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'radial-gradient(ellipse at 50% 50%, transparent 45%, rgba(0,0,0,0.65) 90%, rgba(0,0,0,0.92) 100%)',
          pointerEvents: 'none',
        }}
      />
    </div>
  );
};
