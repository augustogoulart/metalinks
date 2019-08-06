from rest_framework import serializers
from server.core.models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'url', 'category', 'title', 'description', 'image']
