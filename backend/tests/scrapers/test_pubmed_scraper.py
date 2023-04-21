import pytest
import responses
from src.scrapers import PubMedScraper
from .mocks import (
    sample_pubmed_html,
    sample_pubmed_html_no_abstract,
    sample_pubmed_html_multi_para_abstract,
    sample_pubmed_html_no_citation,
    pubmed_url,
    mock_summarise_text,
)


@pytest.fixture
def pubmed_scraper():
    return PubMedScraper()


@responses.activate
def test_fetch_html_pubmed(pubmed_scraper):
    responses.add(responses.GET, pubmed_url, body=sample_pubmed_html, status=200)
    html_content = pubmed_scraper.fetch_html(pubmed_url)

    assert html_content is not None
    assert "results-article" in html_content


@responses.activate
def test_fetch_html_pubmed_failed_request(pubmed_scraper):
    responses.add(responses.GET, pubmed_url, status=404)
    html_content = pubmed_scraper.fetch_html(pubmed_url)

    assert html_content is None


@responses.activate
def test_scrape_pubmed(pubmed_scraper, monkeypatch):
    monkeypatch.setattr("src.clients.summarise_text", mock_summarise_text)
    responses.add(responses.GET, pubmed_url, body=sample_pubmed_html, status=200)

    summary_api_url = "https://api.smrzr.io/v1/summarize?&num_sentences=5"
    summary_response = {"summary": "Sample summary"}
    responses.add(responses.POST, summary_api_url, json=summary_response, status=200)

    articles = pubmed_scraper.scrape(max_pages=1)

    assert len(articles) == 1
    assert articles[0]["title"] == "Sample Article Title"
    assert articles[0]["authors"] == "John Doe, Jane Smith"
    assert articles[0]["publication_date"] == "Jan 01, 2022"
    assert articles[0]["abstract"] == "Sample abstract text"


def test_parse_pubmed_no_abstract(pubmed_scraper, monkeypatch):
    monkeypatch.setattr("src.clients.summarise_text", mock_summarise_text)
    articles = pubmed_scraper.parse_html(sample_pubmed_html_no_abstract)

    assert len(articles) == 1
    assert articles[0]["abstract"] == ""


def test_parse_pubmed_multi_para_abstract(pubmed_scraper, monkeypatch):
    monkeypatch.setattr("src.clients.summarise_text", mock_summarise_text)
    articles = pubmed_scraper.parse_html(sample_pubmed_html_multi_para_abstract)

    assert len(articles) == 1
    assert (
        articles[0]["abstract"] == "Sample abstract text Another paragraph of abstract"
    )


def test_parse_pubmed_no_citation(pubmed_scraper, monkeypatch):
    monkeypatch.setattr("src.clients.summarise_text", mock_summarise_text)
    articles = pubmed_scraper.parse_html(sample_pubmed_html_no_citation)

    assert len(articles) == 1
    assert articles[0]["publication_date"] == ""
