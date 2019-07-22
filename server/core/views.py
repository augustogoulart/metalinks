from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.core.models import Link


def get_metadata(url):
    return {
        'url': url,
        'category': 'software',
        'title': 'Github - augustogoulart/involved',
        'description': 'Learn modern web development on Instagram while '
                       'building an app for online communities'
    }


@api_view(['GET', 'POST'])
def get_links(request):
    """
    Returns list of links
    :param request:
    :return JSON response
    """
    if request.method == 'GET':
        return Response([{
            'id': 1,
            'url': 'https://github.com/augustogoulart/involved',
            'category': 'software',
            'title': 'Github - augustogoulart/involved',
            'description': 'Learn modern web development on Instagram while '
                           'building an app for online communities'
        }])

    if request.method == 'POST':
        link = Link(**get_metadata('https://github.com/augustogoulart/involved'))
        link.full_clean()
        link.save()

        return Response([{
            'id': 1,
            'url': request.data['url'],
            'category': 'software',
            'title': 'Github - augustogoulart/involved',
            'description': 'Learn modern web development on Instagram while '
                           'building an app for online communities'
        }])
