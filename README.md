# Django Blog

This is a blog application built with **Django 5** as a practical example, following the principles and projects outlined in "Django 5 by Example." It demonstrates key Django concepts through a functional, real-world application.

---

### ✨ Features

* **Post Management**: Users can create, edit, and delete blog posts. Posts are managed in the Django admin site.
* **User Authentication**: The project uses Django's built-in authentication system for user logins and registration.
* **Comments**: Users can leave comments on blog posts.
* **Tagging**: Posts can be tagged using `django-taggit`, allowing for organization and filtering of content.
* **SEO-Friendly URLs**: Posts have canonical URLs for better search engine optimization.
* **Full-Text Search**: The application includes a full-text search feature powered by PostgreSQL, allowing users to find content by searching for keywords.
* **Sitemap and RSS Feeds**: It generates an XML sitemap for search engines and RSS feeds for content syndication.

---

### 🚀 Getting Started

#### Prerequisites

* Python 3.12 or newer
* PostgreSQL database

#### Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure the database**:
    * Create a PostgreSQL database and update the `DATABASES` setting in `settings.py`.
    * Ensure the `django.contrib.postgres` app is listed in your `INSTALLED_APPS`.
5.  **Run migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6.  **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```
7.  **Run the development server**:
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`. You can access the Django admin site at `http://127.0.0.1:8000/admin/` to create and manage blog posts.

---

### 🛠️ Built With

* **Django**: The web framework used to build the application.
* **PostgreSQL**: The database used for full-text search and storing data.
* **Gunicorn**: A Python WSGI HTTP Server for UNIX.
* **Nginx**: A high-performance web server.

---