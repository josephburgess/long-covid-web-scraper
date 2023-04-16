from .base_scraper import Scraper
from bs4 import BeautifulSoup


class PubMedScraper(Scraper):
    def __init__(self):
        self.base_url = "https://pubmed.ncbi.nlm.nih.gov/"
        self.query = '?term=%28"long+covid"%29&filter=simsearch1.fha&filter=pubt.booksdocs&filter=pubt.clinicaltrial&filter=pubt.meta-analysis&filter=pubt.randomizedcontrolledtrial&filter=pubt.review&filter=pubt.systematicreview&format=abstract&sort=date&size=50&page='

    def parse_pubmed(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        articles = []

        article_containers = soup.find_all("div", class_="results-article")

        for container in article_containers:
            title_tag = container.find("h1", class_="heading-title").find("a")
            title = title_tag.text.strip()
            url = "https://pubmed.ncbi.nlm.nih.gov" + title_tag["href"]

            authors = container.find("span", class_="authors-list").text.strip()

            citation_span = container.find("span", class_="cit")
            if citation_span:
                publication_date = citation_span.text.strip()
            else:
                publication_date = ""

            abstract = container.find("div", class_="abstract-content")
            if abstract:
                abstract_paragraphs = abstract.find_all("p")
                abstract_text = " ".join(
                    p.get_text(strip=True) for p in abstract_paragraphs
                )
            else:
                abstract_text = ""

            article = {
                "title": title,
                "url": url,
                "authors": authors,
                "publication_date": publication_date,
                "abstract": abstract_text,
                "source": "pubmed",
            }
            articles.append(article)

        return articles

    def scrape(self, max_pages=14):
        all_articles = []

        for page_num in range(1, max_pages + 1):
            print("Scraping page", page_num, "of", max_pages, "via PubMed...")
            url = f"{self.base_url}{self.query}{page_num}"
            html_content = self.fetch_html(url)

            if html_content:
                articles = self.parse_pubmed(html_content)
                all_articles.extend(articles)
                print("Found", len(articles), "articles")
            else:
                break

        return all_articles
