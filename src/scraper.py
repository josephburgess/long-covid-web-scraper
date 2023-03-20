import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scraper:
    def fetch_html(self, url):
        response = requests.get(url)
        print(f"Status code: {response.status_code}")
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
        article_containers = soup.find_all('div', class_='docsum-content')

        for container in article_containers:
            title = container.find('a', class_='docsum-title').text.strip()

            authors = container.find(
                'span', class_='docsum-authors').text.strip()

            publication_date = container.find(
                'span', class_='docsum-journal-citation').text.strip()

            article = {
                'title': title,
                'authors': authors,
                'publication_date': publication_date,
            }

            articles.append(article)

        return articles

    def scrape(self, max_pages=5):
        base_url = 'https://pubmed.ncbi.nlm.nih.gov/'
        query = '?term=long+covid&page='
        all_articles = []

        for page_num in range(1, max_pages + 1):
            url = f"{base_url}{query}{page_num}"
            html_content = self.fetch_html(url)

            if html_content:
                articles = self.parse_pubmed(html_content)
                all_articles.extend(articles)
            else:
                break

        return all_articles


def main():
    scrapers = [
        PubMedScraper(),
    ]

    for scraper in scrapers:
        data = scraper.scrape()
        df = pd.DataFrame(data)
        df.to_csv('data/long_covid_articles.csv', index=False)


if __name__ == '__main__':
    main()
