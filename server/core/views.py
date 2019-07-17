from rest_framework.decorators import api_view
from rest_framework.response import Response


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
        return Response({
            'id': 2,
            'url': request.data['url'],
            'category': 'software',
            'title': 'Github - augustogoulart/involved',
            'description': 'Learn modern web development on Instagram while '
                           'building an app for online communities'
        })
