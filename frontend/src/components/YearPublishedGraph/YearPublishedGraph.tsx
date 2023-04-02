import React, { useEffect, useRef } from 'react';
import * as Plotly from 'plotly.js-dist';
import { schemeSet2 } from 'd3-scale-chromatic';

interface Article {
  source: string;
  publication_date: string;
}

const YearPublishedGraph: React.FC = () => {
  const plotRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    fetch('/api/data')
      .then((response) => response.json())
      .then((data: Article[]) => {
        const sources = Array.from(
          new Set(data.map((article) => article.source))
        );

        const colors = schemeSet2.slice(0, sources.length);

        const traces: Plotly.Data[] = sources.map((source, i) => {
          const sourceData = data.filter(
            (article: Article) => article.source === source
          );

          const years = sourceData.reduce((acc: Record<string, number>, article: Article) => {
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
          title: 'Number of Long COVID Articles by Year',
          xaxis: {
            title: 'Year',
            tickmode: 'linear', // Change this line
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
      });
  }, []);

  return <div ref={plotRef} />;
};

export default YearPublishedGraph;
