// hooks/useProcessedYearPublishedData.ts
import { useState, useEffect } from 'react';
import { fetchResearchArticleData } from '../services/dataApi';
import { ResearchArticleInterface } from '../types/ResearchArticleInterface';
import { schemeSet2 } from 'd3-scale-chromatic';

export const useProcessedYearPublishedData = () => {
  const [traces, setTraces] = useState<Plotly.Data[]>([]);

  useEffect(() => {
    const processData = async () => {
      const data = await fetchResearchArticleData();
      const sources = Array.from(
        new Set(data.map((article: ResearchArticleInterface) => article.source))
      );

      const processedTraces: Plotly.Data[] = sources.map((source, i) => {
        const sourceData = data.filter(
          (article: ResearchArticleInterface) => article.source === source
        );

        const years = sourceData.reduce(
          (acc: Record<string, number>, article: ResearchArticleInterface) => {
            const year = article.publication_date.split('-')[0];
            acc[year] = (acc[year] || 0) + 1;
            return acc;
          },
          {}
        );

        return {
          x: Object.keys(years),
          y: Object.values(years),
          type: 'bar',
          name: source,
          marker: { color: schemeSet2[i] },
        };
      });

      setTraces(processedTraces);
    };

    processData();
  }, []);

  return traces;
};
