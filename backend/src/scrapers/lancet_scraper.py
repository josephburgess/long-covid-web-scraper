from scrapers import Scraper
from bs4 import BeautifulSoup


class LancetScraper(Scraper):
    def __init__(self):
        self.base_url = 'https://www.thelancet.com/action/doSearch'
        self.query = '?text1=long+covid&field1=Title&journalCode=lancet&SeriesKey=lancet'

    def parse_lancet(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = []

        # Find all article containers
        article_containers = soup.find_all('li', class_='search__item')

        for container in article_containers:
            if 'long covid' not in container.find('span', class_='hlFld-Title').text.lower():
                continue

            title_tag = container.find('a', href=True)
            title = title_tag.text.strip()
            url = "https://www.thelancet.com" + title_tag['href']

            authors = container.find(
                'ul', class_='meta__authors').text.strip()

            if authors == "The Lancet":
                authors = "Unattributed"

            publication_date = container.find(
                'span', id='item_date').text.strip()

            article = {
                'title': title,
                'url': url,
                'authors': authors,
                'publication_date': publication_date,
                'source': 'The Lancet'
            }

            articles.append(article)

        return articles

    def scrape(self):

        html_content = self.fetch_html(self.base_url + self.query)

        if html_content:
            articles = self.parse_lancet(html_content)
        else:
            articles = []

        return articles
