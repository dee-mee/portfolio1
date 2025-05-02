from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True, help_text='Live project URL if available')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # GitHub specific fields
    github_url = models.URLField(blank=True, help_text='GitHub repository URL')
    stars = models.IntegerField(default=0, blank=True, help_text='Number of GitHub stars')
    forks = models.IntegerField(default=0, blank=True, help_text='Number of GitHub forks')
    is_featured = models.BooleanField(default=False, help_text='Feature this project on the homepage')

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-is_featured', '-created_at']

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)  # For FontAwesome icons
    proficiency = models.IntegerField(default=0)  # 0-100

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'
