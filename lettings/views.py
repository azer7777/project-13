from django.shortcuts import render
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the index page displaying a list of all lettings.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML page displaying the list of lettings.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        logger.info("Successfully retrieved lettings for the index page.")
        return render(request, "lettings/index.html", context)
    except Exception as e:
        logger.error(f"An error occurred while retrieving lettings: {e}", exc_info=True)
        # Handle the error or re-raise it if necessary
        raise


def letting(request, letting_id):
    """
    Renders the detail page for a specific letting.

    Parameters:
    - request: The HTTP request object.
    - letting_id: The unique identifier of the letting.

    Returns:
    - A rendered HTML page displaying the details of the specified letting.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        logger.info(f"Successfully retrieved details for letting with ID: {letting_id}")
        return render(request, "lettings/letting.html", context)
    except Exception as e:
        logger.error(f"An error occurred while retrieving letting details: {e}", exc_info=True)
        # Handle the error or re-raise it if necessary
        raise
