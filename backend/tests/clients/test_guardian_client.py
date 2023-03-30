import unittest
import requests
from unittest.mock import Mock, patch
from src.clients import GuardianClient


class TestGuardianClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = GuardianClient()
        cls.example_response_data = {
            'response': {
                'results': [
                    {
                        'webUrl': 'https://www.example.com/article1',
                        'fields': {
                            'headline': 'Example Article 1',
                            'thumbnail': 'https://www.example.com/thumbnail1',
                            'standfirst': 'This is an example article'
                        }
                    },
                    {
                        'webUrl': 'https://www.example.com/article2',
                        'fields': {
                            'headline': 'Example Article 2',
                            'thumbnail': '',
                            'standfirst': ''
                        }
                    }
                ]
            }
        }
        cls.example_output = [
            {
                'weburl': 'https://www.example.com/article1',
                'headline': 'Example Article 1',
                'thumbnail': 'https://www.example.com/thumbnail1',
                'standfirst': 'This is an example article'
            },
            {
                'weburl': 'https://www.example.com/article2',
                'headline': 'Example Article 2',
                'thumbnail': '',
                'standfirst': ''
            }
        ]

    @patch('requests.get')
    def test_search_news(self, mock_get):
        # Set up mock response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.example_response_data
        mock_get.return_value = mock_response

        # Call search_news method with a query
        output = self.client.search_news('example')

        # Check that the mock response was used and the output is correct
        mock_get.assert_called_once_with(
            'https://content.guardianapis.com/search',
            params={
                'q': 'example',
                'page-size': 40,
                'query-fields': 'headline',
                'show-fields': 'thumbnail,headline,byline,standfirst,bodyText',
                'order-by': 'newest',
                'api-key': self.client.api_key
            }
        )
        self.assertEqual(output, self.example_output)
