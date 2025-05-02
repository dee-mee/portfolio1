import os
import requests
from django.core.management.base import BaseCommand
from core.models import Project
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Fetch GitHub repositories and save them as projects'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='GitHub username')

    def handle(self, *args, **options):
        # Get GitHub username from command line or environment variable
        github_username = options.get('username') or os.environ.get('GITHUB_USERNAME', 'dee-mee')
        
        self.stdout.write(f'Fetching repositories for GitHub user: {github_username}')
        
        # Fetch repositories from GitHub API
        api_url = f'https://api.github.com/users/{github_username}/repos'
        response = requests.get(api_url)
        
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Failed to fetch repositories: {response.status_code}'))
            return
        
        # Parse repositories
        repos = response.json()
        
        # Mark all existing GitHub projects as not from GitHub
        # This allows us to re-sync and remove projects that no longer exist
        Project.objects.filter(is_github_project=True).update(is_github_project=False)
        
        # Process each repository
        for repo in repos:
            # Skip forks unless they have significant contributions
            if repo['fork'] and (repo['stargazers_count'] < 2 and repo['forks_count'] < 2):
                continue
                
            # Skip repositories with no description
            if not repo['description']:
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
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Failed to fetch languages for {repo["name"]}: {e}'))
            
            # Get or create project
            project, created = Project.objects.update_or_create(
                github_url=repo['html_url'],
                defaults={
                    'title': repo['name'],
                    'description': repo['description'] or '',
                    'technology': ', '.join(languages) or 'Various',
                    'url': repo.get('homepage', ''),
                    'stars': repo['stargazers_count'],
                    'forks': repo['forks_count'],
                    'is_github_project': True
                }
            )
            
            status = 'Created' if created else 'Updated'
            self.stdout.write(self.style.SUCCESS(f'{status} project: {project.title}'))
        
        # Remove projects that no longer exist on GitHub
        removed_count = Project.objects.filter(is_github_project=False, github_url__isnull=False).delete()[0]
        if removed_count:
            self.stdout.write(self.style.WARNING(f'Removed {removed_count} projects that no longer exist on GitHub'))
            
        self.stdout.write(self.style.SUCCESS('Successfully synced GitHub repositories'))
