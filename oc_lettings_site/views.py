from django.shortcuts import render


def index(request):
    """
    Renders the index page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML page for the index.
    """
    return render(request, "index.html")


def custom_404(request, exception):
    """
    Renders the custom 404 (Page Not Found) error page.

    Parameters:
    - request: The HTTP request object.
    - exception: The exception that triggered the 404 error.

    Returns:
    - A rendered HTML page for the custom 404 error.
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Renders the custom 500 (Internal Server Error) error page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML page for the custom 500 error.
    """
    return render(request, "500.html", status=500)
