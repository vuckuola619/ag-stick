import React from 'react';
import {
  useCurrentFrame,
  useVideoConfig,
  Img,
  staticFile,
  Audio,
  interpolate,
  spring,
} from 'remotion';

export interface WordInfo {
  word: string;
  start_frame: number;
  end_frame: number;
}

export interface ShortsScene {
  scene_id: string;
  headline: string;
  voiceover_text: string;
  image_file: string;
  ken_burns: {
    scale_from: number;
    scale_to: number;
    pan_y: number;
  };
  start_frame: number;
  end_frame: number;
  duration_frames: number;
  speech_frames: number;
  words: WordInfo[];
}

export interface ShortsProps {
  shorts_id: string;
  title: string;
  case_tag: string;
  fps: number;
  total_frames: number;
  duration_sec: number;
  audio_file: string;
  theme: {
    primary: string;
    accent: string;
    warning: string;
    bg: string;
  };
  scenes: ShortsScene[];
}

export const DossierShortsComposition: React.FC<ShortsProps> = ({
  shorts_id,
  title,
  case_tag,
  total_frames,
  audio_file,
  theme,
  scenes,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  // Find active scene
  const activeSceneIndex = scenes.findIndex(
    (sc) => frame >= sc.start_frame && frame < sc.end_frame
  );
  const activeScene =
    activeSceneIndex !== -1
      ? scenes[activeSceneIndex]
      : scenes[scenes.length - 1];

  // Local scene frame for transitions & animations
  const sceneLocalFrame = frame - (activeScene ? activeScene.start_frame : 0);
  const sceneDur = activeScene ? activeScene.duration_frames : 150;

  // Scene transition crossfade (12 frames)
  const crossfadeFrames = 12;
  const sceneEnterProgress = interpolate(
    sceneLocalFrame,
    [0, crossfadeFrames],
    [0, 1],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // Ken Burns drift
  const scale = interpolate(
    sceneLocalFrame,
    [0, sceneDur],
    [activeScene.ken_burns.scale_from, activeScene.ken_burns.scale_to],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );
  const panY = interpolate(
    sceneLocalFrame,
    [0, sceneDur],
    [0, activeScene.ken_burns.pan_y],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // Retention progress bar (0 to 100%)
  const progressRatio = Math.min(1, Math.max(0, frame / total_frames));

  // Current phrase/words for kinetic caption (show 4-word window or current clause)
  const currentWordIndex = activeScene.words.findIndex(
    (w) => frame >= w.start_frame && frame < w.end_frame
  );

  // Display a window of ~4-5 words around the active word
  const activeIdx = currentWordIndex !== -1 ? currentWordIndex : 0;
  const windowStart = Math.max(0, Math.floor(activeIdx / 4) * 4);
  const captionWords = activeScene.words.slice(windowStart, windowStart + 4);

  // Visual pulse on active word
  const wordSpring = spring({
    frame: currentWordIndex !== -1 ? frame - activeScene.words[currentWordIndex].start_frame : 0,
    fps,
    config: { damping: 12, stiffness: 220 },
  });

  return (
    <div
      style={{
        position: 'relative',
        width,
        height,
        backgroundColor: theme.bg,
        overflow: 'hidden',
        fontFamily: "'Inter', -apple-system, sans-serif",
      }}
    >
      {/* 1. MASTER AUDIO TRACK */}
      <Audio
        src={
          audio_file.startsWith('assets/') || audio_file.startsWith('/')
            ? staticFile(audio_file.replace(/^\//, ''))
            : staticFile(`assets/dossier_shorts/audio/${audio_file}`)
        }
      />

      {/* 2. BACKGROUND ARTWORK WITH KEN BURNS */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          opacity: sceneEnterProgress,
          transform: `scale(${scale}) translateY(${panY}px)`,
          transformOrigin: 'center center',
        }}
      >
        <Img
          src={
            activeScene.image_file.startsWith('assets/') || activeScene.image_file.startsWith('/')
              ? staticFile(activeScene.image_file.replace(/^\//, ''))
              : staticFile(`assets/dossier_shorts/scenes/${activeScene.image_file}`)
          }
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
          }}
        />
      </div>

      {/* 3. CINEMATIC NOIR ATMOSPHERIC OVERLAYS */}
      {/* Dark Vignette */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          background:
            'radial-gradient(circle at center, transparent 45%, rgba(10, 13, 20, 0.7) 80%, rgba(5, 7, 14, 0.95) 100%)',
          pointerEvents: 'none',
        }}
      />

      {/* Top and Bottom Gradient Fades for HUD legibility */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: 320,
          background:
            'linear-gradient(to bottom, rgba(5, 7, 14, 0.9) 0%, rgba(5, 7, 14, 0.4) 60%, transparent 100%)',
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          width: '100%',
          height: 480,
          background:
            'linear-gradient(to top, rgba(5, 7, 14, 0.95) 0%, rgba(5, 7, 14, 0.5) 65%, transparent 100%)',
          pointerEvents: 'none',
        }}
      />

      {/* 4. TOP HUD BAR */}
      {/* Retention Progress Line */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: 8,
          backgroundColor: 'rgba(255, 255, 255, 0.12)',
          zIndex: 50,
        }}
      >
        <div
          style={{
            width: `${progressRatio * 100}%`,
            height: '100%',
            backgroundColor: theme.accent,
            boxShadow: `0 0 16px ${theme.accent}`,
          }}
        />
      </div>

      {/* Top Badges */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: 36,
          right: 36,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 40,
        }}
      >
        <div
          style={{
            padding: '10px 18px',
            backgroundColor: 'rgba(10, 13, 20, 0.85)',
            backdropFilter: 'blur(12px)',
            border: `1px solid ${theme.primary}55`,
            borderRadius: 10,
            fontSize: 15,
            fontWeight: 900,
            letterSpacing: '0.12em',
            color: theme.accent,
            boxShadow: `0 0 20px ${theme.primary}33`,
          }}
        >
          {case_tag}
        </div>

        <div
          style={{
            padding: '10px 16px',
            backgroundColor: 'rgba(10, 13, 20, 0.85)',
            backdropFilter: 'blur(12px)',
            border: '1px solid rgba(255, 255, 255, 0.15)',
            borderRadius: 10,
            fontSize: 13,
            fontWeight: 800,
            letterSpacing: '0.1em',
            color: '#cbd5e1',
          }}
        >
          DECLASSIFIED
        </div>
      </div>

      {/* 5. DYNAMIC KINETIC CAPTIONS (VIRAL SHORTS STYLE) */}
      <div
        style={{
          position: 'absolute',
          bottom: 340,
          left: 48,
          right: 48,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 40,
        }}
      >
        <div
          style={{
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'center',
            alignItems: 'center',
            gap: '12px 16px',
            padding: '20px 32px',
            backgroundColor: 'rgba(5, 7, 14, 0.82)',
            backdropFilter: 'blur(16px)',
            borderRadius: 24,
            border: '1px solid rgba(255, 255, 255, 0.12)',
            boxShadow: '0 16px 40px rgba(0,0,0,0.85)',
            maxWidth: 960,
          }}
        >
          {captionWords.map((w, i) => {
            const isWordActive =
              frame >= w.start_frame && frame < w.end_frame;
            const isWordPast = frame >= w.end_frame;

            return (
              <span
                key={i}
                style={{
                  fontFamily: "'Impact', 'Arial Black', sans-serif",
                  fontSize: isWordActive ? 52 : 46,
                  fontWeight: 900,
                  letterSpacing: '0.04em',
                  textTransform: 'uppercase',
                  color: isWordActive
                    ? theme.accent
                    : isWordPast
                    ? '#ffffff'
                    : '#94a3b8',
                  transform: isWordActive
                    ? `scale(${1 + wordSpring * 0.12})`
                    : 'scale(1)',
                  display: 'inline-block',
                  textShadow: isWordActive
                    ? `0 0 24px ${theme.accent}, 0 4px 8px #000000`
                    : '0 3px 6px #000000',
                  transition: 'transform 0.05s ease, color 0.05s ease',
                }}
              >
                {w.word}
              </span>
            );
          })}
        </div>
      </div>

      {/* 6. BOTTOM HUD WATERMARK */}
      <div
        style={{
          position: 'absolute',
          bottom: 120,
          left: 0,
          width: '100%',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 40,
        }}
      >
        <div
          style={{
            fontSize: 13,
            fontWeight: 800,
            letterSpacing: '0.2em',
            color: 'rgba(255, 255, 255, 0.45)',
            textTransform: 'uppercase',
          }}
        >
          THE DOSSIER ZERO • SUBSCRIBE FOR CASE FILES
        </div>
      </div>
    </div>
  );
};
