document.addEventListener('DOMContentLoaded', function () {
  fetch('/data')
    .then((response) => response.json())
    .then((data) => {
      const years = data.reduce((acc, article) => {
        const year = article.publication_date.split('-')[0];
        acc[year] = (acc[year] || 0) + 1;
        return acc;
      }, {});

      const trace = {
        x: Object.keys(years),
        y: Object.values(years),
        type: 'bar',
      };

      const layout = {
        title: 'Number of Long COVID Articles by Year',
        xaxis: { title: 'Year' },
        yaxis: { title: 'Number of Articles' },
      };

      Plotly.newPlot('plot', [trace], layout);
    });
});
