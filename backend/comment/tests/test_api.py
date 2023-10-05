from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_comment(client, comment):
    url = reverse('comment-list')
    response = client.post(url, comment, content_type='application/json')
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_create_comment_with_tags(client, tag, comment_with_tag):
    url = reverse('comment-list')
    response = client.post(url, comment_with_tag, content_type='application/json')
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_list_comments_status_code(client):
    url = reverse('comment-list')
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_update_comment(client, comment):
    url = reverse('comment-list')
    client.post(url, comment, content_type='application/json')

    url = reverse('comment-detail', kwargs={'pk': 1})
    response = client.put(url, comment, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_delete_comment(client, comment):
    url = reverse('comment-list')
    client.post(url, comment, content_type='application/json')

    url = reverse('comment-detail', kwargs={'pk': 1})
    response = client.delete(url)
    assert response.status_code == HTTPStatus.NO_CONTENT
