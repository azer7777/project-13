from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Renders the index page displaying a list of all lettings.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML page displaying the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Renders the detail page for a specific letting.

    Parameters:
    - request: The HTTP request object.
    - letting_id: The unique identifier of the letting.

    Returns:
    - A rendered HTML page displaying the details of the specified letting.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
