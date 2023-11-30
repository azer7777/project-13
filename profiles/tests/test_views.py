from django.urls import reverse
import pytest
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_index_view(client):
    """
    Test that the index view displays a list of users.
    """
    user = User.objects.create(username="testuser")
    Profile.objects.create(user=user, favorite_city="Test City")
    url = reverse("profiles:index")
    response = client.get(url)

    # Ensure the response status is 200 (OK)
    assert response.status_code == 200

    # Ensure the username is present in the response content
    assert "testuser" in response.content.decode()


@pytest.mark.django_db
def test_profile_view(client):
    """
    Test that the profile view displays user details including favorite_city.
    """
    user = User.objects.create(username="testuser")
    Profile.objects.create(user=user, favorite_city="Test City")
    url = reverse("profiles:profile", args=["testuser"])
    response = client.get(url)

    # Ensure the response status is 200 (OK)
    assert response.status_code == 200

    # Ensure the username is present in the response content
    assert "testuser" in response.content.decode()

    # Ensure favorite_city is present in the response content
    assert "Test City" in response.content.decode()
