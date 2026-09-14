import React from 'react';
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export type SystemNodeType =
  | 'Client'
  | 'DNS'
  | 'CDN'
  | 'LoadBalancer'
  | 'WebServer'
  | 'Database'
  | 'Cache'
  | 'MessageQueue';

export interface SystemNodeProps {
  type: SystemNodeType;
  title: string;
  tech?: string;
  status?: 'healthy' | 'warning' | 'overload' | 'offline';
  cpuPercent?: number;
  scaleCount?: string;
  width?: number;
  height?: number;
}

export const SystemNode: React.FC<SystemNodeProps> = ({
  type,
  title,
  tech,
  status = 'healthy',
  cpuPercent,
  scaleCount,
  width = 200,
  height = 110,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Color mappings
  const statusColors = {
    healthy: { border: '#10b981', glow: 'rgba(16, 185, 129, 0.25)', badge: '#065f46', text: '#34d399' },
    warning: { border: '#f59e0b', glow: 'rgba(245, 158, 11, 0.3)', badge: '#78350f', text: '#fbbf24' },
    overload: { border: '#ef4444', glow: 'rgba(239, 68, 68, 0.4)', badge: '#7f1d1d', text: '#f87171' },
    offline: { border: '#64748b', glow: 'rgba(100, 116, 139, 0.15)', badge: '#1e293b', text: '#94a3b8' },
  }[status];

  // Overload shake
  const shake = status === 'overload' ? (Math.sin(frame * 2.0) * 3) : 0;

  // Pulse animation for glow
  const pulse = Math.sin(frame / 6) * 0.1 + 0.9;

  // Spring appearance
  const enterSpring = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 140 },
  });

  // Render tech icon
  const renderIcon = () => {
    switch (type) {
      case 'Database':
        return (
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <ellipse cx="12" cy="5" rx="9" ry="3" />
            <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" />
            <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" />
          </svg>
        );
      case 'Cache':
        return (
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
          </svg>
        );
      case 'LoadBalancer':
        return (
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="18" cy="18" r="3" />
            <circle cx="6" cy="6" r="3" />
            <path d="M13 6h3a2 2 0 0 1 2 2v7" />
            <path d="M6 9v12" />
          </svg>
        );
      case 'CDN':
        return (
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="12" cy="12" r="10" />
            <line x1="2" y1="12" x2="22" y2="12" />
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
          </svg>
        );
      case 'MessageQueue':
        return (
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <line x1="4" y1="6" x2="20" y2="6" />
            <line x1="4" y1="12" x2="20" y2="12" />
            <line x1="4" y1="18" x2="20" y2="18" />
            <circle cx="8" cy="6" r="2" fill="currentColor" />
            <circle cx="14" cy="12" r="2" fill="currentColor" />
            <circle cx="10" cy="18" r="2" fill="currentColor" />
          </svg>
        );
      default:
        return (
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <rect x="2" y="2" width="20" height="8" rx="2" ry="2" />
            <rect x="2" y="14" width="20" height="8" rx="2" ry="2" />
            <line x1="6" y1="6" x2="6.01" y2="6" />
            <line x1="6" y1="18" x2="6.01" y2="18" />
          </svg>
        );
    }
  };

  return (
    <div
      style={{
        width: `${width}px`,
        height: `${height}px`,
        backgroundColor: '#111827',
        border: `2px solid ${statusColors.border}`,
        borderRadius: '12px',
        padding: '12px 14px',
        boxShadow: `0 10px 25px rgba(0,0,0,0.6), 0 0 20px ${statusColors.glow}`,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        position: 'relative',
        transform: `scale(${enterSpring}) translate(${shake}px, 0)`,
        overflow: 'hidden',
      }}
    >
      {/* Top Row: Icon, Title, Status Indicator */}
      <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '6px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: statusColors.text, flex: 1, minWidth: 0 }}>
          {renderIcon()}
          <div style={{ minWidth: 0 }}>
            <div style={{ color: '#f8fafc', fontWeight: 700, fontSize: '13px', fontFamily: 'Inter, sans-serif', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
              {title}
            </div>
            {tech && (
              <div style={{ color: '#94a3b8', fontSize: '10.5px', fontFamily: 'monospace', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                {tech}
              </div>
            )}
          </div>
        </div>

        {/* Right Header: Scale Badge + Status Dot */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexShrink: 0 }}>
          {scaleCount && (
            <div
              style={{
                backgroundColor: '#1e293b',
                color: '#38bdf8',
                fontSize: '9.5px',
                fontWeight: 700,
                padding: '1px 5px',
                borderRadius: '3px',
                border: '1px solid #0284c7',
                whiteSpace: 'nowrap',
              }}
            >
              {scaleCount}
            </div>
          )}
          <div
            style={{
              width: '9px',
              height: '9px',
              borderRadius: '50%',
              backgroundColor: statusColors.border,
              boxShadow: `0 0 8px ${statusColors.border}`,
              transform: `scale(${pulse})`,
            }}
          />
        </div>
      </div>

      {/* Bottom Row: CPU & Status Banner */}
      <div style={{ marginTop: '6px' }}>
        {typeof cpuPercent === 'number' && (
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', marginBottom: '3px' }}>
              <span style={{ color: '#64748b' }}>CPU LOAD</span>
              <span style={{ color: statusColors.text, fontWeight: 700, fontFamily: 'monospace' }}>
                {cpuPercent}%
              </span>
            </div>
            <div style={{ width: '100%', height: '5px', backgroundColor: '#1e293b', borderRadius: '3px', overflow: 'hidden' }}>
              <div
                style={{
                  width: `${Math.min(cpuPercent, 100)}%`,
                  height: '100%',
                  backgroundColor: statusColors.border,
                  transition: 'width 0.2s ease',
                }}
              />
            </div>
          </div>
        )}

        {status === 'overload' && (
          <div
            style={{
              marginTop: '4px',
              backgroundColor: '#7f1d1d',
              color: '#fca5a5',
              fontSize: '10px',
              fontWeight: 800,
              padding: '2px 6px',
              borderRadius: '3px',
              textAlign: 'center',
              letterSpacing: '0.05em',
            }}
          >
            🔥 504 GATEWAY TIMEOUT
          </div>
        )}
      </div>
    </div>
  );
};
