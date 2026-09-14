import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';

export interface TCPSocketGaugeProps {
  currentSockets: number;
  maxSockets?: number;
  label?: string;
  isPeak?: boolean;
}

export const TCPSocketGauge: React.FC<TCPSocketGaugeProps> = ({
  currentSockets,
  maxSockets = 3000000,
  label = 'FREEBSD TCP SOCKETS',
  isPeak = false,
}) => {
  const frame = useCurrentFrame();
  const percent = Math.min(100, (currentSockets / maxSockets) * 100);
  const pulse = Math.sin(frame * 0.2) * 0.15 + 0.85;

  return (
    <div
      style={{
        backgroundColor: 'rgba(15, 23, 42, 0.95)',
        border: isPeak ? '2.5px solid #25d366' : '2px solid rgba(56, 189, 248, 0.5)',
        borderRadius: '20px',
        padding: '20px 24px',
        boxShadow: isPeak
          ? '0 0 40px rgba(37, 211, 102, 0.4), 0 16px 32px rgba(0,0,0,0.8)'
          : '0 12px 30px rgba(0,0,0,0.7)',
        backdropFilter: 'blur(16px)',
        minWidth: '320px',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <div
            style={{
              width: '10px',
              height: '10px',
              borderRadius: '50%',
              backgroundColor: isPeak ? '#25d366' : '#38bdf8',
              boxShadow: `0 0 10px ${isPeak ? '#25d366' : '#38bdf8'}`,
            }}
          />
          <span style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800, letterSpacing: '0.08em' }}>
            {label}
          </span>
        </div>
        <span
          style={{
            backgroundColor: isPeak ? 'rgba(37, 211, 102, 0.2)' : 'rgba(56, 189, 248, 0.15)',
            color: isPeak ? '#4ade80' : '#38bdf8',
            fontSize: '11px',
            fontWeight: 800,
            padding: '3px 8px',
            borderRadius: '8px',
          }}
        >
          {isPeak ? '⚡ C2M SOLVED' : 'ACTIVE'}
        </span>
      </div>

      {/* Main Big Metric */}
      <div style={{ display: 'flex', alignItems: 'baseline', gap: '6px', marginBottom: '10px' }}>
        <div
          style={{
            color: isPeak ? '#25d366' : '#38bdf8',
            fontSize: '38px',
            fontWeight: 900,
            fontFamily: 'monospace',
            letterSpacing: '-0.02em',
            textShadow: isPeak ? '0 0 20px rgba(37, 211, 102, 0.6)' : 'none',
          }}
        >
          {Math.floor(currentSockets).toLocaleString()}
        </div>
        <span style={{ color: '#64748b', fontSize: '14px', fontWeight: 700 }}>
          / 1 Box
        </span>
      </div>

      {/* Meter Bar */}
      <div
        style={{
          width: '100%',
          height: '10px',
          backgroundColor: '#1e293b',
          borderRadius: '5px',
          overflow: 'hidden',
          marginBottom: '10px',
        }}
      >
        <div
          style={{
            width: `${percent}%`,
            height: '100%',
            background: isPeak
              ? 'linear-gradient(90deg, #38bdf8 0%, #25d366 100%)'
              : 'linear-gradient(90deg, #0284c7 0%, #38bdf8 100%)',
            borderRadius: '5px',
            transition: 'width 0.2s ease',
            boxShadow: isPeak ? '0 0 12px #25d366' : 'none',
          }}
        />
      </div>

      {/* Hardware Specs Footnote */}
      <div style={{ display: 'flex', justifyContent: 'space-between', color: '#64748b', fontSize: '11.5px', fontWeight: 600 }}>
        <span>FreeBSD 9.2 // Dual Xeon</span>
        <span style={{ color: isPeak ? '#86efac' : '#94a3b8' }}>~2.5 KB RAM / Conn</span>
      </div>
    </div>
  );
};
