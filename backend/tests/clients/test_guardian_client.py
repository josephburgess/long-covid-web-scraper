import pytest
import logging
from unittest.mock import Mock, patch
from src.clients import GuardianClient
from mocks import mock_guardian_response, mock_guardian_client_output


@pytest.fixture
def guardian_client():
    return GuardianClient()


def test_search_news(guardian_client):
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_guardian_response
        mock_get.return_value = mock_response

        output = guardian_client.search_news("example")

        mock_get.assert_called_once_with(
            "https://content.guardianapis.com/search",
            params={
                "q": "example",
                "page-size": 40,
                "query-fields": "headline",
                "show-fields": "thumbnail,headline,byline,standfirst,bodyText",
                "order-by": "newest",
                "api-key": guardian_client.api_key,
            },
        )
        assert output == mock_guardian_client_output


def test_search_news_error_handling(guardian_client):
    with patch("requests.get", side_effect=Exception("error")):
        with patch.object(logging, "error") as log:
            guardian_client.search_news("example")
            log.assert_called_once_with("Error searching news: error", exc_info=True)
