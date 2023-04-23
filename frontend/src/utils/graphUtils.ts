import * as Plotly from 'plotly.js';
import { ResearchArticleInterface } from '../types/ResearchArticleInterface';
import { schemeSet2 } from 'd3-scale-chromatic';

export const getUniqueSources = (
  data: ResearchArticleInterface[]
): string[] => {
  return Array.from(
    new Set(data.map((article: ResearchArticleInterface) => article.source))
  );
};

export const processTraces = (
  data: ResearchArticleInterface[],
  sources: string[]
): Plotly.Data[] => {
  return sources.map((source, i) => {
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
};
