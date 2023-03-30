import pytest
import responses
from src.scrapers import PubMedScraper, BMJScraper
from .sample_html import sample_pubmed_html, sample_bmj_html


@responses.activate
def test_fetch_html_pubmed():
    url = 'https://pubmed.ncbi.nlm.nih.gov/?term=long+covid'
    responses.add(responses.GET, url, body=sample_pubmed_html, status=200)

    pubmed_scraper = PubMedScraper()
    html_content = pubmed_scraper.fetch_html(url)

    assert html_content is not None
    assert 'docsum-content' in html_content


def test_parse_pubmed():
    pubmed_scraper = PubMedScraper()
    articles = pubmed_scraper.parse_pubmed(sample_pubmed_html)

    assert len(articles) == 1
    assert articles[0]['title'] == 'Sample Article Title'
    assert articles[0]['authors'] == 'John Doe, Jane Smith'
    assert articles[0]['publication_date'] == 'Jan 01, 2022'


def test_fetch_html_BMJ():
    url = 'https://www.bmj.com/search/advanced/title%3Along%2Bcovid'
    responses.add(responses.GET, url, body=sample_bmj_html, status=200)

    bmj_scraper = BMJScraper()
    html_content = bmj_scraper.fetch_html(url)

    assert html_content is not None
    assert 'highwire-article-citation' in html_content


def test_parse_BMJ():
    bmj_scraper = BMJScraper()
    articles = bmj_scraper.parse_bmj(sample_bmj_html)

    assert len(articles) == 1
    assert articles[0]['title'] == 'Sample Article Title'
    assert articles[0]['authors'] == 'John Doe'
    assert articles[0]['publication_date'] == 'Mar 01, 2023'
