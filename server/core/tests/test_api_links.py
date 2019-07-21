import pytest


@pytest.fixture
def get_response(client):
    """
    Get render_app response
    """
    return client.get('/api/links/')


def post_payload():
    payload = {
        'url': 'https://github.com/augustogoulart/involved',
    }
    return payload


def test_get_links_status_code(get_response):
    """
    GET /api/links/ must return status code 200
    """
    assert get_response.status_code == 200


def test_get_links_response_content(get_response):
    """
    GET /api/links/ must return list of links
    """
    response = get_response.content
    assert b'url' in response
    assert b'category' in response
    assert b'title' in response
    assert b'description' in response
    assert b'id' in response


def test_post_links_status_code(client):
    """
    POST /api/links/ must return status code 301
    """
    post_response = client.post('/api/links', post_payload())

    assert post_response.status_code == 301


def test_posted_links_response_content(client):
    """
    POST /api/links/ must return parsed metadata
    """
    post_response = client.post('/api/links', post_payload(), follow=True)

    for field, value in post_payload().items():
        assert bytes(value, 'utf-8') in post_response.content
