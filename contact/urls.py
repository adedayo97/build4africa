from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),  # if your function is named 'contact'
    # OR
     # if your function is named 'contact_view'
]