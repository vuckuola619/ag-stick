import React from 'react';

export const GridBlueprintBackground: React.FC = () => {
  return (
    <div
      style={{
        position: 'absolute',
        width: '100%',
        height: '100%',
        backgroundColor: '#090d16',
        overflow: 'hidden',
      }}
    >
      {/* Blueprint Technical Dot Grid */}
      <svg
        width="100%"
        height="100%"
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          opacity: 0.25,
        }}
      >
        <defs>
          <pattern
            id="grid-dots"
            x="0"
            y="0"
            width="40"
            height="40"
            patternUnits="userSpaceOnUse"
          >
            <circle cx="20" cy="20" r="1.5" fill="#38bdf8" />
          </pattern>
          <pattern
            id="grid-lines"
            x="0"
            y="0"
            width="200"
            height="200"
            patternUnits="userSpaceOnUse"
          >
            <path
              d="M 200 0 L 0 0 0 200"
              fill="none"
              stroke="#1e293b"
              strokeWidth="1"
            />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid-lines)" />
        <rect width="100%" height="100%" fill="url(#grid-dots)" />
      </svg>

      {/* Vignette & Soft Center Glow */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          background:
            'radial-gradient(ellipse at center, rgba(30, 58, 138, 0.15) 0%, rgba(9, 13, 22, 0.85) 75%, #090d16 100%)',
          pointerEvents: 'none',
        }}
      />
    </div>
  );
};
