# innovation/urls.py
from django.urls import path
from . import views

app_name = 'innovation'  # This defines the namespace

urlpatterns = [
    path('', views.index, name='index'),  # Add this line
    # Add other innovation URLs as needed
]