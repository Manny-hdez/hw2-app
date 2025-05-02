import pytest
import requests_mock
from backend.app import app as flask_app  # Import the Flask app instance

# Fixture to create a test client for the Flask app
@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

# Test the /api/articles endpoint
def test_get_articles_success(client, requests_mock):
    # Mock the NYT API endpoint
    mock_api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    mock_response_data = {
        "status": "OK",
        "response": {
            "docs": [
                {"headline": {"main": "Test Article 1"}, "pub_date": "2024-01-01T00:00:00Z", "web_url": "http://example.com/1", "snippet": "Snippet 1"},
                {"headline": {"main": "Test Article 2"}, "pub_date": "2024-01-02T00:00:00Z", "web_url": "http://example.com/2", "snippet": "Snippet 2"}
            ]
        }
    }
    # We match any query parameters using '?qs=' with requests_mock
    requests_mock.get(f"{mock_api_url}?qs=", json=mock_response_data, status_code=200)

    # Make a request to our app's endpoint
    response = client.get('/api/articles')

    # Assertions
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "OK"
    assert len(json_data["response"]["docs"]) == 2
    assert json_data["response"]["docs"][0]["headline"]["main"] == "Test Article 1"

# (Optional) Add more tests for failure cases, other endpoints etc. 