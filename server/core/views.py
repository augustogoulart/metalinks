from rest_framework import viewsets

from server.core.models import Link
from server.core.serializers import LinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .meta_parser import parse_meta_data


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.order_by('id').reverse()
    serializer_class = LinkSerializer


@api_view(['POST'])
def meta_parser(request):

    url = request.data.get('url')
    title, description = parse_meta_data(url)

    return Response({
        'url': url,
        'category': 'software',
        'title': title,
        'description': description
    })
