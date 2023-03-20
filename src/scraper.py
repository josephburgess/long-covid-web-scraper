import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scraper:
    def fetch_html(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None

    def scrape(self):
        raise NotImplementedError("Subclasses must implement this method")


class PubMedScraper(Scraper):
    def parse_pubmed(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = []

        # Find all article containers
        article_containers = soup.find_all('div', class_='pubmed-docsum')

        for container in article_containers:
            # Extract the title
            title = container.find('a', class_='docsum-title').text.strip()

            # Extract authors
            authors = container.find(
                'span', class_='docsum-authors').text.strip()

            # Extract the publication date
            publication_date = container.find(
                'span', class_='docsum-journal-citation').text.strip()

            # Save the extracted data in a dictionary
            article = {
                'title': title,
                'authors': authors,
                'publication_date': publication_date
            }

            articles.append(article)

        return articles

    def scrape(self):
        url = 'https://pubmed.ncbi.nlm.nih.gov/?term=long+covid'
        html_content = self.fetch_html(url)
        if html_content:
            return self.parse_pubmed(html_content)
        return []
