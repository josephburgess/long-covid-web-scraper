import pytest
import responses
from src.scrapers import BMJScraper
from .mocks import sample_bmj_html, bmj_url


@pytest.fixture
def bmj_scraper():
    return BMJScraper()


@responses.activate
def test_fetch_html_BMJ(bmj_scraper):
    responses.add(responses.GET, bmj_url, body=sample_bmj_html, status=200)

    html_content = bmj_scraper.fetch_html(bmj_url)

    assert html_content is not None
    assert "highwire-article-citation" in html_content


@responses.activate
def test_scrape_BMJ(bmj_scraper):
    responses.add(responses.GET, bmj_url, body=sample_bmj_html, status=200)

    articles = bmj_scraper.scrape()

    assert len(articles) == 1
    assert articles[0]["title"] == "Sample Article Title"
    assert articles[0]["authors"] == "John Doe"
    assert articles[0]["publication_date"] == "Mar 01, 2023"


@responses.activate
def test_scrape_BMJ_no_html(bmj_scraper):
    responses.add(responses.GET, bmj_url, body=None, status=200)

    articles = bmj_scraper.scrape()

    assert articles == []
