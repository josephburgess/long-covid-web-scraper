import unittest
import responses
import json
from unittest.mock import MagicMock, patch
from src.scrapers import PubMedScraper
from .sample_html import (
    sample_pubmed_html,
    sample_pubmed_html_no_abstract,
    sample_pubmed_html_multi_para_abstract,
    sample_pubmed_html_no_citation,
)


def mock_summarise_text(text):
    return "Sample summary"


class TestPubMedScraper:
    @responses.activate
    def test_fetch_html_pubmed(self):
        url = "https://pubmed.ncbi.nlm.nih.gov/?term=long+covid"
        responses.add(responses.GET, url, body=sample_pubmed_html, status=200)

        pubmed_scraper = PubMedScraper()
        html_content = pubmed_scraper.fetch_html(url)

        assert html_content is not None
        assert "results-article" in html_content

    @responses.activate
    def test_fetch_html_pubmed_failed_request(self):
        url = "https://pubmed.ncbi.nlm.nih.gov/?term=long+covid"
        responses.add(responses.GET, url, status=404)

        pubmed_scraper = PubMedScraper()
        html_content = pubmed_scraper.fetch_html(url)

        assert html_content is None

    def test_parse_pubmed(self):
        pubmed_scraper = PubMedScraper()
        articles = pubmed_scraper.parse_html(sample_pubmed_html)

        assert len(articles) == 1
        assert articles[0]["title"] == "Sample Article Title"
        assert articles[0]["authors"] == "John Doe, Jane Smith"
        assert articles[0]["publication_date"] == "Jan 01, 2022"
        assert articles[0]["publication_date"] == "Jan 01, 2022"
        assert articles[0]["abstract"] == "Sample abstract text"

    def test_parse_pubmed_no_abstract(self, monkeypatch):
        monkeypatch.setattr("src.clients.summarise_text", mock_summarise_text)
        pubmed_scraper = PubMedScraper()
        articles = pubmed_scraper.parse_html(sample_pubmed_html_no_abstract)

        assert len(articles) == 1
        assert articles[0]["title"] == "Sample Article Title"
        assert articles[0]["authors"] == "John Doe, Jane Smith"
        assert articles[0]["publication_date"] == "Jan 01, 2022"
        assert articles[0]["abstract"] == ""

    def test_parse_pubmed_multi_para_abstract(self, monkeypatch):
        monkeypatch.setattr("src.clients.summarise_text", mock_summarise_text)
        pubmed_scraper = PubMedScraper()
        articles = pubmed_scraper.parse_html(sample_pubmed_html_multi_para_abstract)

        assert len(articles) == 1
        assert articles[0]["title"] == "Sample Article Title"
        assert articles[0]["authors"] == "John Doe, Jane Smith"
        assert articles[0]["publication_date"] == "Jan 01, 2022"
        assert (
            articles[0]["abstract"]
            == "Sample abstract text Another paragraph of abstract"
        )

    def test_parse_pubmed_no_citation(self, monkeypatch):
        monkeypatch.setattr("src.clients.summarise_text", mock_summarise_text)
        pubmed_scraper = PubMedScraper()
        articles = pubmed_scraper.parse_html(sample_pubmed_html_no_citation)

        assert len(articles) == 1
        assert articles[0]["title"] == "Sample Article Title"
        assert articles[0]["authors"] == "John Doe, Jane Smith"
        assert articles[0]["publication_date"] == ""
        assert articles[0]["abstract"] == "Sample abstract text"


if __name__ == "__main__":
    unittest.main()
