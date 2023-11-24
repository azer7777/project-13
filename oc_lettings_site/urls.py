from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
]

handler404 = views.custom_404
handler500 = views.custom_500
