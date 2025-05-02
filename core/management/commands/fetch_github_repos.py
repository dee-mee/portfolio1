from django.core.management.base import BaseCommand
from django.conf import settings
from github import Github
from core.models import Project
import os

class Command(BaseCommand):
    help = 'Fetch GitHub repositories and add them to the portfolio'

    def handle(self, *args, **options):
        # Get GitHub token from environment variables
        github_token = os.environ.get('GITHUB_TOKEN')
        if not github_token:
            self.stdout.write(self.style.ERROR('GitHub token not found. Please set GITHUB_TOKEN in your environment variables.'))
            return

        # Initialize GitHub client
        g = Github(github_token)
        
        # Get user's repositories
        try:
            user = g.get_user()
            repos = user.get_repos()
            
            self.stdout.write(self.style.SUCCESS(f'Found {repos.totalCount} repositories'))
            
            # Add repositories to portfolio
            for repo in repos:
                if not repo.private:  # Only add public repositories
                    project, created = Project.objects.update_or_create(
                        github_url=repo.html_url,
                        defaults={
                            'title': repo.name,
                            'description': repo.description or 'No description provided',
                            'technology': ', '.join(repo.language.split()) if repo.language else 'Unknown',
                            'stars': repo.stargazers_count,
                            'forks': repo.forks_count,
                            'is_featured': False  # Set to True for featured projects
                        }
                    )
                    
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Added project: {repo.name}'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'Updated project: {repo.name}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error fetching repositories: {str(e)}'))
