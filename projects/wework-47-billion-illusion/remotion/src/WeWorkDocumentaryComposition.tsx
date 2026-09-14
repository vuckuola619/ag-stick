import React from 'react';
import { Sequence, Audio, staticFile, useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';
import { PaperBackground } from './components/PaperBackground';
import { LowerThird } from './components/LowerThird';
import { FilmGrainOverlay } from './components/FilmGrainOverlay';
import { KineticHeadline } from './components/KineticHeadline';
import { WatermarkStamp } from './components/WatermarkStamp';
import { EditorialDustParticles } from './components/EditorialDustParticles';
import { KenBurnsImage } from './components/KenBurnsImage';

export interface SceneItem {
  sceneIndex: number;
  sceneId: string;
  act: string;
  narration: string;
  kineticHeading: string;
  lowerThird: string;
  audioSrc: string;
  imageSrc: string;
  puppetSrc?: string | null;
  startFrame: number;
  durationInFrames: number;
  durationSeconds: number;
  posterizeFps: number;
  transition?: string;
}

export interface ManifestProps {
  project: string;
  workingTitle: string;
  totalDurationSeconds: number;
  totalFrames: number;
  fps: number;
  width: number;
  height: number;
  visualStyle: string;
  masterAudioSrc: string;
  scenes: SceneItem[];
}

export const WeWorkDocumentaryComposition: React.FC<ManifestProps> = ({ scenes }) => {
  return (
    <div
      style={{
        flex: 1,
        width: 1920,
        height: 1080,
        backgroundColor: '#14171d',
        position: 'relative',
        overflow: 'hidden',
        fontFamily: "'Helvetica Neue', Arial, sans-serif",
      }}
    >
      {/* Background Tactile Paper Texture */}
      <PaperBackground />

      {/* Render each documentary scene with zero-shake cinematic stability */}
      {scenes.map((scene) => {
        return (
          <Sequence
            key={scene.sceneId}
            from={scene.startFrame}
            durationInFrames={scene.durationInFrames}
          >
            <SceneContent scene={scene} />
            {scene.audioSrc && <Audio src={staticFile(scene.audioSrc)} volume={1.0} />}
          </Sequence>
        );
      })}

      {/* Broadcast Global Overlays */}
      <WatermarkStamp label="SEC FORENSIC ARCHIVES // WEWORK INVESTIGATION" />
      <EditorialDustParticles />
      <FilmGrainOverlay opacity={0.06} />
    </div>
  );
};

const SceneContent: React.FC<{ scene: SceneItem }> = ({ scene }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Smooth spring entrance (NO VIOLENT JITTER OR DIZZYING SHAKE)
  const cardSpring = spring({
    fps,
    frame,
    config: { damping: 16, stiffness: 120 },
  });

  const cardOpacity = interpolate(cardSpring, [0, 1], [0, 1]);
  const cardScale = interpolate(cardSpring, [0, 1], [0.92, 1.0]);

  // Smooth, subtle cinematic drift (0.3% over entire scene duration, perfectly stable)
  const slowDrift = interpolate(frame, [0, scene.durationInFrames], [1.0, 1.03], {
    extrapolateRight: 'clamp',
  });

  // Choose alternating transition style for Ken Burns
  const transitionStyles = ['ken_burns_in', 'ken_burns_out', 'pan_right', 'pan_left'];
  const transitionStyle = transitionStyles[scene.sceneIndex % transitionStyles.length];

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        position: 'relative',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        opacity: cardOpacity,
        transform: `scale(${cardScale})`,
      }}
    >
      {/* Central Visual Document / Real Archival Photograph Card */}
      {scene.imageSrc && (
        <div
          style={{
            position: 'absolute',
            width: '1380px',
            height: '780px',
            top: '150px',
            left: '270px',
            backgroundColor: '#ffffff',
            padding: '16px',
            borderRadius: '6px',
            boxShadow: '0 30px 70px rgba(0, 0, 0, 0.65), 0 10px 25px rgba(0, 0, 0, 0.4)',
            overflow: 'hidden',
            transform: `scale(${slowDrift})`,
            transformOrigin: 'center center',
          }}
        >
          <KenBurnsImage
            imageSrc={scene.imageSrc}
            durationInFrames={scene.durationInFrames}
            transitionStyle={transitionStyle}
          />

          {/* Authentic Corner Tape Frills */}
          <div
            style={{
              position: 'absolute',
              top: '-10px',
              left: '40px',
              width: '100px',
              height: '35px',
              backgroundColor: 'rgba(235, 230, 215, 0.65)',
              transform: 'rotate(-4deg)',
              boxShadow: '0 2px 5px rgba(0,0,0,0.15)',
              backdropFilter: 'blur(1px)',
            }}
          />
          <div
            style={{
              position: 'absolute',
              top: '-10px',
              right: '40px',
              width: '100px',
              height: '35px',
              backgroundColor: 'rgba(235, 230, 215, 0.65)',
              transform: 'rotate(5deg)',
              boxShadow: '0 2px 5px rgba(0,0,0,0.15)',
              backdropFilter: 'blur(1px)',
            }}
          />
        </div>
      )}

      {/* Photographic Cutout Puppet Overlay with Clean Smooth Breathing (NO CAMERA SHAKE) */}
      {scene.puppetSrc && (
        <div
          style={{
            position: 'absolute',
            bottom: '30px',
            right: '90px',
            width: '420px',
            height: '520px',
            zIndex: 35,
            filter: 'drop-shadow(20px 30px 25px rgba(0,0,0,0.75))',
            transform: `scale(${slowDrift})`,
            transformOrigin: 'bottom center',
          }}
        >
          <img
            src={staticFile(scene.puppetSrc)}
            alt="Puppet"
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'contain',
            }}
          />
        </div>
      )}

      {/* Kinetic Headline with Clean Visibility */}
      {scene.kineticHeading && (
        <div
          style={{
            position: 'absolute',
            top: '40px',
            left: '80px',
            right: '80px',
            zIndex: 40,
          }}
        >
          <KineticHeadline text={scene.kineticHeading} />
        </div>
      )}

      {/* Forensic Lower Third */}
      {scene.lowerThird && (
        <div
          style={{
            position: 'absolute',
            bottom: '40px',
            left: '80px',
            zIndex: 40,
          }}
        >
          <LowerThird text={scene.lowerThird} />
        </div>
      )}
    </div>
  );
};
