from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Contact
from django.core.mail import send_mail
import os

def home(request):
    try:
        # Get existing projects
        projects = list(Project.objects.all().order_by('-created_at'))
        skills = Skill.objects.all()
        
        context = {
            'projects': projects,
            'skills': skills,
        }
        return render(request, 'core/home.html', context)
    except Exception as e:
        # Fallback to a simple response in case of errors
        from django.http import HttpResponse
        return HttpResponse(f"<h1>Portfolio Website</h1><p>We're experiencing technical difficulties. Please check back later.</p>")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send email notification
        email_subject = f'Portfolio Contact: {subject}'
        email_message = f"""You have received a new message from your portfolio website:
        
Name: {name}
Email: {email}
Subject: {subject}
Message:
{message}
"""
        
        try:
            send_mail(
                email_subject,
                email_message,
                from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings
                recipient_list=[os.environ.get('EMAIL_HOST_USER', 'your-email@example.com')],  # Uses the same email as sender
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            # Still save to database even if email fails
            messages.success(request, 'Your message has been received. Thank you!')
            print(f"Email sending failed: {e}")
            
        return redirect('home')
    
    return render(request, 'core/contact.html')
