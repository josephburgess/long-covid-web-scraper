_This project is still being built, however it is deployed on Render so that changes can be viewed on a live site in realtime. Please feel free to have a browse [here](https://long-covid-hub.onrender.com/), but note that it is still a work in progress!_

# Long COVID Hub

This project is an information hub for research, news and social posts about Long Covid. It utilises several APIs and web scrapers built using Python to obtain information and display it to the user. 

## Technology
The project uses a Python/Flask backend and a TypeScript/React frontend, with MongoDB used to store scraped data.  Currently the hub has 3 sections, News, Data and Reddit Feed. News articles and Reddit posts are obtained using API calls to the respective services. 

The Research section visualizes data on long COVID articles from PubMed, the British Medical Journal (BMJ) and the Lancet. The data is scraped from the web using BeautifulSoup and stored in MongoDB, which is read by the Flask backend using Pandas. The backend serves the data as JSON, which is then fetched by the React frontend and visualized using Plotly. 

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

3. open http://localhost:3000/ in your web browser.

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



