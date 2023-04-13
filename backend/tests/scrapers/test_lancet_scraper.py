import unittest
import responses
from src.scrapers import LancetScraper
from .sample_html import sample_lancet_html


class TestLancetScraper(unittest.TestCase):
    @responses.activate
    def test_fetch_html_lancet(self):
        url = "https://www.thelancet.com/action/doSearch?text1=long+covid&field1=Title&journalCode=lancet&SeriesKey=lancet"
        responses.add(responses.GET, url, body=sample_lancet_html, status=200)

        lancet_scraper = LancetScraper()
        html_content = lancet_scraper.fetch_html(url)

        assert html_content is not None
        assert "search__item" in html_content

    def test_parse_lancet(self):
        lancet_scraper = LancetScraper()
        articles = lancet_scraper.parse_lancet(sample_lancet_html)

        assert len(articles) == 2
        assert articles[0]["title"] == "Long COVID: 3 years in"
        assert articles[0]["authors"] == "Unattributed"
        assert articles[0]["publication_date"] == "11 Mar 2023"
        assert articles[1]["title"] == "Healing Long Covid: a marathon not a sprint"
        assert articles[1]["authors"] == "Nisreen A Alwan"
        assert articles[1]["publication_date"] == "4 Mar 2023"


if __name__ == "__main__":
    unittest.main()
