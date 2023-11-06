from django.urls import path
from . import views

app_name = 'lettings'  # Create a namespace for the app URLs

urlpatterns = [
    path('', views.index, name='index'),  # Maps to 'index.html'
    path('<int:letting_id>/', views.letting, name='letting'),
]
