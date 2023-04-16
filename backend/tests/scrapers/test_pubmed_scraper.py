import unittest
import responses
from src.scrapers import PubMedScraper
from .sample_html import sample_pubmed_html


class TestPubMedScraper(unittest.TestCase):
    @responses.activate
    def test_fetch_html_pubmed(self):
        url = "https://pubmed.ncbi.nlm.nih.gov/?term=long+covid"
        responses.add(responses.GET, url, body=sample_pubmed_html, status=200)

        pubmed_scraper = PubMedScraper()
        html_content = pubmed_scraper.fetch_html(url)

        assert html_content is not None
        assert "results-article" in html_content

    def test_parse_pubmed(self):
        pubmed_scraper = PubMedScraper()
        articles = pubmed_scraper.parse_pubmed(sample_pubmed_html)

        assert len(articles) == 1
        assert articles[0]["title"] == "Sample Article Title"
        assert articles[0]["authors"] == "John Doe, Jane Smith"
        assert articles[0]["publication_date"] == "Jan 01, 2022"
        assert articles[0]["abstract"] == "Sample abstract text"


if __name__ == "__main__":
    unittest.main()
