# Long COVID Articles Visualization

This project visualizes data on long COVID articles from PubMed and the British Medical Journal (BMJ) using a Python/Flask backend and a React frontend. The data is scraped from the web using BeautifulSoup and stored in a CSV file, which is read into the Flask backend using Pandas. The backend serves the data as JSON, which is then fetched by the React frontend and visualized using Plotly.

## Installation

To install the project, follow these steps:

1. Clone the repository:

2. Navigate into the project directory and install dependencies:

```bash
cd backend && pip install -r requirements.txt
cd ../frontend && npm install
```


## Usage

1. To start the backend, run:

```bash
cd backend && flask run
```


2. To start the frontend, run:

```bash
cd frontend && npm start
```

3. open http://localhost:3000/ in your web browser to view the visualization.

## Testing

To run the backend tests, run:

```bash
cd backend
pytest
```

To run the frontend tests, run:

```bash
cd frontend
npm run cypress
```



