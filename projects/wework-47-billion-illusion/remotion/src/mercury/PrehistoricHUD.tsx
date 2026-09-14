import React from 'react';
import { useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';

export interface PrehistoricHUDProps {
  temperature?: number;
  showReactionBadge?: boolean;
  currentCaption?: string;
  isTikTok?: boolean;
}

export const PrehistoricHUD: React.FC<PrehistoricHUDProps> = ({
  temperature = 25,
  showReactionBadge = false,
  currentCaption = '',
  isTikTok = false,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const tempClamped = Math.min(420, Math.max(25, temperature));
  const isBoiling = tempClamped >= 357;

  // Pulse if boiling point reached
  const alertPulse = isBoiling ? 0.7 + 0.3 * Math.sin(frame * 0.4) : 1.0;

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        pointerEvents: 'none',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        padding: isTikTok ? '60px 40px' : '40px 60px',
        fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
      }}
    >
      {/* Top Header Bar */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          width: '100%',
        }}
      >
        {/* Channel & Topic Badge */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            backgroundColor: 'rgba(15, 23, 42, 0.75)',
            backdropFilter: 'blur(12px)',
            border: '1.5px solid rgba(251, 191, 36, 0.4)',
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
              fontSize: isTikTok ? '16px' : '15px',
              letterSpacing: '0.08em',
              textTransform: 'uppercase',
            }}
          >
            Sains Purba // Misteri Merkuri
          </span>
        </div>

        {/* Live Temperature Gauge */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            backgroundColor: isBoiling
              ? `rgba(239, 68, 68, ${alertPulse * 0.3})`
              : 'rgba(15, 23, 42, 0.75)',
            backdropFilter: 'blur(12px)',
            border: `1.5px solid ${isBoiling ? '#ef4444' : 'rgba(148, 163, 184, 0.3)'}`,
            borderRadius: '12px',
            padding: '8px 18px',
            boxShadow: '0 8px 24px rgba(0,0,0,0.5)',
            transition: 'all 0.2s ease',
          }}
        >
          <span style={{ fontSize: '18px' }}>🔥</span>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span
              style={{
                color: isBoiling ? '#fca5a5' : '#94a3b8',
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
                color: isBoiling ? '#ef4444' : '#f8fafc',
                fontSize: '20px',
                fontWeight: 900,
                fontFamily: 'monospace',
              }}
            >
              {Math.round(tempClamped)}°C
            </span>
          </div>
        </div>
      </div>

      {/* Center Reaction HUD (When Stone is Broken Down) */}
      {showReactionBadge && (
        <div
          style={{
            alignSelf: 'center',
            backgroundColor: 'rgba(15, 23, 42, 0.88)',
            backdropFilter: 'blur(16px)',
            border: '2px solid #38bdf8',
            borderRadius: '16px',
            padding: '16px 28px',
            boxShadow: '0 12px 32px rgba(56, 189, 248, 0.25)',
            textAlign: 'center',
            transform: `scale(${1 + 0.02 * Math.sin(frame * 0.2)})`,
          }}
        >
          <div
            style={{
              color: '#38bdf8',
              fontSize: '12px',
              fontWeight: 700,
              letterSpacing: '0.12em',
              textTransform: 'uppercase',
              marginBottom: '6px',
            }}
          >
            ⚡ Reaksi Termokimia Purba
          </div>
          <div
            style={{
              color: '#f8fafc',
              fontSize: isTikTok ? '20px' : '24px',
              fontWeight: 800,
              fontFamily: 'monospace',
            }}
          >
            <span style={{ color: '#ef4444' }}>HgS (Cinabar)</span>
            {' + '}
            <span style={{ color: '#f59e0b' }}>Kalor (&gt;357°C)</span>
            {' ➔ '}
            <span style={{ color: '#38bdf8', textShadow: '0 0 12px #38bdf8' }}>
              Hg (Perak Cair)
            </span>
            {' + SO₂'}
          </div>
        </div>
      )}

      {/* Bottom Kinetic Captions */}
      <div
        style={{
          width: '100%',
          display: 'flex',
          justifyContent: 'center',
          marginBottom: isTikTok ? '180px' : '20px',
        }}
      >
        {currentCaption && (
          <div
            style={{
              maxWidth: isTikTok ? '92%' : '85%',
              backgroundColor: 'rgba(10, 15, 30, 0.88)',
              backdropFilter: 'blur(12px)',
              border: '2px solid #fbbf24',
              borderRadius: '16px',
              padding: isTikTok ? '18px 24px' : '16px 36px',
              textAlign: 'center',
              boxShadow: '0 10px 30px rgba(0,0,0,0.8), 0 0 15px rgba(251, 191, 36, 0.25)',
            }}
          >
            <span
              style={{
                color: '#ffffff',
                fontSize: isTikTok ? '28px' : '32px',
                fontWeight: 900,
                lineHeight: 1.35,
                letterSpacing: '0.02em',
                textShadow: '0 2px 4px rgba(0,0,0,0.8)',
              }}
            >
              {currentCaption}
            </span>
          </div>
        )}
      </div>
    </div>
  );
};
