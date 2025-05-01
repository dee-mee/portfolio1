from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Contact
from django.core.mail import send_mail

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'core/home.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')
    
    return render(request, 'core/contact.html')
