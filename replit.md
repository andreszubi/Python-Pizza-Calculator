# Python Pizza Calculator

## Project Overview
An interactive and fun pizza ordering calculator with a retro 1980s/90s theme. This project provides three versions:
- **Command-line interface** - Terminal-based calculator (Pizza-Calculator.py)
- **Flask Web App** - Retro-themed web interface (default)
- **Django Web App** - Full-featured retro web application (django_pizza/)

The active version in Replit is the **Flask Web App** running on port 5000.

## Features
- Three pizza sizes: Small ($15), Medium ($20), Large ($25)
- 12 topping options with size-based pricing
- Automatic combo deal detection (Meat Lovers, Veggie Delight, Supreme, Hawaiian)
- Retro CRT-style interface with neon colors and scanlines
- Detailed receipts with itemized breakdown

## Project Structure
```
.
├── app.py                    # Flask web application (ACTIVE)
├── templates/                # Flask HTML templates
│   ├── index.html           # Main ordering page
│   └── receipt.html         # Order receipt page
├── static/                   # Flask static files (CSS)
│   └── style.css            # Retro-themed styling
├── Pizza-Calculator.py       # CLI version
├── django_pizza/             # Django version
│   ├── manage.py
│   ├── pizza_project/       # Django settings
│   └── calculator/          # Django app
└── requirements.txt          # Python dependencies

## Technologies
- **Language**: Python 3.11
- **Framework**: Flask 3.0.0 (web), Django 4.2.7 (alternative)
- **Package Manager**: pip

## Setup Configuration
- **Host**: 0.0.0.0 (allows Replit proxy access)
- **Port**: 5000
- **Deployment**: Autoscale (stateless web app)
- **Dependencies**: Flask, Werkzeug, Django

## Running Alternative Versions
To run the CLI version:
```bash
python Pizza-Calculator.py
```

To run the Django version:
```bash
cd django_pizza
python manage.py runserver 0.0.0.0:8000
```

## Recent Changes
- 2025-11-21: Initial import and Replit setup
  - Installed Python 3.11 and dependencies
  - Configured Flask to bind to 0.0.0.0:5000
  - Updated Django ALLOWED_HOSTS to accept all hosts
  - Set up Flask workflow for webview on port 5000
  - Configured deployment for autoscale
  - Added .gitignore for Python projects
