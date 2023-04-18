import React, { useRef } from 'react';
import { useYearPublishedData } from '../../hooks/useYearPublishedData';
import { useDrawYearPublishedPlot } from '../../hooks/useDrawYearPublishedPlot';
import { getLayout } from '../../utils/graphUtils';

const YearPublishedGraph: React.FC = () => {
  const plotRef = useRef<HTMLDivElement>(null);
  const data = useYearPublishedData();
  const layout = getLayout();

  useDrawYearPublishedPlot(plotRef, data, layout);

  return <div ref={plotRef} data-cy="year-published-graph" />;
};

export default YearPublishedGraph;
