from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('lettings.urls')),  # Include new 'lettings' app URLs
    path('', include('profiles.urls')),  # Include new 'profiles' app URLs
    path('admin/', admin.site.urls),
]
