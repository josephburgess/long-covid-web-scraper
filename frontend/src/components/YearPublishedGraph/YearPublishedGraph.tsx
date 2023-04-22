// YearPublishedGraph.tsx
import React, { useRef } from 'react';
import { useProcessedYearPublishedData } from '../../hooks/useProcessedYearPublishedData';
import { useDrawPlot } from '../../hooks/useDrawPlot';

const YearPublishedGraph: React.FC = () => {
  const plotRef = useRef<HTMLDivElement>(null);
  const traces = useProcessedYearPublishedData();

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

  useDrawPlot(plotRef, traces, layout);

  return <div ref={plotRef} data-cy='year-published-graph' />;
};

export default YearPublishedGraph;
