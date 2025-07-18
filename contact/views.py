from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

def contact(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        interest = request.POST.get('interest', '').strip()
        message = request.POST.get('message', '').strip()

        # Validate required fields
        if not all([first_name, last_name, email, interest, message]):
            return JsonResponse({
                'success': False,
                'error': 'All fields are required'
            }, status=400)

        # Create email content
        subject = f"New Contact from {first_name} {last_name}"
        email_content = f"""
        Name: {first_name} {last_name}
        Email: {email}
        Interest: {interest}
        Message:
        {message}
        """

        try:
            # Send email
            send_mail(
                subject,
                email_content,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': 'Failed to send message. Please try again later.'
            }, status=500)
    
    # GET request - show empty form
    return render(request, 'contact/contact.html')