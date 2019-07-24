from server.core.models import Link
from server.core.serializers import LinkSerializer


new_link = {
    'id': 1,
    'url': "https://github.blog/",
    'category': 'software',
    'title': "GitHub's Blog",
    'description': "Cool article I just found"
}


def test_serializer_has_the_correct_fields(db):
    link_instance = Link.objects.create(**new_link)
    serialized_link = LinkSerializer(instance=link_instance)
    assert serialized_link.data.keys() == new_link.keys()


def test_serializer_returns_the_correct_data(db):
    link_instance = Link.objects.create(**new_link)
    serialized_link = LinkSerializer(instance=link_instance)

    assert [
        serialized_link.data[value] == new_link.get(value) for value in new_link
    ]
