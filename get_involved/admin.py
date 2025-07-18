# admin.py
from django.contrib import admin
from .models import VolunteerApplication

@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'interest', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('interest', 'newsletter_consent')