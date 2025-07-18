# models.py
from django.db import models

class VolunteerApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    interest = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    cv = models.FileField(upload_to='volunteer_cvs/')
    newsletter_consent = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.interest}"