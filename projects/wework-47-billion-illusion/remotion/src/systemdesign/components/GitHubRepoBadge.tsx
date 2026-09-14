import React from 'react';
import { useCurrentFrame, spring, useVideoConfig } from 'remotion';

export interface GitHubRepoBadgeProps {
  repo: string;
  stars: string;
  topic?: string;
}

export const GitHubRepoBadge: React.FC<GitHubRepoBadgeProps> = ({
  repo,
  stars,
  topic,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120 },
  });

  return (
    <div
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: '10px',
        backgroundColor: 'rgba(22, 27, 34, 0.95)',
        border: '1.5px solid #38bdf8',
        borderRadius: '8px',
        padding: '7px 16px',
        color: '#f0f6fc',
        fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif',
        fontSize: '16px',
        fontWeight: 700,
        boxShadow: '0 8px 24px rgba(0,0,0,0.6), 0 0 15px rgba(56, 189, 248, 0.25)',
        transform: `scale(${entrance})`,
        transformOrigin: 'left center',
        backdropFilter: 'blur(12px)',
      }}
    >
      {/* GitHub Octocat Icon */}
      <svg height="20" viewBox="0 0 16 16" width="20" fill="currentColor">
        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" />
      </svg>
      <span style={{ color: '#58a6ff', fontFamily: 'monospace', fontWeight: 800 }}>{repo}</span>
      <span style={{ display: 'flex', alignItems: 'center', gap: '4px', color: '#e6edf3', fontSize: '14px', fontWeight: 700 }}>
        <span style={{ color: '#e3b341' }}>★</span> {stars}
      </span>
      {topic && (
        <span
          style={{
            backgroundColor: 'rgba(31, 111, 235, 0.25)',
            color: '#79c0ff',
            fontSize: '13px',
            fontWeight: 800,
            padding: '2px 8px',
            borderRadius: '12px',
            border: '1px solid rgba(56, 189, 248, 0.4)',
          }}
        >
          {topic}
        </span>
      )}
    </div>
  );
};
