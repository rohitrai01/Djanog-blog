# Django Blog Application

[![Django Version](https://img.shields.io/badge/Django-4.2%2B-brightgreen)](https://www.djangoproject.com/)

A fully-featured, multi-app Django-based blog platform. This project includes a public-facing blog, user authentication, an admin dashboard, and an "About Us" section, designed to be a solid foundation for a personal or small-scale blogging website.

✨ Features

- **Public Blog:** View and browse published blog posts.
- **User Dashboard:** A dedicated interface for registered users to create, edit, and manage their own posts.
- **Authentication System:** Secure user registration, login, and logout functionality.
- **Admin Panel:** Django's powerful built-in admin interface for comprehensive site management (superuser required).
- **About Us Page:** A static page to share information about the blog, author, or team.
- **MIT Licensed:** Open-source and freely usable.

🛠️ Technology Stack

- **Backend Framework:** [Django](https://www.djangoproject.com/) (Python)
- **Frontend:** HTML, CSS, JavaScript (with static files management)
- **Database:** (Default SQLite, easily configurable for PostgreSQL, MySQL, etc.)

📁 Project Structure

The project is organized into several Django applications for modularity:
Djanog-blog/
├── aboutUs/ # Handles the "About Us" page view and logic
├── blog/ # Core blog application (post models, list, detail views)
├── dashboard/ # User dashboard for creating and managing posts
├── djangoblog/ # Main project settings and URL configuration
├── static/ # Global static files (CSS, JS, images)
├── templates/ # Project-wide HTML templates
├── manage.py # Django command-line utility
├── requirements.txt # Python package dependencies
└── .gitignore # Files ignored by version control
