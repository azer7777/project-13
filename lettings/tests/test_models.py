import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_create_address():
    address = Address.objects.create(
        number=123, street="Main St", city="City", state="ST", zip_code=12345,
        country_iso_code="ABC"
    )
    assert Address.objects.count() == 1
    assert str(address) == "123 Main St"


@pytest.mark.django_db
def test_create_letting_with_address():
    address = Address.objects.create(
        number=123, street="Main St", city="City", state="ST", zip_code=12345, country_iso_code="ABC"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    assert Letting.objects.count() == 1
    assert str(letting) == "Test Letting"
