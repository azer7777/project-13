from django.urls import reverse, resolve
from profiles.views import index, profile


def test_index_url():
    """
    Test that the 'index' URL resolves to the correct view function.

    This test uses the 'reverse' function to generate the URL and then checks
    that the resolved view function is 'index'.

    Usage:
    - Ensure that the 'index' URL is correctly configured in the 'urls.py' file.

    """
    url = reverse("profiles:index")
    assert resolve(url).func == index


def test_profile_url():
    """
    Test that the 'profile' URL resolves to the correct view function.

    This test uses the 'reverse' function to generate the URL and then checks
    that the resolved view function is 'profile'. It also provides a sample username.

    Usage:
    - Ensure that the 'profile' URL is correctly configured in the 'urls.py' file.
    - Provide a valid username as an argument to the 'reverse' function.

    """
    url = reverse("profiles:profile", args=["testuser"])
    assert resolve(url).func == profile
