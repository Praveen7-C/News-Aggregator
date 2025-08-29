# NewsAggregator - Django Web Application

## Overview

**NewsAggregator** is a Django-based web application that provides users with an interactive platform to view aggregated news, explore weather predictions, and access informative content. The system uses Django’s robust backend framework with templates, static assets, and a SQLite database for storage.

It offers a clean, responsive interface where users can navigate between pages like Home, About, Weather Prediction, and more.

---

## Features

* **Dynamic Pages**: Home, About, Weather Prediction, etc.
* **News Module**: Structured Django app (`news/`) to manage models, views, and templates.
* **Weather Prediction**: Dedicated template for weather-related insights.
* **Admin Panel**: Manage users, news data, and content through Django’s built-in admin.
* **Responsive UI**: Styled with custom CSS and assets.
* **Database Integration**: SQLite database for fast and easy storage.

---

## Technologies Used

* **Backend**: Django, Python
* **Frontend**: HTML5, CSS3 (custom styles in `assets/css/mystyle.css`)
* **Database**: SQLite (`db.sqlite3`)
* **Other Tools**: Django ORM, Django Templates

---

## Installation

1. **Clone the Repository**

```bash
git clone <your_repo_link>
cd NewsAggregator
```

2. **Create Virtual Environment & Install Requirements**
   Make sure you have **Python 3.8+** and **pip** installed.

```bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

pip install -r requirements.txt
```

3. **Run Database Migrations**

```bash
python manage.py migrate
python manage.py makemigrations
```

4. **Create Superuser (for Django Admin)**

```bash
python manage.py createsuperuser
```

5. **Run Development Server**

```bash
python manage.py runserver
```

The app will be available at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## Directory Structure

```
NewsAggregator/
├── assets/                    # Static assets
│   ├── css/                   # Custom styles (mystyle.css)
│   └── images/                # Images (welcome.jpg)
│
├── news/                      # Django app (models, views, urls, etc.)
│   ├── migrations/            # Database migrations
│   ├── admin.py               # Admin registration
│   ├── apps.py                # App configuration
│   ├── models.py              # Django models
│   ├── views.py               # Application views
│   ├── urls.py                # App-level URL routes
│
├── templates/                 # HTML templates
│   ├── home.html
│   ├── about.html
│   ├── homestatic.html
│   └── Weather_Prediction.html
│
├── NewsAggregator/            # Django project folder
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project-level URL routes
│   ├── wsgi.py / asgi.py      # Deployment entry points
│
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
```

---

## Usage

* **Home Page**: Landing page with main navigation.
* **About Page**: Information about the app/project.
* **Weather Prediction**: View predictions via dedicated template.
* **Admin Panel**: Login at `/admin` with superuser credentials to manage content.

---

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with new features, bug fixes, or improvements.

---

## Acknowledgments

* **Django** – for backend framework.
* **SQLite** – lightweight database used.
* **Bootstrap/CSS** – for styling and responsiveness.
* **Python Community** – for resources and documentation.

---

## License

This project is licensed under the **MIT License** – see the LICENSE file for details.

