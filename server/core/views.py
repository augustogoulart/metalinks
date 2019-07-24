from rest_framework import viewsets

from server.core.models import Link
from server.core.serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
