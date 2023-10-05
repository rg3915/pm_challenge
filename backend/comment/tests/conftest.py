import pytest

from backend.comment.models import Tag


@pytest.fixture
def tag():
    data = {
        "name": "Python"
    }
    return data


@pytest.fixture
def comment():
    data = {
        "text": "The quick brown fox jumps over the lazy dog.",
    }
    return data


@pytest.fixture
def comment_with_tag(tag):
    Tag.objects.create(**tag)
    data = {
        "text": "Comment with tags.",
        "tags": [1]
    }
    return data
