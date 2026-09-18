import React from 'react';
import { useCurrentFrame, Audio, staticFile } from 'remotion';
import { BeatTimelineMaster, BeatManifestItem } from '../components/v2/BeatTimelineMaster';
import beatsData from '../../public/assets/demon_core/demon_core_v2_beats_manifest.json';

export const DemonCoreV2Scene24Composition: React.FC = () => {
  const frame = useCurrentFrame();

  // Find Scene 24 in manifest
  const scene24 = beatsData.scenes.find((s: any) => s.scene_id === '24');
  if (!scene24) {
    return <div style={{ color: 'white' }}>Scene 24 not found</div>;
  }

  // Adjust start frames relative to 0 for standalone Scene 24 showcase
  const baseFrame = scene24.beats[0]?.start_frame || 0;
  const relativeBeats: BeatManifestItem[] = scene24.beats.map((b: any) => ({
    ...b,
    start_frame: b.start_frame - baseFrame,
  }));

  return (
    <div style={{ position: 'relative', width: '100%', height: '100%' }}>
      <Audio src={staticFile('assets/demon_core/audio/scenes/scene_24.wav')} />
      <BeatTimelineMaster
        beats={relativeBeats}
        sceneTitle="ACT IV // LOUIS SLOTIN & THE SCREWDRIVER"
        headline="ONE MILLIMETER SLIP"
      />
    </div>
  );
};

export const DemonCoreV2Scene04Composition: React.FC = () => {
  const scene04 = beatsData.scenes.find((s: any) => s.scene_id === '04');
  if (!scene04) {
    return <div style={{ color: 'white' }}>Scene 04 not found</div>;
  }

  const baseFrame = scene04.beats[0]?.start_frame || 0;
  const relativeBeats: BeatManifestItem[] = scene04.beats.map((b: any) => ({
    ...b,
    start_frame: b.start_frame - baseFrame,
  }));

  return (
    <div style={{ position: 'relative', width: '100%', height: '100%' }}>
      <Audio src={staticFile('assets/demon_core/audio/scenes/scene_04.wav')} />
      <BeatTimelineMaster
        beats={relativeBeats}
        sceneTitle="ACT I // CRITICALITY PHYSICS"
        headline="NEUTRON CROSSFIRE (PROMPT CRITICALITY)"
      />
    </div>
  );
};
