# work/urls.py
from django.urls import path
from . import views

app_name = 'work'

urlpatterns = [
    path('', views.index, name='index'),  # Add this line
    path('youth-empowerment/', views.youth, name='youth'),
    path('good-governance/', views.governance, name='governance'),
    path('fintech-inclusion/', views.fintech, name='fintech'),
    path('education/', views.education, name='education'),
]