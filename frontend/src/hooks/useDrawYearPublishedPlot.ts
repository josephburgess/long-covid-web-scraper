// hooks/
import { useEffect } from 'react';
import * as Plotly from 'plotly.js-dist';

export const useDrawYearPublishedPlot = (
  plotRef: React.RefObject<HTMLDivElement>,
  data: Plotly.Data[],
  layout: Partial<Plotly.Layout>
) => {
  useEffect(() => {
    if (plotRef.current) {
      Plotly.newPlot(plotRef.current, data, layout);
    }
  }, [plotRef, data, layout]);
};
