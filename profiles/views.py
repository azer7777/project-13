from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Renders the index page displaying a list of all user profiles.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML page displaying the list of user profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Renders the detail page for a specific user profile.

    Parameters:
    - request: The HTTP request object.
    - username: The username of the user whose profile is being viewed.

    Returns:
    - A rendered HTML page displaying the details of the specified user profile.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
