from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Project
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
import random

class Command(BaseCommand):
    help = 'Generate SVG project images based on project titles'

    def handle(self, *args, **options):
        # Define color palette
        colors = [
            '#ea4335',  # Red
            '#ff9f42',  # Orange
            '#ffd756',  # Yellow
            '#4bccc0',  # Teal
            '#36a2eb',  # Blue
            '#9966ff',  # Purple
            '#c9c9c9',  # Gray
        ]

        # Create output directory if it doesn't exist
        output_dir = os.path.join(settings.MEDIA_ROOT, 'projects')
        os.makedirs(output_dir, exist_ok=True)

        # Get all projects
        projects = Project.objects.all()

        for project in projects:
            # Create SVG element
            svg = ET.Element('svg', {
                'width': '800',
                'height': '400',
                'viewBox': '0 0 800 400',
                'xmlns': 'http://www.w3.org/2000/svg',
            })

            # Get a random color from the palette
            color = random.choice(colors)
            
            # Create gradient
            defs = ET.SubElement(svg, 'defs')
            gradient = ET.SubElement(defs, 'linearGradient', {
                'id': 'grad1',
                'x1': '0%',
                'y1': '0%',
                'x2': '0%',
                'y2': '100%'
            })
            ET.SubElement(gradient, 'stop', {
                'offset': '0%',
                'style': f'stop-color:{color};stop-opacity:1'
            })
            ET.SubElement(gradient, 'stop', {
                'offset': '100%',
                'style': f'stop-color:{color};stop-opacity:0.5'
            })

            # Add background rectangle with gradient
            ET.SubElement(svg, 'rect', {
                'width': '100%',
                'height': '100%',
                'fill': 'url(#grad1)'
            })

            # Add project title
            title = project.title
            text = ET.SubElement(svg, 'text', {
                'x': '50%',
                'y': '50%',
                'text-anchor': 'middle',
                'dominant-baseline': 'middle',
                'font-family': 'Arial, sans-serif',
                'font-size': '48',
                'fill': 'white',
                'filter': 'url(#shadow)'
            })
            text.text = title

            # Add shadow filter
            filter_ = ET.SubElement(defs, 'filter', {'id': 'shadow'})
            ET.SubElement(filter_, 'feDropShadow', {
                'dx': '2',
                'dy': '2',
                'stdDeviation': '2',
                'flood-color': '#000000',
                'flood-opacity': '0.3'
            })

            # Save the SVG
            filename = f"{project.title.lower().replace(' ', '_')}.svg"
            filepath = os.path.join(output_dir, filename)
            
            # Convert to string and add XML declaration
            svg_str = ET.tostring(svg, encoding='unicode')
            xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg_str
            
            with open(filepath, 'w') as f:
                f.write(xml_str)

            # Update the project's image field
            project.image = f"projects/{filename}"
            project.save()

            self.stdout.write(self.style.SUCCESS(f'Created SVG for {project.title}'))
