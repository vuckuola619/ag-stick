import React from 'react';
import { useCurrentFrame, spring, useVideoConfig } from 'remotion';

export type SystemNodeType =
  | 'Client'
  | 'DNS'
  | 'CDN'
  | 'LoadBalancer'
  | 'WebServer'
  | 'Database'
  | 'Cache'
  | 'MessageQueue';

export interface SystemNodeV2Props {
  type: SystemNodeType;
  title: string;
  tech?: string;
  status?: 'healthy' | 'warning' | 'overload' | 'offline';
  cpuPercent?: number;
  scaleCount?: string;
  width?: number;
  height?: number;
  speedTag?: string;
  isMonolith?: boolean;
}

export const SystemNodeV2: React.FC<SystemNodeV2Props> = ({
  type,
  title,
  tech,
  status = 'healthy',
  cpuPercent,
  scaleCount,
  width = 300,
  height = 165,
  speedTag,
  isMonolith = false,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const colors = {
    healthy: {
      border: 'rgba(56, 189, 248, 0.65)',
      glow: 'rgba(56, 189, 248, 0.35)',
      badgeBg: 'rgba(12, 74, 110, 0.85)',
      badgeBorder: '#0284c7',
      accent: '#38bdf8',
      led: '#22c55e',
    },
    warning: {
      border: 'rgba(245, 158, 11, 0.85)',
      glow: 'rgba(245, 158, 11, 0.45)',
      badgeBg: 'rgba(120, 53, 15, 0.85)',
      badgeBorder: '#d97706',
      accent: '#fbbf24',
      led: '#f59e0b',
    },
    overload: {
      border: 'rgba(239, 68, 68, 0.95)',
      glow: 'rgba(239, 68, 68, 0.7)',
      badgeBg: 'rgba(127, 29, 29, 0.9)',
      badgeBorder: '#ef4444',
      accent: '#f87171',
      led: '#ef4444',
    },
    offline: {
      border: 'rgba(100, 116, 139, 0.5)',
      glow: 'rgba(100, 116, 139, 0.2)',
      badgeBg: 'rgba(30, 41, 59, 0.8)',
      badgeBorder: '#475569',
      accent: '#94a3b8',
      led: '#64748b',
    },
  }[status];

  const panicShake = status === 'overload' ? Math.sin(frame * 2.2) * 4 : 0;
  const floatBob = Math.sin(frame / 8) * 2;

  const entrance = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120 },
  });

  const ledBlink1 = Math.sin(frame * 0.8) > 0 ? 1 : 0.3;
  const ledBlink2 = Math.cos(frame * 1.1) > 0 ? 1 : 0.2;
  const ledBlink3 = Math.sin(frame * 1.5) > 0 ? 1 : 0.4;

  const showMonolithInterior = isMonolith || title.includes('Monolith');

  return (
    <div
      style={{
        width,
        height,
        position: 'relative',
        transform: `scale(${entrance}) translate(${panicShake}px, ${floatBob}px)`,
        transformOrigin: 'center center',
      }}
    >
      {/* Outer Ambient Glow */}
      <div
        style={{
          position: 'absolute',
          inset: -8,
          borderRadius: '20px',
          background: `radial-gradient(ellipse at center, ${colors.glow} 0%, rgba(0,0,0,0) 75%)`,
          zIndex: 0,
          pointerEvents: 'none',
        }}
      />

      {/* Main Glassmorphic Hardware Chassis */}
      <div
        style={{
          position: 'relative',
          width: '100%',
          height: '100%',
          borderRadius: '18px',
          background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.97) 0%, rgba(8, 12, 22, 0.99) 100%)',
          border: `2.5px solid ${colors.border}`,
          backdropFilter: 'blur(20px)',
          boxShadow: `0 16px 40px rgba(0, 0, 0, 0.85), inset 0 1.5px 2px rgba(255, 255, 255, 0.25)`,
          padding: '14px 18px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          zIndex: 1,
          overflow: 'hidden',
        }}
      >
        {/* Top Header Row: Icon + Title + Blinking Hardware LEDs */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <div
              style={{
                width: '36px',
                height: '36px',
                borderRadius: '10px',
                backgroundColor: colors.badgeBg,
                border: `1.5px solid ${colors.badgeBorder}`,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: colors.accent,
                boxShadow: `0 0 14px ${colors.glow}`,
              }}
            >
              {type === 'Database' && (
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4">
                  <ellipse cx="12" cy="5" rx="9" ry="3" />
                  <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" />
                  <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" />
                </svg>
              )}
              {type === 'Cache' && (
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
                </svg>
              )}
              {type === 'WebServer' && (
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4">
                  <rect x="2" y="3" width="20" height="7" rx="2" />
                  <rect x="2" y="14" width="20" height="7" rx="2" />
                  <line x1="6" y1="6" x2="6.01" y2="6" strokeWidth="3" strokeLinecap="round" />
                  <line x1="6" y1="17" x2="6.01" y2="17" strokeWidth="3" strokeLinecap="round" />
                </svg>
              )}
              {type === 'LoadBalancer' && (
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4">
                  <path d="M16 3h5v5" />
                  <path d="M4 20L21 3" />
                  <path d="M21 16v5h-5" />
                  <path d="M15 15l6 6" />
                  <path d="M4 4l5 5" />
                </svg>
              )}
              {type === 'CDN' && (
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4">
                  <circle cx="12" cy="12" r="10" />
                  <line x1="2" y1="12" x2="22" y2="12" />
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
                </svg>
              )}
              {type === 'MessageQueue' && (
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4">
                  <rect x="2" y="4" width="20" height="4" rx="1" />
                  <rect x="2" y="10" width="20" height="4" rx="1" />
                  <rect x="2" y="16" width="20" height="4" rx="1" />
                </svg>
              )}
            </div>

            <div>
              <div style={{ fontSize: '20px', fontWeight: 900, color: '#ffffff', letterSpacing: '-0.02em', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
                {title}
              </div>
              {tech && (
                <div style={{ fontSize: '13.5px', color: colors.accent, fontWeight: 800, marginTop: '2px' }}>
                  {tech}
                </div>
              )}
            </div>
          </div>

          {/* Real-time Hardware Activity LEDs */}
          <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
            <div
              style={{
                width: '10px',
                height: '10px',
                borderRadius: '50%',
                backgroundColor: colors.led,
                opacity: ledBlink1,
                boxShadow: `0 0 12px ${colors.led}`,
              }}
            />
            <div
              style={{
                width: '10px',
                height: '10px',
                borderRadius: '50%',
                backgroundColor: '#38bdf8',
                opacity: ledBlink2,
                boxShadow: `0 0 12px #38bdf8`,
              }}
            />
            <div
              style={{
                width: '10px',
                height: '10px',
                borderRadius: '50%',
                backgroundColor: '#a855f7',
                opacity: ledBlink3,
                boxShadow: `0 0 12px #a855f7`,
              }}
            />
          </div>
        </div>

        {/* -------------------------------------------------------------
            MONOLITH INTERNAL ARCHITECTURE CARDS (Big Clear Typography)
            ------------------------------------------------------------- */}
        {showMonolithInterior ? (
          <div
            style={{
              display: 'flex',
              gap: '10px',
              backgroundColor: 'rgba(2, 6, 23, 0.85)',
              borderRadius: '10px',
              border: '1.5px solid rgba(56, 189, 248, 0.4)',
              padding: '8px 10px',
              margin: '4px 0',
            }}
          >
            {/* Box 1: Web App */}
            <div
              style={{
                flex: 1,
                backgroundColor: status === 'overload' ? 'rgba(127, 29, 29, 0.5)' : 'rgba(15, 23, 42, 0.9)',
                border: `1.5px solid ${status === 'overload' ? '#ef4444' : '#38bdf8'}`,
                borderRadius: '8px',
                padding: '6px 8px',
                textAlign: 'center',
              }}
            >
              <div style={{ fontSize: '13px', fontWeight: 900, color: '#ffffff' }}>WEB CONTAINER</div>
              <div style={{ fontSize: '11px', color: '#38bdf8', fontWeight: 800 }}>Next.js / Node API</div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ fontSize: '14px', color: status === 'overload' ? '#ef4444' : '#f59e0b', fontWeight: 900 }}>
                ⚡
              </span>
            </div>

            {/* Box 2: Database */}
            <div
              style={{
                flex: 1,
                backgroundColor: status === 'overload' ? 'rgba(127, 29, 29, 0.5)' : 'rgba(15, 23, 42, 0.9)',
                border: `1.5px solid ${status === 'overload' ? '#ef4444' : '#a855f7'}`,
                borderRadius: '8px',
                padding: '6px 8px',
                textAlign: 'center',
              }}
            >
              <div style={{ fontSize: '13px', fontWeight: 900, color: '#ffffff' }}>DB INSTANCE</div>
              <div style={{ fontSize: '11px', color: '#c084fc', fontWeight: 800 }}>PostgreSQL Engine</div>
            </div>
          </div>
        ) : (
          <div
            style={{
              height: '32px',
              backgroundColor: 'rgba(2, 6, 23, 0.75)',
              borderRadius: '8px',
              border: '1.5px solid rgba(51, 65, 85, 0.6)',
              padding: '4px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              margin: '4px 0',
            }}
          >
            {type === 'Cache' ? (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '12px', color: '#38bdf8', fontWeight: 900 }}>⚡ RAM CACHE:</span>
                <span style={{ fontSize: '13px', color: '#4ade80', fontWeight: 900 }}>1ms (IN-MEMORY)</span>
              </div>
            ) : type === 'Database' ? (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '12px', color: '#94a3b8', fontWeight: 900 }}>NVMe SSD IOPS:</span>
                <span style={{ fontSize: '13px', color: status === 'overload' ? '#f87171' : '#38bdf8', fontWeight: 900 }}>
                  {status === 'overload' ? '100% DISK BOTTLENECK' : '84,000 IOPS'}
                </span>
              </div>
            ) : (
              <div style={{ display: 'flex', gap: '6px', width: '100%' }}>
                {[...Array(16)].map((_, i) => (
                  <div
                    key={i}
                    style={{
                      flex: 1,
                      height: '14px',
                      backgroundColor: i % 2 === 0 ? 'rgba(56, 189, 248, 0.35)' : 'rgba(30, 41, 59, 0.9)',
                      borderRadius: '3px',
                    }}
                  />
                ))}
              </div>
            )}

            {speedTag && (
              <span style={{ fontSize: '12px', fontWeight: 900, color: '#f59e0b', textTransform: 'uppercase' }}>
                {speedTag}
              </span>
            )}
          </div>
        )}

        {/* Bottom Metrics Bar: CPU Gauge & Scale Badge */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          {cpuPercent !== undefined ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flex: 1, marginRight: '14px' }}>
              <span style={{ fontSize: '12px', fontWeight: 900, color: '#94a3b8' }}>
                {status === 'overload' ? 'RAM/CPU:' : 'CPU:'}
              </span>
              <div
                style={{
                  flex: 1,
                  height: '10px',
                  backgroundColor: 'rgba(30, 41, 59, 0.9)',
                  borderRadius: '5px',
                  overflow: 'hidden',
                  border: '1px solid rgba(71, 85, 105, 0.6)',
                }}
              >
                <div
                  style={{
                    width: `${Math.min(100, cpuPercent)}%`,
                    height: '100%',
                    background:
                      cpuPercent > 85
                        ? 'linear-gradient(90deg, #f59e0b, #ef4444)'
                        : 'linear-gradient(90deg, #38bdf8, #10b981)',
                    boxShadow: cpuPercent > 85 ? '0 0 10px #ef4444' : '0 0 10px #38bdf8',
                  }}
                />
              </div>
              <span
                style={{
                  fontSize: '13px',
                  fontWeight: 900,
                  color: cpuPercent > 85 ? '#ef4444' : '#38bdf8',
                }}
              >
                {cpuPercent}%
              </span>
            </div>
          ) : (
            <div />
          )}

          {scaleCount && (
            <div
              style={{
                padding: '4px 12px',
                borderRadius: '10px',
                backgroundColor: 'rgba(56, 189, 248, 0.2)',
                border: '1.5px solid rgba(56, 189, 248, 0.55)',
                fontSize: '12px',
                fontWeight: 900,
                color: '#38bdf8',
                letterSpacing: '0.04em',
              }}
            >
              {scaleCount}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
