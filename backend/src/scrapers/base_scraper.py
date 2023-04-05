import requests
from abc import ABC, abstractmethod


class Scraper(ABC):

    def fetch_html(self, url):
        response = requests.get(url)
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            return response.text
        return None

    @abstractmethod
    def scrape(self):
        pass
