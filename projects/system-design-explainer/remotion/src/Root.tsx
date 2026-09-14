import React from 'react';
import { Composition } from 'remotion';
import { SystemDesignMasterComposition } from './SystemDesignMasterComposition';

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="SystemDesignMaster"
        component={SystemDesignMasterComposition}
        durationInFrames={2000}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
