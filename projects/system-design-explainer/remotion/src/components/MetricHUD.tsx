import React from 'react';
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export interface MetricHUDProps {
  levelTitle: string;
  userCount: number;
  qps: number;
  latencyMs: number;
  statusText?: string;
  isAlert?: boolean;
}

export const MetricHUD: React.FC<MetricHUDProps> = ({
  levelTitle,
  userCount,
  qps,
  latencyMs,
  statusText = 'OPERATIONAL',
  isAlert = false,
}) => {
  const frame = useCurrentFrame();

  // Format large numbers
  const formatNumber = (num: number) => {
    if (num >= 1000000) return `${(num / 1000000).toFixed(num % 1000000 === 0 ? 0 : 1)}M`;
    if (num >= 1000) return `${(num / 1000).toFixed(num % 1000 === 0 ? 0 : 1)}k`;
    return num.toLocaleString();
  };

  const alertFlash = isAlert ? (Math.sin(frame / 4) > 0 ? '#ef4444' : '#7f1d1d') : '#10b981';

  return (
    <div
      style={{
        position: 'absolute',
        top: '30px',
        right: '40px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'flex-end',
        gap: '10px',
        fontFamily: 'Inter, system-ui, sans-serif',
        zIndex: 100,
      }}
    >
      {/* Current Scale Architecture Level Badge */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          backgroundColor: '#111827',
          border: `1.5px solid ${isAlert ? '#ef4444' : '#38bdf8'}`,
          borderRadius: '8px',
          padding: '6px 14px',
          boxShadow: '0 8px 24px rgba(0,0,0,0.6)',
        }}
      >
        <div
          style={{
            width: '8px',
            height: '8px',
            borderRadius: '50%',
            backgroundColor: alertFlash,
            boxShadow: `0 0 10px ${alertFlash}`,
          }}
        />
        <div
          style={{
            color: '#f8fafc',
            fontWeight: 800,
            fontSize: '13px',
            letterSpacing: '0.06em',
            textTransform: 'uppercase',
          }}
        >
          {levelTitle}
        </div>
      </div>

      {/* Grid of Real-Time Metrics */}
      <div
        style={{
          display: 'flex',
          gap: '12px',
          backgroundColor: '#0f172a',
          border: '1px solid #1e293b',
          borderRadius: '10px',
          padding: '10px 16px',
          boxShadow: '0 12px 30px rgba(0,0,0,0.7)',
        }}
      >
        {/* Active Users */}
        <div style={{ textAlign: 'center', minWidth: '85px' }}>
          <div style={{ color: '#64748b', fontSize: '11px', fontWeight: 600 }}>ACTIVE USERS</div>
          <div style={{ color: '#f8fafc', fontSize: '20px', fontWeight: 800, fontFamily: 'monospace' }}>
            {formatNumber(userCount)}
          </div>
        </div>

        <div style={{ width: '1px', backgroundColor: '#1e293b' }} />

        {/* Requests Per Second (QPS) */}
        <div style={{ textAlign: 'center', minWidth: '85px' }}>
          <div style={{ color: '#64748b', fontSize: '11px', fontWeight: 600 }}>THROUGHPUT</div>
          <div style={{ color: '#38bdf8', fontSize: '20px', fontWeight: 800, fontFamily: 'monospace' }}>
            {formatNumber(qps)}/s
          </div>
        </div>

        <div style={{ width: '1px', backgroundColor: '#1e293b' }} />

        {/* Latency */}
        <div style={{ textAlign: 'center', minWidth: '85px' }}>
          <div style={{ color: '#64748b', fontSize: '11px', fontWeight: 600 }}>P99 LATENCY</div>
          <div
            style={{
              color: latencyMs > 300 ? '#f87171' : latencyMs > 80 ? '#fbbf24' : '#34d399',
              fontSize: '20px',
              fontWeight: 800,
              fontFamily: 'monospace',
            }}
          >
            {latencyMs}ms
          </div>
        </div>
      </div>
    </div>
  );
};
