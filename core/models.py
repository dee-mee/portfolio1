from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.FileField(upload_to='projects/', blank=True, null=True, help_text='Project image or SVG file')
    url = models.URLField(blank=True, help_text='Live project URL if available')
    github_url = models.URLField(blank=True, help_text='GitHub repository URL')
    stars = models.IntegerField(default=0, blank=True, help_text='Number of GitHub stars')
    forks = models.IntegerField(default=0, blank=True, help_text='Number of GitHub forks')
    is_featured = models.BooleanField(default=False, help_text='Feature this project on the homepage')
    pinned = models.BooleanField(default=False, help_text='Pin this project to the featured section')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
    def get_image_url(self):
        """
        Returns the URL for the project image.
        Ensures the URL is absolute and uses the correct media URL.
        """
        if self.image and hasattr(self.image, 'url'):
            # Get the relative path from the file field
            rel_path = str(self.image)
            # Remove any leading 'media/' or '/' if present
            rel_path = rel_path.replace('media/', '').lstrip('/')
            # Return the URL with a single /media/ prefix
            return f'/media/{rel_path}'
        return ''
        
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
