from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Contact
from django.core.mail import send_mail
import os

def home(request):
    # Static projects and skills data
    projects = [
        {
            'title': 'Portfolio Website',
            'description': 'A modern portfolio website built with Django, showcasing my skills and projects.',
            'technology': 'Django, HTML, CSS, JavaScript',
            'github_url': 'https://github.com/dee-mee/portfolio1',
            'url': 'https://portfolio-2ogh.onrender.com',
            'stars': 5,
            'forks': 2,
            'is_github_project': True
        },
        {
            'title': 'Linux System Monitor',
            'description': 'A command-line tool for monitoring system resources on Linux servers.',
            'technology': 'Python, Bash',
            'github_url': 'https://github.com/dee-mee/linux-monitor',
            'url': '',
            'stars': 8,
            'forks': 3,
            'is_github_project': True
        },
        {
            'title': 'Django REST API',
            'description': 'A RESTful API built with Django REST Framework for a task management application.',
            'technology': 'Django, DRF, PostgreSQL',
            'github_url': 'https://github.com/dee-mee/django-rest-api',
            'url': '',
            'stars': 12,
            'forks': 4,
            'is_github_project': True
        }
    ]
    
    skills = [
        {
            'name': 'Python',
            'description': 'Advanced proficiency in Python programming, including Django, Flask, and data analysis libraries.',
            'icon': 'fab fa-python',
            'proficiency': 90
        },
        {
            'name': 'Linux Administration',
            'description': 'Expert in Linux system administration, server management, and automation.',
            'icon': 'fab fa-linux',
            'proficiency': 95
        },
        {
            'name': 'Web Development',
            'description': 'Full stack web development with HTML, CSS, JavaScript, and modern frameworks.',
            'icon': 'fas fa-code',
            'proficiency': 85
        },
        {
            'name': 'Database Management',
            'description': 'Experience with SQL and NoSQL databases, including PostgreSQL, MySQL, and MongoDB.',
            'icon': 'fas fa-database',
            'proficiency': 80
        }
    ]
    
    try:
        # Try to get data from database first
        db_projects = list(Project.objects.all().order_by('-created_at'))
        db_skills = list(Skill.objects.all())
        
        # If we have data in the database, use it
        if db_projects:
            projects = db_projects
        if db_skills:
            skills = db_skills
    except Exception as e:
        # If database access fails, we already have static data
        pass
    
    # Render the template with our data
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
