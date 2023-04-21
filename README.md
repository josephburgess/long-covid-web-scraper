<p align="center">
_This project is still being built, however it is deployed on Render so that changes can be viewed on a live site in realtime. Please feel free to have a browse [here](https://long-covid-hub.onrender.com/), but note that it is still a work in progress!_

[![main](https://github.com/josephburgess/long-covid-web-scraper/actions/workflows/main.yml/badge.svg)](https://github.com/josephburgess/long-covid-web-scraper/actions/workflows/main.yml) [![codecov](https://codecov.io/gh/josephburgess/long-covid-web-scraper/branch/main/graph/badge.svg?token=0OEO440FI9)](https://codecov.io/gh/josephburgess/long-covid-web-scraper) [![Maintainability](https://api.codeclimate.com/v1/badges/a188eab62b8fc975e22c/maintainability)](https://codeclimate.com/github/josephburgess/long-covid-web-scraper/maintainability)

</p>

# Long COVID Hub

This project is an information hub for research, news and social posts about Long Covid. It utilises several APIs and web scrapers built using Python to obtain information and display it to the user. 

## Technology
The project uses a Python/Flask backend and a TypeScript/React frontend, with MongoDB used to store scraped data.  Currently the hub has 3 sections, News, Data and Reddit Feed. News articles and Reddit posts are obtained using API calls to the respective services. 

The Research section visualizes data on long COVID articles from PubMed. The data is scraped from the PubMed website using BeautifulSoup which grabs the Title, Author, Date, and Abstract from the articles. The abstract is summarised using an AI model and stored in MongoDB, which is read by the Flask backend using Pandas. The backend serves the data as JSON, which is then fetched by the React frontend and visualized using Plotly. 

## Installation

To install the project, follow these steps:

1. Clone the repository:

2. Navigate into the project directory and install dependencies:

```bash
cd backend && pip install -r requirements.txt
cd ../frontend && npm install
```
3. Install MongoDB

   ```
   brew tap mongodb/brew
   brew install mongodb-community@5.0
   ```
4. Start MongoDB
   ```
   brew services start mongodb-community@5.0
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
npm run test
```



