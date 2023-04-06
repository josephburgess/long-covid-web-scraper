import unittest
import responses
from src.scrapers import PubMedScraper, BMJScraper, LancetScraper
from .sample_html import sample_pubmed_html, sample_bmj_html, sample_lancet_html


class TestPubMedScraper(unittest.TestCase):
    @responses.activate
    def test_fetch_html_pubmed(self):
        url = 'https://pubmed.ncbi.nlm.nih.gov/?term=long+covid'
        responses.add(responses.GET, url, body=sample_pubmed_html, status=200)

        pubmed_scraper = PubMedScraper()
        html_content = pubmed_scraper.fetch_html(url)

        assert html_content is not None
        assert 'docsum-content' in html_content

    def test_parse_pubmed(self):
        pubmed_scraper = PubMedScraper()
        articles = pubmed_scraper.parse_pubmed(sample_pubmed_html)

        assert len(articles) == 1
        assert articles[0]['title'] == 'Sample Article Title'
        assert articles[0]['authors'] == 'John Doe, Jane Smith'
        assert articles[0]['publication_date'] == 'Jan 01, 2022'


class TestBMJScraper(unittest.TestCase):
    @responses.activate
    def test_fetch_html_BMJ(self):
        url = 'https://www.bmj.com/search/advanced/title%3Along%2Bcovid'
        responses.add(responses.GET, url, body=sample_bmj_html, status=200)

        bmj_scraper = BMJScraper()
        html_content = bmj_scraper.fetch_html(url)

        assert html_content is not None
        assert 'highwire-article-citation' in html_content

    def test_parse_BMJ(self):
        bmj_scraper = BMJScraper()
        articles = bmj_scraper.parse_bmj(sample_bmj_html)

        assert len(articles) == 1
        assert articles[0]['title'] == 'Sample Article Title'
        assert articles[0]['authors'] == 'John Doe'
        assert articles[0]['publication_date'] == 'Mar 01, 2023'


class TestLancetScraper(unittest.TestCase):
    @responses.activate
    def test_fetch_html_lancet(self):
        url = 'https://www.thelancet.com/action/doSearch?text1=long+covid&field1=Title&journalCode=lancet&SeriesKey=lancet'
        responses.add(responses.GET, url, body=sample_lancet_html, status=200)

        lancet_scraper = LancetScraper()
        html_content = lancet_scraper.fetch_html(url)

        assert html_content is not None
        assert 'search__item' in html_content

    def test_parse_lancet(self):
        lancet_scraper = LancetScraper()
        articles = lancet_scraper.parse_lancet(sample_lancet_html)

        assert len(articles) == 2
        assert articles[0]['title'] == 'Long COVID: 3 years in'
        assert articles[0]['authors'] == 'The Lancet'
        assert articles[0]['publication_date'] == '11 Mar 2023'
        assert articles[1]['title'] == 'Healing Long Covid: a marathon not a sprint'
        assert articles[1]['authors'] == 'Nisreen A Alwan'
        assert articles[1]['publication_date'] == '4 Mar 2023'


if __name__ == '__main__':
    unittest.main()
