# Generated by Django 5.0.1 on 2025-05-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_project_pinned_project_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FileField(
                blank=True,
                help_text="Project image or SVG file",
                null=True,
                upload_to="projects/",
            ),
        ),
    ]
