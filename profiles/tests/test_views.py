
# your_app/tests/test_views.py
from django.urls import reverse
import pytest
from profiles.models import Profile
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_index_view(client):
    user = User.objects.create(username="testuser")
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "Test City" in response.content.decode()

@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create(username="testuser")
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    url = reverse('profile', args=['testuser'])
    response = client.get(url)
    assert response.status_code == 200
    assert "Test City" in response.content.decode()
