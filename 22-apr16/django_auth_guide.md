# Building a Django App with Authentication

A step-by-step guide to building a Django web application with a landing page, user registration, login, and a protected dashboard.

---

## Prerequisites

- Python 3.8 or higher installed
- `pip` available on your system
- Basic familiarity with the terminal

---

## 1. Install Django

Django is installed via pip, Python's package manager.

```bash
pip install django
```

To verify it installed correctly:

```bash
python -m django --version
```

---

## 2. Create the Project

Django separates code into **projects** and **apps**. A project is the entire web application. An app is a self-contained module inside the project that handles a specific concern (e.g., authentication).

```bash
django-admin startproject myproject
cd myproject
```

This generates the following structure:

```
myproject/
    manage.py               # Command-line utility for the project
    myproject/
        __init__.py
        settings.py         # All project configuration lives here
        urls.py             # The root URL dispatcher
        asgi.py             # For async deployment (not needed now)
        wsgi.py             # For traditional deployment (not needed now)
```

### What is `manage.py`?

`manage.py` is your main tool for interacting with Django from the terminal. You use it to run the server, create apps, apply database migrations, and more. You will always run it from inside the outer `myproject/` directory.

---

## 3. Create the `accounts` App

```bash
python manage.py startapp accounts
```

This creates a new directory:

```
accounts/
    __init__.py
    admin.py        # Register models to appear in Django's admin panel
    apps.py         # App configuration metadata
    models.py       # Database models (tables)
    tests.py        # Automated tests
    views.py        # Request handlers — the logic of each page
    migrations/     # Auto-generated database migration files
```

### Why a separate app?

Django encourages splitting functionality into reusable apps. Keeping authentication in its own `accounts` app makes the code organized and easier to maintain or reuse in other projects.

---

## 4. Register the App in Settings

Django needs to know your app exists. Open `myproject/settings.py` and add `'accounts'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',       # Django's built-in auth system
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',                  # <-- add this
]
```

Also add the `LOGIN_URL` setting at the bottom of the file. This tells Django where to redirect unauthenticated users when they try to access a protected page:

```python
LOGIN_URL = 'login'
```

---

## 5. Configure the Templates Directory

Django needs to know where to look for HTML files. By default it looks inside each app folder, but it is cleaner to keep all templates in a single top-level `templates/` directory.

In `myproject/settings.py`, find the `TEMPLATES` setting and update the `DIRS` key:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # <-- add this
        ...
    },
]
```

`BASE_DIR` is automatically defined at the top of `settings.py` and points to the outer `myproject/` folder. `BASE_DIR / 'templates'` uses Python's `pathlib` to build the full path to your templates directory.

Then create the directory:

```bash
mkdir templates
```

---

## 6. Write the Views

Views are Python functions that receive an HTTP request and return an HTTP response. Each page in your app has a corresponding view. Open `accounts/views.py` and replace its contents:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def landing(request):
    return render(request, 'landing.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
    return render(request, 'register.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('landing')
```

### Explanation of each view

**`landing`**
The simplest possible view. It just renders the landing page template and returns it to the browser. No logic needed.

**`login_view`**
Handles both displaying the form (GET request) and processing it (POST request).

- On GET: renders the login form.
- On POST: reads the submitted `username` and `password` from `request.POST`, then calls `authenticate()`. This is Django's built-in function that checks credentials against the database. If valid, it calls `login()` to create a session for the user and redirects to the dashboard. If invalid, it adds an error message and re-renders the form.

**`register_view`**
Similar two-step pattern.

- Validates that passwords match and the username is not already taken.
- Calls `User.objects.create_user()` which hashes the password before saving — never store plain text passwords.
- On success, redirects to the login page.

**`dashboard`**
The `@login_required` decorator is the key here. If the user is not authenticated, Django automatically redirects them to `LOGIN_URL` (which you set to `'login'`). If they are authenticated, the view renders normally. The template has access to the `user` object automatically via Django's context processors.

**`logout_view`**
Calls `logout()` to destroy the user's session, then redirects to the landing page.

---

## 7. Create the URL Configuration

URLs tell Django which view to call for a given path. Create a new file `accounts/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
```

### What does `name=` do?

Naming a URL pattern lets you reference it by name anywhere in your code or templates (e.g., `redirect('dashboard')` or `href="/dashboard/"` can be written as `{% url 'dashboard' %}`). This way, if you ever change the URL path, you only update it in one place.

### Connect to the root URL file

Open `myproject/urls.py` and include the accounts URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

`include()` delegates any URL that matches the prefix (in this case, everything from the root `''`) to the `accounts/urls.py` file.

---

## 8. Create the HTML Templates

Create each file inside the `templates/` directory you made earlier.

### `templates/landing.html`

```html
<!DOCTYPE html>
<html>
<head><title>Welcome</title></head>
<body>
  <h1>Welcome to My App</h1>
  <p>This is a simple web application. Please log in or create an account to get started.</p>
  <a href="/login/"><button>Login</button></a>
  <a href="/register/"><button>Register</button></a>
</body>
</html>
```

