# Personal Portfolio Website

A modern and responsive portfolio website built with Django, showcasing my skills as a Linux Administrator and Full Stack Developer.

## Features

- Modern, responsive design with a dark theme
- About section with professional profile
- Skills showcase with interactive elements
- Projects gallery with SVG illustrations
- Contact form for direct communication
- GitHub project integration with stars and forks
- Featured projects section with pinned projects
- SVG images for project cards

## Technologies Used

- Backend: Django 5.0.1
- Frontend: HTML5, CSS3, JavaScript
- Database: SQLite (development)
- Additional tools: Font Awesome, SVG illustrations, Crispy Forms
- SVG generation for project images

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/dee-mee/portfolio1.git
   cd portfolio1
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python3 manage.py migrate
   ```

5. Run the development server:
   ```bash
   python3 manage.py runserver
   ```

6. Open your browser and visit: http://127.0.0.1:8000/

## Project Structure

```
portfolio1/
├── core/              # Main Django app
│   ├── management/    # Management commands
│   │   └── commands/ # Custom commands (generate_project_images)
│   ├── models/       # Database models
│   ├── templates/    # HTML templates
│   └── static/       # App-specific static files
├── media/            # User uploaded media
│   └── projects/     # Project SVG images
├── static/           # Global static files
├── manage.py         # Django management script
├── requirements.txt  # Project dependencies
└── .gitignore        # Git ignore file
```

## Deployment

### Deploying to Render

1. Create a Render account at https://render.com/
2. Connect your GitHub account
3. Click "New +" and select "Web Service"
4. Choose your GitHub repository
5. Select the `master` branch
6. Under "Build Command", enter: 
   ```bash
   python3 -m pip install -r requirements.txt && python3 manage.py collectstatic --noinput
   ```
7. Under "Start Command", enter: `gunicorn portfolio.wsgi:application`
8. Click "Create Web Service"

Your website will be deployed and accessible through a Render-provided URL.

Note: Ensure your repository includes all static files (CSS, JavaScript, images) in the `static` directory.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
