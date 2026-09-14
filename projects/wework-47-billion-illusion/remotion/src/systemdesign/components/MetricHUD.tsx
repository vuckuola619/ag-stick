import React from 'react';
import { useCurrentFrame } from 'remotion';

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

  const formatNumber = (num: number) => {
    if (num >= 1000000) return `${(num / 1000000).toFixed(num % 1000000 === 0 ? 0 : 1)}M`;
    if (num >= 1000) return `${(num / 1000).toFixed(num % 1000 === 0 ? 0 : 1)}k`;
    return num.toLocaleString();
  };

  const alertFlash = isAlert ? (Math.sin(frame / 4) > 0 ? '#ef4444' : '#7f1d1d') : '#10b981';

  return (
    <div
      style={{
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
          gap: '10px',
          backgroundColor: '#0f172a',
          border: `2px solid ${isAlert ? '#ef4444' : '#38bdf8'}`,
          borderRadius: '10px',
          padding: '8px 18px',
          boxShadow: `0 8px 25px rgba(0,0,0,0.7), 0 0 15px ${isAlert ? 'rgba(239, 68, 68, 0.4)' : 'rgba(56, 189, 248, 0.25)'}`,
        }}
      >
        <div
          style={{
            width: '10px',
            height: '10px',
            borderRadius: '50%',
            backgroundColor: alertFlash,
            boxShadow: `0 0 12px ${alertFlash}`,
          }}
        />
        <div
          style={{
            color: '#f8fafc',
            fontWeight: 900,
            fontSize: '16px',
            letterSpacing: '0.06em',
            textTransform: 'uppercase',
          }}
        >
          {levelTitle}
        </div>
      </div>

      {/* Grid of Real-Time Metrics with BIG Typography */}
      <div
        style={{
          display: 'flex',
          gap: '16px',
          backgroundColor: 'rgba(15, 23, 42, 0.95)',
          border: '1.5px solid rgba(56, 189, 248, 0.35)',
          borderRadius: '12px',
          padding: '12px 20px',
          boxShadow: '0 14px 35px rgba(0,0,0,0.75)',
          backdropFilter: 'blur(16px)',
        }}
      >
        {/* Active Users */}
        <div style={{ textAlign: 'center', minWidth: '110px' }}>
          <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800, letterSpacing: '0.04em' }}>ACTIVE USERS</div>
          <div style={{ color: '#ffffff', fontSize: '28px', fontWeight: 900, fontFamily: 'monospace', marginTop: '2px' }}>
            {formatNumber(userCount)}
          </div>
        </div>

        <div style={{ width: '1.5px', backgroundColor: 'rgba(51, 65, 85, 0.6)' }} />

        {/* Requests Per Second (QPS) */}
        <div style={{ textAlign: 'center', minWidth: '110px' }}>
          <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800, letterSpacing: '0.04em' }}>THROUGHPUT</div>
          <div style={{ color: '#38bdf8', fontSize: '28px', fontWeight: 900, fontFamily: 'monospace', marginTop: '2px' }}>
            {formatNumber(qps)}/s
          </div>
        </div>

        <div style={{ width: '1.5px', backgroundColor: 'rgba(51, 65, 85, 0.6)' }} />

        {/* Latency */}
        <div style={{ textAlign: 'center', minWidth: '110px' }}>
          <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800, letterSpacing: '0.04em' }}>P99 LATENCY</div>
          <div
            style={{
              color: latencyMs > 300 ? '#f87171' : latencyMs > 80 ? '#fbbf24' : '#34d399',
              fontSize: '28px',
              fontWeight: 900,
              fontFamily: 'monospace',
              marginTop: '2px',
              textShadow: latencyMs > 300 ? '0 0 12px rgba(239, 68, 68, 0.6)' : 'none',
            }}
          >
            {latencyMs}ms
          </div>
        </div>
      </div>
    </div>
  );
};
