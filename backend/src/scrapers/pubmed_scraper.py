from .base_scraper import Scraper
from bs4 import BeautifulSoup
from src.clients import summariseText


class PubMedScraper(Scraper):
    def __init__(self):
        self.base_url = "https://pubmed.ncbi.nlm.nih.gov/"
        self.query = '?term=%28"long+covid"%29&filter=simsearch1.fha&filter=pubt.booksdocs&filter=pubt.clinicaltrial&filter=pubt.meta-analysis&filter=pubt.randomizedcontrolledtrial&filter=pubt.review&filter=pubt.systematicreview&format=abstract&sort=date&size=50&page='

    def extract_title_and_url(self, container):
        title_tag = container.find("h1", class_="heading-title").find("a")
        title = title_tag.text.strip()
        url = "https://pubmed.ncbi.nlm.nih.gov" + title_tag["href"]
        return title, url

    def extract_authors(self, container):
        return container.find("span", class_="authors-list").text.strip()

    def extract_publication_date(self, container):
        citation_span = container.find("span", class_="cit")
        if citation_span:
            return citation_span.text.strip()
        return ""

    def extract_abstract(self, container):
        abstract = container.find("div", class_="abstract-content")
        if abstract:
            abstract_paragraphs = abstract.find_all("p")
            return " ".join(p.get_text(strip=True) for p in abstract_paragraphs)
        return ""

    def parse_html(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        articles = []

        article_containers = soup.find_all("div", class_="results-article")

        for container in article_containers:
            title, url = self.extract_title_and_url(container)
            authors = self.extract_authors(container)
            publication_date = self.extract_publication_date(container)
            abstract_text = self.extract_abstract(container)
            summary = summariseText(abstract_text)

            article = {
                "title": title,
                "url": url,
                "authors": authors,
                "publication_date": publication_date,
                "abstract": abstract_text,
                "summary": summary,
                "source": "pubmed",
            }
            articles.append(article)

        return articles

    def scrape(self, max_pages=1):
        all_articles = []

        for page_num in range(1, max_pages + 1):
            print("Scraping page", page_num, "of", max_pages, "via PubMed...")
            url = f"{self.base_url}{self.query}{page_num}"
            html_content = self.fetch_html(url)

            if html_content:
                articles = self.parse_html(html_content)
                all_articles.extend(articles)
                print("Found", len(articles), "articles")
            else:
                break

        return all_articles
