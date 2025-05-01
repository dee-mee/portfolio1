import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import Skill, Project
from django.core.files.images import ImageFile

def populate_skills():
    # Clear existing skills
    Skill.objects.all().delete()
    
    # Create new skills
    skills_data = [
        {
            'name': 'Linux Admin',
            'description': 'Advanced system administration, server management, and security hardening.',
            'icon': 'fab fa-linux',
            'proficiency': 95
        },
        {
            'name': 'Python',
            'description': 'Proficient in Python development including web frameworks, data analysis, and automation.',
            'icon': 'fab fa-python',
            'proficiency': 90
        },
        {
            'name': 'Django',
            'description': 'Expert in building web applications using Django framework with best practices.',
            'icon': 'fas fa-code',
            'proficiency': 85
        },
        {
            'name': 'Bash Scripting',
            'description': 'Shell scripting for automation, system management, and DevOps workflows.',
            'icon': 'fas fa-terminal',
            'proficiency': 90
        },
        {
            'name': 'HTML/CSS',
            'description': 'Creating responsive and modern user interfaces with HTML5 and CSS3.',
            'icon': 'fab fa-html5',
            'proficiency': 80
        },
        {
            'name': 'JavaScript',
            'description': 'Frontend development with vanilla JS and modern frameworks.',
            'icon': 'fab fa-js',
            'proficiency': 75
        }
    ]
    
    for skill_data in skills_data:
        Skill.objects.create(**skill_data)
    
    print(f"Added {len(skills_data)} skills")

def populate_projects():
    # Clear existing projects
    Project.objects.all().delete()
    
    # Create new projects
    projects_data = [
        {
            'title': 'Server Monitoring Dashboard',
            'description': 'A real-time monitoring system for Linux servers with alerts, performance metrics, and resource utilization tracking.',
            'technology': 'Python, Django, Chart.js',
            'url': 'https://github.com/'
        },
        {
            'title': 'Automated Deployment Pipeline',
            'description': 'CI/CD pipeline for automating the deployment of web applications with testing, staging, and production environments.',
            'technology': 'Bash, Docker, Jenkins',
            'url': 'https://github.com/'
        },
        {
            'title': 'E-commerce Platform',
            'description': 'Full-featured online store with product management, user authentication, payment processing, and order tracking.',
            'technology': 'Django, PostgreSQL, Bootstrap',
            'url': 'https://github.com/'
        },
        {
            'title': 'Portfolio Website',
            'description': 'Personal portfolio website showcasing skills, projects, and professional experience with a modern, responsive design.',
            'technology': 'Django, HTML/CSS, JavaScript',
            'url': 'https://github.com/'
        }
    ]
    
    for project_data in projects_data:
        Project.objects.create(**project_data)
    
    print(f"Added {len(projects_data)} projects")

if __name__ == '__main__':
    print("Starting database population...")
    populate_skills()
    populate_projects()
    print("Database population completed!")