A static page. The two buttons are anchor tags wrapping `<button>` elements, linking to the login and register URLs.

### `templates/login.html`

```html
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
  <h1>Login</h1>
  {% for message in messages %}
    <p>{{ message }}</p>
  {% endfor %}
  <form method="post">
    {% csrf_token %}
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username" required><br><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password" required><br><br>
    <button type="submit">Login</button>
  </form>
  <p>Don't have an account? <a href="/register/">Register</a></p>
</body>
</html>
```

### `templates/register.html`

```html
<!DOCTYPE html>
<html>
<head><title>Register</title></head>
<body>
  <h1>Register</h1>
  {% for message in messages %}
    <p>{{ message }}</p>
  {% endfor %}
  <form method="post">
    {% csrf_token %}
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username" required><br><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password" required><br><br>
    <label for="password2">Confirm Password:</label><br>
    <input type="password" id="password2" name="password2" required><br><br>
    <button type="submit">Register</button>
  </form>
  <p>Already have an account? <a href="/login/">Login</a></p>
</body>
</html>
```

### `templates/dashboard.html`

```html
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
  <h1>Hello, {{ user.username }}!</h1>
  <p>Welcome to your dashboard.</p>
  <a href="/logout/"><button>Logout</button></a>
</body>
</html>
```

### Key template concepts

**`{% csrf_token %}`**
CSRF stands for Cross-Site Request Forgery. This is a security attack where a malicious website tricks a user's browser into submitting a form to your site. Django protects against this by generating a unique hidden token for every form. Without it, Django will reject POST requests with a `403 Forbidden` error. You must include `{% csrf_token %}` inside every `<form method="post">`.

**`{% for message in messages %}`**
This is Django's template tag for looping. The `messages` framework lets views add one-time notifications (errors, success messages) that are displayed once and then discarded. The `{% for %}...{% endfor %}` block renders a `<p>` for each message in the queue.

**`{{ user.username }}`**
Double curly braces render a variable. Django's template engine automatically makes the currently logged-in `user` object available in every template via context processors (configured in `settings.py` by default). `user.username` accesses the username attribute of that object.

---

## 9. Run Migrations

Django uses a database (SQLite by default) to store users, sessions, and other data. Before you can use any of this, you need to create the database tables by running migrations.

```bash
python manage.py migrate
```

You will see output listing each migration being applied. This sets up the tables for Django's built-in `auth`, `sessions`, and other core apps. You do not need to write any SQL yourself.

### What are migrations?

Migrations are Django's way of tracking and applying changes to the database schema. When you (or Django's built-in apps) define or change a model, a migration file is generated that describes what changed. Running `migrate` applies those changes to the actual database.

---

## 10. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/`. You should see the landing page.

The development server automatically reloads when you save changes to your Python files, so you rarely need to restart it manually.

---

## How the Request Cycle Works

Understanding how Django processes a request from start to finish helps when debugging or extending the app.

```
Browser sends GET /dashboard/
        |
        v
myproject/urls.py           -- matches '' prefix, delegates to accounts/urls.py
        |
        v
accounts/urls.py            -- matches 'dashboard/', calls dashboard view
        |
        v
accounts/views.py           -- @login_required checks session
    |           |
not logged in   logged in
    |               |
redirect to     render(request, 'dashboard.html')
/login/                 |
                        v
                templates/dashboard.html  -- rendered with context
                        |
                        v
                HTML sent back to browser
```

---

## Project Structure Overview

After completing all steps, your project looks like this:

```
myproject/
    manage.py
    db.sqlite3              # Auto-created SQLite database file
    templates/
        landing.html
        login.html
        register.html
        dashboard.html
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
    accounts/
        __init__.py
        apps.py
        admin.py
        models.py
        views.py
        urls.py
        migrations/
            __init__.py
```

---

## Common Issues and Fixes

**`TemplateDoesNotExist` error**
Django cannot find your HTML file. Check that `BASE_DIR / 'templates'` is in the `DIRS` list inside `TEMPLATES` in `settings.py`, and that your HTML files are saved in the `templates/` folder at the project root (not inside any app folder).

**`403 Forbidden` on form submit**
You forgot `{% csrf_token %}` inside your `<form>` tag. Add it immediately after `<form method="post">`.

**Redirected to `/accounts/login/` instead of `/login/`**
Django's default `LOGIN_URL` is `/accounts/login/`. Make sure you added `LOGIN_URL = 'login'` to `settings.py`.

**`No module named 'accounts'`**
You forgot to add `'accounts'` to `INSTALLED_APPS` in `settings.py`.

**Password not hashing / login not working after manual DB edits**
Always create users through `User.objects.create_user()`, never by inserting raw rows into the database. Django hashes passwords before saving; a plain text password in the database will never match.
