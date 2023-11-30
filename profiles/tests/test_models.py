# your_app/tests/test_models.py
import pytest
from profiles.models import Profile
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_profile():
    user = User.objects.create(username="testuser")
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    assert Profile.objects.count() == 1
    assert profile.user.username == "testuser"
    assert profile.favorite_city == "Test City"
