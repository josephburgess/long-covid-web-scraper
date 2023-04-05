from scrapers import Scraper
from bs4 import BeautifulSoup


class PubMedScraper(Scraper):
    def __init__(self):
        self.base_url = 'https://pubmed.ncbi.nlm.nih.gov/'
        self.query = '?term=long+covid&page='

    def parse_pubmed(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = []

        # Find all article containers
        article_containers = soup.find_all('div', class_='docsum-content')

        for container in article_containers:
            title_tag = container.find('a', class_='docsum-title')
            title = title_tag.text.strip()
            url = "https://pubmed.ncbi.nlm.nih.gov" + title_tag['href']

            authors = container.find(
                'span', class_='docsum-authors').text.strip()

            publication_date = container.find(
                'span', class_='docsum-journal-citation').text.strip()

            article = {
                'title': title,
                'url': url,
                'authors': authors,
                'publication_date': publication_date,
                'source': 'pubmed'
            }

            articles.append(article)

        return articles

    def scrape(self, max_pages=5):
        all_articles = []

        for page_num in range(1, max_pages + 1):
            url = f"{self.base_url}{self.query}{page_num}"
            html_content = self.fetch_html(url)

            if html_content:
                articles = self.parse_pubmed(html_content)
                all_articles.extend(articles)
            else:
                break

        return all_articles
