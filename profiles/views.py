import logging
from .models import Profile
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the index page displaying a list of all user profiles.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML page displaying the list of user profiles.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        logger.info("Successfully retrieved user profiles for the index page.")
        return render(request, "profiles/index.html", context)
    except Exception as e:
        logger.error(f"An error occurred while retrieving user profiles: {e}", exc_info=True)
        # Handle the error or re-raise it if necessary
        raise


def profile(request, username):
    """
    Renders the detail page for a specific user profile.

    Parameters:
    - request: The HTTP request object.
    - username: The username of the user whose profile is being viewed.

    Returns:
    - A rendered HTML page displaying the details of the specified user profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        logger.info(f"Successfully retrieved profile for user: {username}")
        return render(request, "profiles/profile.html", context)
    except Exception as e:
        logger.error(f"An error occurred while retrieving user profile: {e}", exc_info=True)
        # Handle the error or re-raise it if necessary
        raise
