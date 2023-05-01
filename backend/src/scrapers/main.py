from src.scrapers import PubMedScraper
from src.database import DatabaseManager
from .data_processor import main as data_processor


def main():
    scraper = PubMedScraper()
    data = scraper.scrape()
    db_manager = DatabaseManager("articles")
    db_manager.update_collection(data)

    data_processor()


if __name__ == "__main__":
    main()
