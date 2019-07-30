from rest_framework import viewsets

from server.core.models import Link
from server.core.serializers import LinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.order_by('id').reverse()
    serializer_class = LinkSerializer


@api_view(['POST'])
def meta_parser(request):

    html_doc = requests.get(request.data.get('url'))

    if html_doc.status_code != 200:
        headers = {'User-Agent': '*', 'Disallow': ''}
        html_doc = requests.get(request.data.get('url'), headers=headers)

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    title = soup.find_all("meta", {"property": "og:title"})

    if not title:
        title = soup.find_all("meta", {"name": "twitter:title"})

    description = soup.find_all("meta", {"property": "og:description"})

    if not description:
        description = soup.find_all("meta", {"name": "twitter:description"})

    try:
        title = title[0].get('content', None)
        description = description[0].get('content', None)
    except (KeyError, TypeError, IndexError):
        title = ''
        description = ''

    if not title or not description:
        title = soup.find("title")
        description = soup("meta", {"name": "description"})

        try:
            title = title.text
            description = description[0].get('content', None)
        except (KeyError, TypeError, IndexError):
            title = ''
            description = ''

    return Response({
        'url': request.data.get('url'),
        'category': 'software',
        'title': title,
        'description': description
    })
