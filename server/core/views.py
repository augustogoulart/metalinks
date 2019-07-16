from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def get_links(request):
    """
    Returns list of links

    :param request:
    :return JSON response
    """
    return Response([{
      'id': 1,
      'url': 'https://github.com/augustogoulart/involved',
      'category': 'software',
      'title': 'Github - augustogoulart/involved',
      'description': 'Learn modern web development on Instagram while '
                     'building an app for online communities'
    }])
