import { useState, useEffect } from 'react';
import { fetchYearPublishedArticleData } from '../services/dataApi';
import { schemeSet2 } from 'd3-scale-chromatic';
import { ResearchArticleInterface } from '../types/ResearchArticleInterface';

export const useYearPublishedData = () => {
  const [data, setData] = useState<Plotly.Data[]>([]);

  const processArticleData = (data: ResearchArticleInterface[]) => {
    const sources = Array.from(
      new Set(data.map((article: ResearchArticleInterface) => article.source))
    );

    return sources.map((source, i) => {
      const sourceData = data.filter(
        (article: ResearchArticleInterface) => article.source === source
      );

      const years = sourceData.reduce(
        (acc: Record<string, number>, article: ResearchArticleInterface) => {
          const year = new Date(article.publication_date)
            .getFullYear()
            .toString();
          acc[year] = (acc[year] || 0) + 1;
          return acc;
        },
        {}
      );

      return {
        x: Object.keys(years),
        y: Object.values(years),
        type: 'bar' as const,
        name: source,
        marker: { color: schemeSet2[i] },
      };
    });
  };

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
