import pytest


@pytest.fixture
def response(client):
    """
    Get render_app response
    """
    return client.get('/')


def test_render_app_get(response):
    """
    GET / must return status code 200
    """
    assert response.status_code == 200


def test_render_app_template_used(response):
    """
    Home view should render index.html from Nuxt build
    """
    assert 'index.html' in [template.name for template in response.templates]
