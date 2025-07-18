# get_involved/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'get_involved'  # This defines the namespace

urlpatterns = [
    path('partner/', views.partner, name='partner'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('donate/', views.donate, name='donate'),
    # Add other get_involved URLs as needed
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)