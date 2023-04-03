import requests
import os
import logging
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


class GuardianClient:
    def __init__(self):
        self.api_key = os.getenv('GUARDIAN_API_KEY')
        self.base_url = 'https://content.guardianapis.com/'

    def search_news(self, query):
        url = f'{self.base_url}search'
        params = {
            'section': 'society',
            'q': query,
            'page-size': 40,
            'query-fields': 'headline',
            'show-fields': 'thumbnail,headline,byline,standfirst,bodyText',
            'order-by': 'newest',
            'api-key': self.api_key
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            results = data['response']['results']
            output = [{
                'weburl': result['webUrl'],
                'headline': result['fields']['headline'],
                'thumbnail': result['fields'].get('thumbnail', ''),
                'standfirst': self.clean_standfirst(result['fields'].get('standfirst', '')),
                'date': result['webPublicationDate']
            } for result in results]
            return output
        except Exception as e:
            logging.exception(f'Error searching news: {e}')
            return None

    def clean_standfirst(self, standfirst: str) -> str:
        soup = BeautifulSoup(standfirst, 'html.parser')
        for ul in soup.find_all('ul'):
            ul.decompose()
        return soup.get_text(strip=True)
