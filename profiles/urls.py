from django.urls import path
from . import views

app_name = 'profiles'  # Create a namespace for the app URLs

urlpatterns = [
    path('', views.index, name='index'),  # Maps to 'index.html'
    path('<str:username>/', views.profile, name='profile'),
]
