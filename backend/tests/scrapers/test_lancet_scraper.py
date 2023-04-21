import pytest
import responses
from src.scrapers import LancetScraper
from .mocks import sample_lancet_html, lancet_url


@pytest.fixture
def lancet_scraper():
    return LancetScraper()


@responses.activate
def test_fetch_html_lancet(lancet_scraper):
    responses.add(responses.GET, lancet_url, body=sample_lancet_html, status=200)
    html_content = lancet_scraper.fetch_html(lancet_url)

    assert html_content is not None
    assert "search__item" in html_content


@responses.activate
def test_scrape_lancet(lancet_scraper):
    responses.add(responses.GET, lancet_url, body=sample_lancet_html, status=200)

    articles = lancet_scraper.scrape()

    assert len(articles) == 2
    assert articles[0]["title"] == "Long COVID: 3 years in"
    assert articles[0]["authors"] == "Unattributed"
    assert articles[0]["publication_date"] == "11 Mar 2023"
    assert articles[1]["title"] == "Healing Long Covid: a marathon not a sprint"
    assert articles[1]["authors"] == "Nisreen A Alwan"
    assert articles[1]["publication_date"] == "4 Mar 2023"
