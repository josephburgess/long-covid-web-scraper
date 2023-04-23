import requests
from abc import ABC


class Scraper(ABC):
    def fetch_html(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None

    def scrape(self):
        html_content = self.fetch_html(self.base_url + self.query)

        if html_content:
            articles = self.parse_html(html_content)
        else:
            articles = []

        return articles
