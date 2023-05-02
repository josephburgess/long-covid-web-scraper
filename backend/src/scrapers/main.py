from src.scrapers import PubMedScraper
from src.database import DatabaseManager
from .processors.main import main as data_processing_main


def main():
    scraper = PubMedScraper()
    data = scraper.scrape()
    db_manager = DatabaseManager("articles")
    db_manager.update_collection(data)

    data_processing_main()


if __name__ == "__main__":
    main()
