# Generated by Django 5.0.1 on 2025-05-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_project_forks_project_github_url_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["-is_featured", "-created_at"]},
        ),
        migrations.RemoveField(
            model_name="project",
            name="is_github_project",
        ),
        migrations.AddField(
            model_name="project",
            name="is_featured",
            field=models.BooleanField(
                default=False, help_text="Feature this project on the homepage"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="forks",
            field=models.IntegerField(
                blank=True, default=0, help_text="Number of GitHub forks"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="github_url",
            field=models.URLField(blank=True, help_text="GitHub repository URL"),
        ),
        migrations.AlterField(
            model_name="project",
            name="stars",
            field=models.IntegerField(
                blank=True, default=0, help_text="Number of GitHub stars"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="url",
            field=models.URLField(
                blank=True, help_text="Live project URL if available"
            ),
        ),
    ]
