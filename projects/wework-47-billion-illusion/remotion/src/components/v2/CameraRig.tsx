import React from 'react';
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export type CameraShotType = 'wide' | 'medium' | 'closeup' | 'macro' | 'extreme_closeup' | 'dutch';
export type CameraMotionType =
  | 'static'
  | 'push_in'
  | 'pull_out'
  | 'pan_left'
  | 'pan_right'
  | 'snap_zoom'
  | 'shake'
  | 'whip';

export interface CameraRigProps {
  shot?: CameraShotType;
  motion?: CameraMotionType;
  strength?: number;
  durationFrames: number;
  currentFrame?: number;
  children: React.ReactNode;
}

export const CameraRig: React.FC<CameraRigProps> = ({
  shot = 'medium',
  motion = 'static',
  strength = 0.35,
  durationFrames,
  currentFrame: customFrame,
  children,
}) => {
  const globalFrame = useCurrentFrame();
  const frame = customFrame !== undefined ? customFrame : globalFrame;
  const { fps } = useVideoConfig();

  // 1. Base Scale & Pan corresponding to Shot type
  let baseScale = 1.0;
  let basePanY = 0;

  switch (shot) {
    case 'wide':
      baseScale = 1.0;
      basePanY = 0;
      break;
    case 'medium':
      baseScale = 1.22;
      basePanY = 25;
      break;
    case 'closeup':
      baseScale = 1.65;
      basePanY = 50;
      break;
    case 'macro':
      baseScale = 2.4;
      basePanY = 85;
      break;
    case 'extreme_closeup':
      baseScale = 3.2;
      basePanY = 110;
      break;
    case 'dutch':
      baseScale = 1.25;
      basePanY = 20;
      break;
  }

  // 2. Dynamic Motion Choreography
  let motionScale = 0;
  let motionPanX = 0;
  let motionPanY = 0;
  let rotation = shot === 'dutch' ? -6 : 0;

  if (motion === 'push_in') {
    motionScale = interpolate(
      frame,
      [0, durationFrames],
      [0, 0.15 * strength * 2.0],
      { extrapolateRight: 'clamp' }
    );
  } else if (motion === 'pull_out') {
    motionScale = interpolate(
      frame,
      [0, durationFrames],
      [0.15 * strength * 2.0, 0],
      { extrapolateRight: 'clamp' }
    );
  } else if (motion === 'pan_left') {
    motionPanX = interpolate(
      frame,
      [0, durationFrames],
      [40 * strength, -40 * strength],
      { extrapolateRight: 'clamp' }
    );
  } else if (motion === 'pan_right') {
    motionPanX = interpolate(
      frame,
      [0, durationFrames],
      [-40 * strength, 40 * strength],
      { extrapolateRight: 'clamp' }
    );
  } else if (motion === 'snap_zoom') {
    const snap = spring({
      frame,
      fps,
      config: { damping: 12, stiffness: 220, mass: 0.5 },
    });
    motionScale = (snap - 1.0) * 0.45 * strength;
  } else if (motion === 'shake') {
    // Camera trauma shake
    const decay = interpolate(frame, [0, durationFrames], [1.0, 0.2], {
      extrapolateRight: 'clamp',
    });
    const shakeMag = 18 * strength * decay;
    motionPanX = Math.sin(frame * 1.8) * shakeMag;
    motionPanY = Math.cos(frame * 2.3) * (shakeMag * 0.75);
    rotation += Math.sin(frame * 1.4) * (2.2 * strength * decay);
  }

  const finalScale = Math.max(0.8, baseScale + motionScale);
  const finalPanX = motionPanX;
  const finalPanY = basePanY + motionPanY;

  return (
    <div
      style={{
        position: 'absolute',
        width: '100%',
        height: '100%',
        transform: `translate(${finalPanX}px, ${finalPanY}px) scale(${finalScale}) rotate(${rotation}deg)`,
        transformOrigin: 'center 60%',
        transition: 'transform 0.05s ease-out',
      }}
    >
      {children}
    </div>
  );
};
