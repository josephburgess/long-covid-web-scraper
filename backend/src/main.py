from scrapers import BMJScraper, PubMedScraper, update_mongodb_collection
import pandas as pd


def main():
    scrapers = [
        PubMedScraper(),
        BMJScraper(),
    ]

    for scraper in scrapers:
        data = scraper.scrape()
        update_mongodb_collection('articles', data)


if __name__ == '__main__':
    main()
