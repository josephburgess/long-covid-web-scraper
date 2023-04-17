from .base_scraper import Scraper
from bs4 import BeautifulSoup


class LancetScraper(Scraper):
    def __init__(self):
        self.base_url = "https://www.thelancet.com/action/doSearch"
        self.query = (
            "?text1=long+covid&field1=Title&journalCode=lancet&SeriesKey=lancet"
        )

    def extract_title_and_url(self, container):
        title_tag = container.find("a", href=True)
        title = title_tag.text.strip()
        url = "https://www.thelancet.com" + title_tag["href"]
        return title, url

    def extract_authors(self, container):
        authors = container.find("ul", class_="meta__authors").text.strip()

        if authors == "The Lancet":
            return "Unattributed"
        return authors

    def extract_publication_date(self, container):
        return container.find("span", id="item_date").text.strip()

    def parse_html(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        articles = []

        article_containers = soup.find_all("li", class_="search__item")

        for container in article_containers:
            if (
                "long covid"
                not in container.find("span", class_="hlFld-Title").text.lower()
            ):
                continue

            title, url = self.extract_title_and_url(container)
            authors = self.extract_authors(container)
            publication_date = self.extract_publication_date(container)

            article = {
                "title": title,
                "url": url,
                "authors": authors,
                "publication_date": publication_date,
                "source": "The Lancet",
            }

            articles.append(article)

        return articles

    def scrape(self):
        html_content = self.fetch_html(self.base_url + self.query)

        if html_content:
            articles = self.parse_html(html_content)
        else:
            articles = []

        return articles
