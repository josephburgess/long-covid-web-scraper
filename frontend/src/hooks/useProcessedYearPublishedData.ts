// hooks/useProcessedYearPublishedData.ts
import { useState, useEffect } from 'react';
import { fetchResearchArticleData } from '../services/dataApi';
import { getUniqueSources, processTraces } from '../utils/graphUtils';

export const useProcessedYearPublishedData = () => {
  const [traces, setTraces] = useState<Plotly.Data[]>([]);

  useEffect(() => {
    const processData = async () => {
      const data = await fetchResearchArticleData();
      const sources = getUniqueSources(data);
      const processedTraces = processTraces(data, sources);
      setTraces(processedTraces);
    };

    processData();
  }, []);

  return traces;
};
