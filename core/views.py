from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Contact
from django.core.mail import send_mail
import os

def home(request):
    # Get existing projects
    projects = list(Project.objects.all().order_by('-created_at'))
    skills = Skill.objects.all()
    
    # Try to fetch GitHub repositories
    try:
        import requests
        
        # GitHub username
        github_username = os.environ.get('GITHUB_USERNAME', 'dee-mee')
        
        # Fetch repositories from GitHub API
        api_url = f'https://api.github.com/users/{github_username}/repos'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            repos = response.json()
            
            # Process each repository
            for repo in repos:
                # Skip forks unless they have significant contributions
                if repo.get('fork', False) and (repo.get('stargazers_count', 0) < 2 and repo.get('forks_count', 0) < 2):
                    continue
                    
                # Skip repositories with no description
                if not repo.get('description'):
                    continue
                    
                # Skip repositories that are archived
                if repo.get('archived', False):
                    continue
                
                # Fetch languages for the repository
                languages = []
                languages_url = repo.get('languages_url')
                if languages_url:
                    try:
                        languages_response = requests.get(languages_url)
                        if languages_response.status_code == 200:
                            languages = list(languages_response.json().keys())
                    except Exception:
                        pass
                
                # Check if project already exists
                github_url = repo.get('html_url', '')
                existing_project = next((p for p in projects if p.github_url == github_url), None)
                
                if existing_project:
                    # Update existing project
                    existing_project.title = repo.get('name', 'Unnamed Project')
                    existing_project.description = repo.get('description', '')
                    existing_project.technology = ', '.join(languages) or 'Various'
                    existing_project.url = repo.get('homepage', '')
                    existing_project.stars = repo.get('stargazers_count', 0)
                    existing_project.forks = repo.get('forks_count', 0)
                    existing_project.is_github_project = True
                    existing_project.save()
                else:
                    # Create new project
                    new_project = Project(
                        title=repo.get('name', 'Unnamed Project'),
                        description=repo.get('description', ''),
                        technology=', '.join(languages) or 'Various',
                        github_url=github_url,
                        url=repo.get('homepage', ''),
                        stars=repo.get('stargazers_count', 0),
                        forks=repo.get('forks_count', 0),
                        is_github_project=True
                    )
                    new_project.save()
                    projects.append(new_project)
    except Exception as e:
        print(f"Error fetching GitHub repositories: {e}")
    
    # Sort projects by stars (GitHub projects first)
    projects = sorted(projects, key=lambda p: (not p.is_github_project, -p.stars))
    
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
