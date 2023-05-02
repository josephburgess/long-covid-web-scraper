import { Options } from 'react-wordcloud';

export const wordCloudOptions: Partial<Options> = {
  fontFamily: 'Roboto, sans-serif',
  fontSizes: [16, 60],
  rotations: 2,
  rotationAngles: [0, 45],
  fontStyle: 'normal',
  fontWeight: 'normal',
  padding: 4,
  scale: 'sqrt',
  spiral: 'archimedean',
  transitionDuration: 1000,
};
