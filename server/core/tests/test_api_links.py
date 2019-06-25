import pytest


@pytest.fixture
def response(client):
    """
    Get render_app response
    """
    return client.get('/api/links/')


def test_api_links_get_status_code(response):
    """
    GET /api/links/ must return status code 200
    """
    assert response.status_code == 200


def test_api_links_get_response_content(response):
    """
    GET /api/links/ must return list of links
    """
    assert b'url' in response.content
    assert b'category' in response.content
    assert b'title' in response.content
    assert b'description' in response.content

