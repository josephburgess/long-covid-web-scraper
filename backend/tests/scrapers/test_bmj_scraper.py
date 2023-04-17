import unittest
import responses
from src.scrapers import BMJScraper
from .sample_html import sample_bmj_html


class TestBMJScraper(unittest.TestCase):
    @responses.activate
    def test_fetch_html_BMJ(self):
        url = "https://www.bmj.com/search/advanced/title%3Along%2Bcovid"
        responses.add(responses.GET, url, body=sample_bmj_html, status=200)

        bmj_scraper = BMJScraper()
        html_content = bmj_scraper.fetch_html(url)

        assert html_content is not None
        assert "highwire-article-citation" in html_content

    def test_parse_html_BMJ(self):
        bmj_scraper = BMJScraper()
        articles = bmj_scraper.parse_html(sample_bmj_html)

        assert len(articles) == 1
        assert articles[0]["title"] == "Sample Article Title"
        assert articles[0]["authors"] == "John Doe"
        assert articles[0]["publication_date"] == "Mar 01, 2023"


if __name__ == "__main__":
    unittest.main()
