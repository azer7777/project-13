from django.test import Client
from django.urls import reverse
import pytest


@pytest.fixture
def client():
    return Client()


def test_index_view(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()


def test_custom_404_view(client):
    # Simulate a server error
    with pytest.raises(Exception):
        url = reverse("custom_404")
        client.get(url)


def test_custom_500_view(client):
    # Simulate a server error
    with pytest.raises(Exception):
        url = reverse("custom_500")
        client.get(url)
