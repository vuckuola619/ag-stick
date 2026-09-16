import React from 'react';
import { Composition } from 'remotion';
import { WeWorkDocumentaryComposition } from './WeWorkDocumentaryComposition';
import { SystemDesignMasterComposition } from './systemdesign/SystemDesignMasterComposition';
import { SystemDesignTikTokComposition } from './systemdesign/SystemDesignTikTokComposition';
import { WhatsAppMasterComposition } from './systemdesign/WhatsAppMasterComposition';
import { WhatsAppTikTokComposition } from './systemdesign/WhatsAppTikTokComposition';
import { MercuryMasterComposition } from './mercury/MercuryMasterComposition';
import { MercuryTikTokComposition } from './mercury/MercuryTikTokComposition';
import { MercurySceneRemakeComposition } from './mercury/MercurySceneRemakeComposition';
import { MercurySceneTikTokComposition } from './mercury/MercurySceneTikTokComposition';
import { MercuryEnterprise8MinComposition } from './mercury/MercuryEnterprise8MinComposition';
import { MercuryEnglish8MinComposition } from './mercury/MercuryEnglish8MinComposition';
import { WhitePhosphorus10MinComposition } from './whitephosphorus/WhitePhosphorus10MinComposition';
import { DemonCore10MinComposition } from './demoncore/DemonCore10MinComposition';
import manifestData from '../public/scene_manifest.json';

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="WeWorkDocumentary"
        component={WeWorkDocumentaryComposition}
        durationInFrames={manifestData.totalFrames}
        fps={manifestData.fps}
        width={manifestData.width}
        height={manifestData.height}
        defaultProps={manifestData as any}
      />
      <Composition
        id="SystemDesignMaster"
        component={SystemDesignMasterComposition}
        durationInFrames={2200}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="SystemDesignTikTok"
        component={SystemDesignTikTokComposition}
        durationInFrames={2200}
        fps={30}
        width={1080}
        height={1920}
      />
      <Composition
        id="WhatsAppMaster"
        component={WhatsAppMasterComposition}
        durationInFrames={2370}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="WhatsAppTikTok"
        component={WhatsAppTikTokComposition}
        durationInFrames={2370}
        fps={30}
        width={1080}
        height={1920}
      />
      <Composition
        id="MercuryMaster"
        component={MercuryMasterComposition}
        durationInFrames={1512}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="MercuryTikTok"
        component={MercuryTikTokComposition}
        durationInFrames={1512}
        fps={30}
        width={1080}
        height={1920}
      />
      <Composition
        id="MercurySceneMaster"
        component={MercurySceneRemakeComposition}
        durationInFrames={1512}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="MercurySceneTikTok"
        component={MercurySceneTikTokComposition}
        durationInFrames={1512}
        fps={30}
        width={1080}
        height={1920}
      />
      <Composition
        id="MercuryEnterprise8Min"
        component={MercuryEnterprise8MinComposition}
        durationInFrames={23359}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="MercuryEnglish8Min"
        component={MercuryEnglish8MinComposition}
        durationInFrames={14833}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="WhitePhosphorus10Min"
        component={WhitePhosphorus10MinComposition}
        durationInFrames={18720}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="DemonCore10Min"
        component={DemonCore10MinComposition}
        durationInFrames={18252}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
