from django.urls import reverse
import pytest
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view(client):
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view(client):
    address = Address.objects.create(
        number=123, street="Main St", city="City", state="ST", zip_code=12345,
        country_iso_code="ABC"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    url = reverse("lettings:letting", args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert "Test Letting" in response.content.decode()
