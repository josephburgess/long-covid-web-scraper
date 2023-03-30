import requests


class Scraper:
    def fetch_html(self, url):
        response = requests.get(url)
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            return response.text
        return None

    def scrape(self):
        raise NotImplementedError("Subclasses must implement this method")
