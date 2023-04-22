import * as Plotly from 'plotly.js';
import { ResearchArticleInterface } from '../types/ResearchArticleInterface';
import { schemeSet2 } from 'd3-scale-chromatic';

export const getLayout = (uniqueYears: number[]): Partial<Plotly.Layout> => ({
  title: 'Publication Tracker',
  xaxis: {
    title: 'Year',
    tickmode: 'array',
    tickvals: uniqueYears,
    ticktext: uniqueYears.map(String),
    ticklen: 5,
    tickwidth: 2,
    tickcolor: '#000',
  },
  yaxis: { title: 'Number of Articles' },
  barmode: 'stack',
});

export const processArticleData = (data: ResearchArticleInterface[]) => {
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
      x: Object.keys(years).map(Number),
      y: Object.values(years),
      type: 'bar' as const,
      name: source,
      marker: { color: schemeSet2[i] },
    };
  });
};
