import unittest
import requests.exceptions
import pytest
import logging
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
                        },
                        'webPublicationDate': "2023-04-03T13:37:48Z"
                    },
                    {
                        'webUrl': 'https://www.example.com/article2',
                        'fields': {
                            'headline': 'Example Article 2',
                            'thumbnail': '',
                            'standfirst': ''
                        },
                        'webPublicationDate': "2023-04-03T15:37:48Z"
                    }
                ]
            }
        }
        cls.example_output = [
            {
                'webUrl': 'https://www.example.com/article1',
                'headline': 'Example Article 1',
                'thumbnail': 'https://www.example.com/thumbnail1',
                'standfirst': 'This is an example article',
                'date': "2023-04-03T13:37:48Z"
            },
            {
                'webUrl': 'https://www.example.com/article2',
                'headline': 'Example Article 2',
                'thumbnail': '',
                'standfirst': '',
                'date': "2023-04-03T15:37:48Z"
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
                'section': 'society',
                'q': 'example',
                'page-size': 40,
                'query-fields': 'headline',
                'show-fields': 'thumbnail,headline,byline,standfirst,bodyText',
                'order-by': 'newest',
                'api-key': self.client.api_key
            }
        )
        self.assertEqual(output, self.example_output)

    def test_search_news_error_handling(self):
        with patch('requests.get', side_effect=Exception('error')):
            with self.assertLogs(level='ERROR') as log:
                self.client.search_news('example')
                self.assertIn('Error searching news', log.output[0])
