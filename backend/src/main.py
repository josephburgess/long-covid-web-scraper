from scrapers import BMJScraper, PubMedScraper, update_mongodb_collection
from data_processing import main as data_processing_main


def main():
    scrapers = [
        PubMedScraper(),
        BMJScraper(),
    ]

    for scraper in scrapers:
        data = scraper.scrape()
        update_mongodb_collection('articles', data)

    data_processing_main()


if __name__ == '__main__':
    main()
