import React from 'react';
import { useCurrentFrame, spring, useVideoConfig } from 'remotion';

export interface MemeDevQuoteProps {
  quote: string;
  author: string;
  variant?: 'junior' | 'senior' | 'cto' | 'panic';
}

export const MemeDevQuote: React.FC<MemeDevQuoteProps> = ({
  quote,
  author,
  variant = 'junior',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame,
    fps,
    config: { damping: 12, stiffness: 160 },
  });

  const colors = {
    junior: { bg: 'rgba(30, 27, 75, 0.95)', border: '#818cf8', text: '#ffffff', badge: '#4338ca', glow: 'rgba(129, 140, 248, 0.4)' },
    senior: { bg: 'rgba(6, 78, 59, 0.95)', border: '#34d399', text: '#ffffff', badge: '#065f46', glow: 'rgba(52, 211, 153, 0.4)' },
    cto: { bg: 'rgba(120, 53, 15, 0.95)', border: '#fbbf24', text: '#ffffff', badge: '#92400e', glow: 'rgba(251, 191, 36, 0.4)' },
    panic: { bg: 'rgba(127, 29, 29, 0.95)', border: '#f87171', text: '#ffffff', badge: '#991b1b', glow: 'rgba(248, 113, 113, 0.5)' },
  }[variant];

  return (
    <div
      style={{
        backgroundColor: colors.bg,
        border: `2.5px solid ${colors.border}`,
        borderRadius: '14px',
        padding: '14px 20px',
        maxWidth: '440px',
        boxShadow: `0 14px 35px rgba(0,0,0,0.75), 0 0 20px ${colors.glow}`,
        transform: `scale(${entrance})`,
        transformOrigin: 'bottom left',
        position: 'relative',
        fontFamily: 'Inter, system-ui, sans-serif',
        backdropFilter: 'blur(16px)',
      }}
    >
      {/* Speech Bubble Arrow */}
      <div
        style={{
          position: 'absolute',
          bottom: '-10px',
          left: '26px',
          width: '18px',
          height: '18px',
          backgroundColor: colors.bg,
          borderBottom: `2.5px solid ${colors.border}`,
          borderRight: `2.5px solid ${colors.border}`,
          transform: 'rotate(45deg)',
        }}
      />

      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
        <span
          style={{
            backgroundColor: colors.badge,
            color: '#f8fafc',
            fontSize: '13px',
            fontWeight: 900,
            padding: '3px 10px',
            borderRadius: '6px',
            letterSpacing: '0.06em',
            textTransform: 'uppercase',
            boxShadow: '0 2px 8px rgba(0,0,0,0.4)',
          }}
        >
          {author}
        </span>
      </div>

      <div
        style={{
          color: colors.text,
          fontSize: '20px',
          fontWeight: 800,
          lineHeight: '1.35',
          fontStyle: 'italic',
          textShadow: '0 2px 10px rgba(0,0,0,0.8)',
        }}
      >
        "{quote}"
      </div>
    </div>
  );
};
