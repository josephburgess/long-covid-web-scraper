from scraper import BMJScraper, PubMedScraper, update_csv_file
import pandas as pd


def main():
    scrapers = [
        PubMedScraper(),
        BMJScraper(),
    ]

    for scraper in scrapers:
        data = scraper.scrape()
        update_csv_file('data/raw/long_covid_articles.csv', data)


if __name__ == '__main__':
    main()
