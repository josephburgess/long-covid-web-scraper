import { useEffect } from 'react';
import * as Plotly from 'plotly.js-dist';

export const useDrawPlot = (
  plotRef: React.RefObject<HTMLDivElement>,
  traces: Plotly.Data[],
  layout: Partial<Plotly.Layout>
) => {
  useEffect(() => {
    if (plotRef.current && traces.length > 0) {
      Plotly.newPlot(plotRef.current, traces, layout);
    }
  }, [plotRef, traces, layout]);
};
