# Django Portfolio Project Foundation

## Overview

This repository contains the foundational structure of a personal portfolio website built using the Django web framework. The project demonstrates correct Django project organization, app modularity, URL delegation, and basic view handling.

The repository is intentionally minimal, clean, and extensible, serving as a strong base for future development such as templates, databases, authentication, and deployment.

---

## Project Objectives

- Demonstrate professional Django project setup
- Showcase clean Python coding practices
- Apply correct URL routing and app delegation
- Establish a scalable portfolio foundation
- Follow GitHub-ready repository standards

---

## Technologies Used

- Python 3.x
- Django 5.x
- Git & GitHub

---

## Project Structure

portfolio_project_workspace/
├── manage.py
├── portfolio_project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── main/
├── views.py
├── urls.py
└── apps.py

---

## Application Features

- Homepage accessible at `/`
- Projects page accessible at `/projects/`
- Modular app-based URL routing
- Clean HttpResponse-based views
- Fully runnable development environment

---

## Setup Instructions (Windows)

### 1. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

2. Install Dependencies

```
pip install -r requirements.txt
```

3. Run Development Server
   ```
   python manage.py runserver
   ```
4. Access Application
   • Homepage: http://127.0.0.1:8000/
   • Projects Page: http://127.0.0.1:8000/projects/

---

## Educational Disclaimer

This project is created strictly for educational purposes and portfolio demonstration only. It is not intended for production use without further security hardening, configuration, and testing.

---

## Future Enhancements

• HTML templates and static assets
• Database-driven project listings
• Admin customization
• User authentication
• Deployment configuration
