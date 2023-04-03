from scrapers import Scraper
from bs4 import BeautifulSoup


class BMJScraper(Scraper):
    def parse_bmj(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = []

        article_containers = soup.find_all(
            'div', class_='highwire-article-citation')

        for container in article_containers:
            title_tag = container.find(
                'a', class_='highwire-cite-linked-title')
            title = title_tag.text.strip()
            url = "http://www.bmj.com" + title_tag['href']

            authors_list = container.find_all(
                'span', {'class': ['nlm-given-names', 'nlm-surname']})
            authors = ' '.join([author.text for author in authors_list])

            publication_date = container.find_all(
                'span', class_='highwire-cite-metadata-date')[1].text.strip()

            article = {
                'title': title,
                'url': url,
                'authors': authors,
                'publication_date': publication_date,
                'source': 'BMJ'
            }

            articles.append(article)

        return articles

    def scrape(self, max_pages=5):

        base_url = "https://www.bmj.com/search/advanced/"
        query = "title%3Along%2Bcovid%20title_flags%3Amatch-all%20limit_from%3A1840-01-01%20limit_to%3A2023-03-20%20numresults%3A10%20sort%3Arelevance-rank%20format_result%3Astandard?page="
        all_articles = []

        for page_num in range(1, max_pages + 1):
            url = f"{base_url}{query}{page_num}"
            html_content = self.fetch_html(url)

            if html_content:
                articles = self.parse_bmj(html_content)
                all_articles.extend(articles)
            else:
                break

        return all_articles
