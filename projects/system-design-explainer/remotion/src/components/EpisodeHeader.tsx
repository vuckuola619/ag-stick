import React from 'react';

export interface EpisodeHeaderProps {
  seriesTitle?: string;
  episodeTitle: string;
  topicTag: string;
}

export const EpisodeHeader: React.FC<EpisodeHeaderProps> = ({
  seriesTitle = 'SYSTEM DESIGN PRIMER // HIGH SCALE',
  episodeTitle,
  topicTag,
}) => {
  return (
    <div
      style={{
        position: 'absolute',
        top: '30px',
        left: '40px',
        display: 'flex',
        flexDirection: 'column',
        gap: '6px',
        fontFamily: 'Inter, system-ui, sans-serif',
        zIndex: 100,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <div
          style={{
            backgroundColor: '#0284c7',
            color: '#f0f9ff',
            fontSize: '11px',
            fontWeight: 800,
            padding: '2px 8px',
            borderRadius: '4px',
            letterSpacing: '0.08em',
          }}
        >
          {topicTag}
        </div>
        <div
          style={{
            color: '#64748b',
            fontSize: '11px',
            fontWeight: 700,
            letterSpacing: '0.08em',
            fontFamily: 'monospace',
          }}
        >
          {seriesTitle}
        </div>
      </div>
      <div
        style={{
          color: '#f8fafc',
          fontSize: '22px',
          fontWeight: 800,
          letterSpacing: '-0.02em',
          textShadow: '0 2px 10px rgba(0,0,0,0.8)',
        }}
      >
        {episodeTitle}
      </div>
    </div>
  );
};
