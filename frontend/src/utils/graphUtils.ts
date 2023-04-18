import * as Plotly from 'plotly.js';

export const getLayout = (): Partial<Plotly.Layout> => ({
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
});
