import React from 'react';
import ReactWordCloud from 'react-wordcloud';

import 'tippy.js/dist/tippy.css';
import 'tippy.js/animations/scale.css';

import { useWordClickCallbacks } from '../../hooks/useWordClickCallbacks';
import { useFetchData } from '../../hooks/useFetchData';
import { wordCloudOptions } from '../../utils/wordCloudOptions';
import { fetchWordCloudData } from '../../services/wordcloudApi';

interface WordCloudProps {
  onWordClick: (word: string) => void;
}

const WordCloud: React.FC<WordCloudProps> = ({ onWordClick }) => {
  const [wordData, isLoading] = useFetchData(fetchWordCloudData);
  const callbacks = useWordClickCallbacks(onWordClick);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div style={{ width: '100%', height: '400px' }}>
      <ReactWordCloud
        options={wordCloudOptions}
        words={wordData}
        callbacks={callbacks}
      />
    </div>
  );
};

export default WordCloud;
