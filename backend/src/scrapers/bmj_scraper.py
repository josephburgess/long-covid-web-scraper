from .base_scraper import Scraper
from bs4 import BeautifulSoup


class BMJScraper(Scraper):
    def __init__(self):
        self.base_url = "https://www.bmj.com/search/advanced/"
        self.query = "title%3Along%2Bcovid%20title_flags%3Amatch-all%20numresults%3A100%20sort%3Apublication-date%20direction%3Adescending%20format_result%3Astandard"

    def extract_title_and_url(self, container):
        title_tag = container.find("a", class_="highwire-cite-linked-title")
        title = title_tag.text.strip()
        url = "http://www.bmj.com" + title_tag["href"]
        return title, url

    def extract_authors(self, container):
        authors_list = container.find_all(
            "span", {"class": ["nlm-given-names", "nlm-surname"]}
        )
        return " ".join([author.text for author in authors_list])

    def extract_publication_date(self, container):
        return container.find_all("span", class_="highwire-cite-metadata-date")[
            1
        ].text.strip()

    def parse_html(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        articles = []

        article_containers = soup.find_all("div", class_="highwire-article-citation")

        for container in article_containers:
            title, url = self.extract_title_and_url(container)
            authors = self.extract_authors(container)
            publication_date = self.extract_publication_date(container)

            article = {
                "title": title,
                "url": url,
                "authors": authors,
                "publication_date": publication_date,
                "source": "BMJ",
            }

            articles.append(article)

        return articles
