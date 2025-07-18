# programs/urls.py
from django.urls import path
from . import views

app_name = 'programs'  # This defines the namespace

urlpatterns = [
    path('', views.index, name='index'),  # Main programs page
    # Add other program URLs as needed
]