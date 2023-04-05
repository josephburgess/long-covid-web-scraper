from scrapers import BMJScraper, PubMedScraper, LancetScraper, DatabaseManager
from data_processing import main as data_processing_main


def main():
    scrapers = [
        PubMedScraper(),
        BMJScraper(),
        LancetScraper()
    ]

    for scraper in scrapers:
        data = scraper.scrape()
        db_manager = DatabaseManager('articles')
        db_manager.update_collection(data)

    data_processing_main()


if __name__ == '__main__':
    main()
