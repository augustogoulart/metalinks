from server.core.models import Link
import pytest
import random
import string


def _get_random_string(string_length):
    return str().join(random.choices(string.printable, k=string_length))


@pytest.mark.django_db()
def test_can_persist_link_object():
    """
    Must persist links object to the database
    """
    link = Link(
        url='https://github.blog/',
        category=_get_random_string(64),
        title=_get_random_string(64),
        description=_get_random_string(128)
    )
    link.full_clean()
    assert not link.save()


