import { useState, useEffect } from 'react';
import { fetchYearPublishedArticleData } from '../services/dataApi';
import { processArticleData } from '../utils/graphUtils';

export const useYearPublishedData = () => {
  const [data, setData] = useState<Plotly.Data[]>([]);

  useEffect(() => {
    const processData = async () => {
      const rawData = await fetchYearPublishedArticleData();
      const processedData = processArticleData(rawData);
      setData(processedData);
    };

    processData();
  }, []);

  return data;
};
