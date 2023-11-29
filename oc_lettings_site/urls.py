from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
]

handler404 = views.custom_404
handler500 = views.custom_500

"""
urlpatterns: A list of URL patterns for the Django project.

- "" (empty path): Maps to the views.index function, serving as the homepage.
- "admin/": Includes Django's admin site URLs.
- "lettings/": Includes URLs from the "lettings" app with the "lettings" namespace.
- "profiles/": Includes URLs from the "profiles" app with the "profiles" namespace.

handler404: Handles 404 (Page Not Found) errors, using views.custom_404 as the custom view.

handler500: Handles 500 (Internal Server Error) errors, using views.custom_500 as the custom view.
"""

