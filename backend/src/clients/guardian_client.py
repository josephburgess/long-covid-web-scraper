import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()


class GuardianClient:
    def __init__(self):
        self.api_key = os.getenv('GUARDIAN_API_KEY')
        self.base_url = 'https://content.guardianapis.com/'

    def search_news(self, query):
        url = f'{self.base_url}search'
        params = {
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
                'standfirst': result['fields'].get('standfirst', '')
            } for result in results]
            return output
        except Exception as e:
            logging.exception(f'Error searching news: {e}')
            return None
