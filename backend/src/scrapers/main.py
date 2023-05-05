from src.scrapers import PubMedScraper
from src.database import DatabaseManager
from src.scrapers.processors.main import run_processors
from src.scrapers import setup_warnings_and_loggers


setup_warnings_and_loggers()


def main():
    scraper = PubMedScraper()
    data = scraper.scrape()
    db_manager = DatabaseManager("articles")
    db_manager.update_collection(data)

    run_processors()


if __name__ == "__main__":
    main()
