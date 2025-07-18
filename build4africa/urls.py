# build4africa/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
import os
from home import views as home_views
from contact import views as contact_views

urlpatterns = [
    path('', home_views.home, name='home'),  # for {% url 'home' %}
    path('index/', home_views.home, name='index'),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('our-work/', include('work.urls', namespace='work')),
    path('innovation-lab/', include('innovation.urls', namespace='innovation')),
    path('programs/', include('programs.urls')),
    path('get-involved/', include('get_involved.urls')),
    path('news/', include('news.urls')),
    path('contact/', contact_views.contact, name='contact'),
    path('home/', include('home.urls', namespace='home')),  # for {% url 'home:home' %}
    path('contact/', include('contact.urls')),
    # Serve .well-known directory from project root
    re_path(r'^\.well-known/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, '.well-known')}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)