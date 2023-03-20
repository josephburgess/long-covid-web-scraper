import pytest
import responses
from src.scraper import PubMedScraper

sample_pubmed_html = '''
<div class="docsum-content">
    <a class="docsum-title" href="/12345678/">Sample Article Title</a>
    <span class="docsum-authors">John Doe, Jane Smith</span>
    <span class="docsum-journal-citation">Jan 01, 2022</span>
</div>
'''


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
