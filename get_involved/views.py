# get_involved/views.py
from django.core.files.storage import FileSystemStorage
from .models import VolunteerApplication
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
import os

def partner(request):
    return render(request, 'get_involved/partner.html')

def volunteer(request):
    if request.method == 'POST':
        try:
            # Handle file upload
            cv_file = None
            if 'cv' in request.FILES:
                cv_file = request.FILES['cv']

            # Save to database
            application = VolunteerApplication.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                interest=request.POST.get('interest'),
                message=request.POST.get('message'),
                cv=cv_file,
                newsletter_consent='newsletter_consent' in request.POST
            )

            # Send email notification
            send_mail(
                'New Volunteer Application',
                f"""New volunteer application received:
                Name: {application.first_name} {application.last_name}
                Email: {application.email}
                Interest: {application.interest}
                """,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],  # Your admin email
                fail_silently=False,
            )

            messages.success(request, 'Thank you for your application! We will contact you soon.')
            return redirect('get_involved:volunteer')
            
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('get_involved:volunteer')
    
    return render(request, 'get_involved/volunteer.html')

def donate(request):
    return render(request, 'get_involved/donate.html')