import React, { useEffect, useRef } from 'react';
import * as Plotly from 'plotly.js-dist';
import { schemeSet2 } from 'd3-scale-chromatic';
import { fetchYearPublishedArticleData } from '../../services/dataApi';

export interface YearPublishedArticle {
  source: string;
  publication_date: string;
}

const YearPublishedGraph: React.FC = () => {
  const plotRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const drawPlot = async () => {
      const data = await fetchYearPublishedArticleData();

      const sources = Array.from(
        new Set(data.map((article: YearPublishedArticle) => article.source))
      );

      const colors = schemeSet2.slice(0, sources.length);

      const traces: Plotly.Data[] = sources.map((source, i) => {
        const sourceData = data.filter(
          (article: YearPublishedArticle) => article.source === source
        );

        const years = sourceData.reduce((acc: Record<string, number>, article: YearPublishedArticle) => {
          const year = article.publication_date.split('-')[0];
          acc[year] = (acc[year] || 0) + 1;
          return acc;
        }, {});

        return {
          x: Object.keys(years),
          y: Object.values(years),
          type: 'bar',
          name: source,
          marker: { color: colors[i] },
        };
      });

      const layout: Partial<Plotly.Layout> = {
        title: 'Publication Tracker',
        xaxis: {
          title: 'Year',
          tickmode: 'linear',
          tick0: 0,
          dtick: 1,
          ticklen: 5,
          tickwidth: 2,
          tickcolor: '#000',
        },
        yaxis: { title: 'Number of Articles' },
        barmode: 'stack',
      };

      if (plotRef.current) {
        Plotly.newPlot(plotRef.current, traces, layout);
      }
    };

    drawPlot();
  }, []);

  return <div ref={plotRef} data-cy="year-published-graph" />;
};


export default YearPublishedGraph;
