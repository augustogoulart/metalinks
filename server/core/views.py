from rest_framework import viewsets

from server.core.models import Link
from server.core.serializers import LinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


@api_view(['POST'])
def meta_parser(request):
    title = ''
    description = ''

    html_doc = requests.get(request.data.get('url')).content
    soup = BeautifulSoup(html_doc, 'html.parser')

    for link in soup.find_all('meta'):
            try:
                if 'url' in link.get('property'):
                    url = link.get('content')

                if 'title' in link.get('property'):
                    title = link.get('content')

                if 'description' in link.get('property'):
                    description = link.get('content')
            except:
                pass

    return Response({
        'url': request.data.get('url'),
        'category': 'software',
        'title': title,
        'description': description
    })
