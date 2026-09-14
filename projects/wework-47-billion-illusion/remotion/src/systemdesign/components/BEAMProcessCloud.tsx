import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';

export interface BEAMProcessCloudProps {
  actorCount?: number;
  highlightErlang?: boolean;
}

export const BEAMProcessCloud: React.FC<BEAMProcessCloudProps> = ({
  actorCount = 1000000,
  highlightErlang = true,
}) => {
  const frame = useCurrentFrame();

  return (
    <div
      style={{
        display: 'flex',
        gap: '24px',
        alignItems: 'stretch',
      }}
    >
      {/* Box A: Traditional OS Threads (Heavy & Red) */}
      <div
        style={{
          width: '320px',
          backgroundColor: 'rgba(24, 15, 23, 0.9)',
          border: '2px solid rgba(239, 68, 68, 0.4)',
          borderRadius: '18px',
          padding: '20px',
          boxShadow: '0 8px 25px rgba(0,0,0,0.6)',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
        }}
      >
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
            <span style={{ fontSize: '18px' }}>⚠️</span>
            <div style={{ color: '#f87171', fontSize: '15px', fontWeight: 800 }}>TRADITIONAL OS THREAD</div>
          </div>
          <div style={{ color: '#fca5a5', fontSize: '28px', fontWeight: 900, fontFamily: 'monospace', marginBottom: '4px' }}>
            2,048 KB <span style={{ fontSize: '14px', color: '#94a3b8' }}>/ Thread</span>
          </div>
          <div style={{ color: '#94a3b8', fontSize: '12px', lineHeight: '1.4' }}>
            Heavy kernel stack. Context switches choke CPU at 10,000 threads.
          </div>
        </div>

        <div style={{ marginTop: '14px', padding: '8px 12px', backgroundColor: 'rgba(239, 68, 68, 0.15)', borderRadius: '10px', border: '1px solid rgba(239, 68, 68, 0.3)' }}>
          <div style={{ color: '#ef4444', fontSize: '12px', fontWeight: 800 }}>💥 C10K WALL: OUT OF RAM</div>
        </div>
      </div>

      {/* Box B: Erlang / BEAM Actor Process (Super Lightweight & Emerald) */}
      <div
        style={{
          width: '360px',
          backgroundColor: 'rgba(15, 30, 23, 0.95)',
          border: '2.5px solid #25d366',
          borderRadius: '18px',
          padding: '20px',
          boxShadow: '0 0 30px rgba(37, 211, 102, 0.35), 0 8px 25px rgba(0,0,0,0.7)',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          position: 'relative',
          overflow: 'hidden',
        }}
      >
        {/* Subtle glowing ambient orb inside card */}
        <div
          style={{
            position: 'absolute',
            top: '-20px',
            right: '-20px',
            width: '120px',
            height: '120px',
            borderRadius: '50%',
            backgroundColor: 'rgba(37, 211, 102, 0.2)',
            filter: 'blur(30px)',
            pointerEvents: 'none',
          }}
        />

        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
            <span style={{ fontSize: '18px' }}>⚡</span>
            <div style={{ color: '#4ade80', fontSize: '15px', fontWeight: 800 }}>ERLANG / BEAM ACTOR</div>
          </div>
          <div style={{ color: '#25d366', fontSize: '32px', fontWeight: 900, fontFamily: 'monospace', marginBottom: '4px' }}>
            300 Bytes <span style={{ fontSize: '14px', color: '#86efac' }}>/ Actor</span>
          </div>
          <div style={{ color: '#cbd5e1', fontSize: '12.5px', lineHeight: '1.4' }}>
            Micro-heap in user space. Zero kernel context switches. Runs millions concurrently!
          </div>
        </div>

        <div style={{ marginTop: '14px', padding: '8px 12px', backgroundColor: 'rgba(37, 211, 102, 0.18)', borderRadius: '10px', border: '1px solid rgba(37, 211, 102, 0.4)' }}>
          <div style={{ color: '#4ade80', fontSize: '12px', fontWeight: 800 }}>🚀 1M+ PROCESSES PER CORE</div>
        </div>
      </div>
    </div>
  );
};
