import React, { useState, useEffect } from 'react';
import ReactWordCloud, { Options } from 'react-wordcloud';
import axios from 'axios';

import 'tippy.js/dist/tippy.css';
import 'tippy.js/animations/scale.css';

interface Word {
  text: string;
  value: number;
}

const WordCloud: React.FC = () => {
  const [wordData, setWordData] = useState<Word[]>([]);

  useEffect(() => {
    const fetchWordData = async () => {
      try {
        const response = await axios.get<Word[]>('/api/wordcloud');
        setWordData(response.data);
      } catch (error) {
        console.error('Error fetching wordcloud data:', error);
      }
    };

    fetchWordData();
  }, []);

  const options: Partial<Options> = {
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

  return (
    <div style={{ width: '100%', height: '400px' }}>
      <ReactWordCloud options={options} words={wordData} />
    </div>
  );
};

export default WordCloud;
