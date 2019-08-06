import pytest
import io

from rest_framework.parsers import JSONParser

payload = {
    'url': "https://github.blog/",
    'category': 'software',
    'title': "GitHub's Blog",
    'description': "Cool article I just found",
    'image': "https://github.blog/wp-content/uploads/2019/03/blog-card.png?resize=1024,538"
}


@pytest.fixture
def get_response(db, client):
    """
    Get render_app response
    """
    return client.get('/api/links/')


def test_get_links_status_code(get_response):
    """
    GET /api/links/ must return status code 200
    """
    assert get_response.status_code == 200


@pytest.mark.django_db()
def test_post_links_status_code(client):
    """
    POST /api/links/ must return status code 200
    """
    post_response = client.post('/api/links/', payload)

    assert post_response.status_code == 201


@pytest.mark.django_db()
def test_posted_links_response_content(client):
    """
    POST /api/links/ must return parsed metadata
    """
    response = client.post('/api/links/', payload, follow=True, format='json').content

    stream = io.BytesIO(response)
    post_response_content = JSONParser().parse(stream)

    for field in payload:
        assert field in post_response_content


@pytest.mark.django_db()
def test_posted_links_must_persist_across_requests(client, get_response):
    """
    POST|GET /api/links test posted links must persist across requests
    """

    client.post('/api/links/', payload, follow=True)

    get_response_content = get_response.content

    assert [
        bytes(payload.get(key), 'utf-8') in get_response_content for key in payload
    ]
