import requests
import os
import logging
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


class GuardianClient:
    def __init__(self):
        self.api_key = os.getenv("GUARDIAN_API_KEY")
        self.base_url = "https://content.guardianapis.com/"

    def search_news(self, query):
        try:
            response = self._fetch_search_results(query)
            results = self._parse_search_results(response)
            return results
        except Exception as e:
            logging.exception(f"Error searching news: {e}")
            return None

    def _fetch_search_results(self, query):
        url = f"{self.base_url}search"
        params = {
            "section": "society",
            "q": query,
            "page-size": 40,
            "query-fields": "headline",
            "show-fields": "thumbnail,headline,byline,standfirst,bodyText",
            "order-by": "newest",
            "api-key": self.api_key,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def _parse_search_results(self, data):
        results = data["response"]["results"]
        return [
            {
                "webUrl": result["webUrl"],
                "headline": result["fields"]["headline"],
                "thumbnail": result["fields"].get("thumbnail", ""),
                "standfirst": self._clean_standfirst(
                    result["fields"].get("standfirst", "")
                ),
                "date": result["webPublicationDate"],
            }
            for result in results
        ]

    @staticmethod
    def _clean_standfirst(standfirst: str) -> str:
        soup = BeautifulSoup(standfirst, "html.parser")
        for ul in soup.find_all("ul"):
            ul.decompose()
        return soup.get_text(strip=True)
