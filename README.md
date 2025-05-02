# Personal Portfolio Website

A modern and responsive portfolio website built with Django, showcasing my skills as a Linux Administrator and Full Stack Developer.

## Features

- Modern, responsive design with a dark theme
- About section with professional profile
- Skills showcase with interactive elements
- Projects gallery
- Contact form for direct communication
- SVG illustrations for visual appeal

## Technologies Used

- Backend: Django
- Frontend: HTML5, CSS3, JavaScript
- Database: SQLite (development)
- Additional tools: Font Awesome, SVG illustrations

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
├── portfolio/         # Portfolio app
├── static/           # Static files (CSS, JavaScript, images)
├── media/            # User uploaded media
├── templates/        # HTML templates
├── manage.py         # Django management script
├── requirements.txt  # Project dependencies
└── .gitignore        # Git ignore file
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
