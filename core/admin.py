from django.contrib import admin
from .models import Project, Skill, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'is_featured', 'github_url', 'stars', 'forks', 'created_at')
    search_fields = ('title', 'description', 'technology', 'github_url')
    list_filter = ('technology', 'is_featured', 'created_at')
    list_editable = ('is_featured',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'technology', 'image')
        }),
        ('URLs', {
            'fields': ('url', 'github_url')
        }),
        ('GitHub Stats', {
            'fields': ('stars', 'forks')
        }),
        ('Display Options', {
            'fields': ('is_featured',)
        })
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name', 'description')
    list_filter = ('proficiency',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
