# Exporting the `accounts` App to Another Django Project

This guide explains how to take the `accounts` app built in the previous project and reuse it inside a completely different Django project.

---

## How Django App Reuse Works

Django apps are designed to be self-contained. An app is just a Python package (a folder with an `__init__.py`) that follows Django conventions. As long as the app's code does not hardcode paths or settings from the original project, it can be dropped into any other project and wired up with minimal changes.

The main things you need to move are:

- The `accounts/` app folder itself
- The HTML templates used by the app
- A few lines of configuration in the new project's `settings.py` and `urls.py`

---

## Step 1 — Copy the App Folder

Navigate to your original project and copy the entire `accounts/` directory into the root of the new project.

```bash
cp -r /path/to/original/myproject/accounts /path/to/new/newproject/
```

After copying, the new project's structure should look like this:

```
newproject/
    manage.py
    newproject/
        settings.py
        urls.py
        ...
    accounts/          <-- copied from the original project
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

## Step 2 — Copy the Templates

The four HTML templates used by the accounts app need to be copied as well. If the new project already has a `templates/` directory, copy the files into it. If not, create the directory first.

```bash
mkdir -p /path/to/new/newproject/templates

cp /path/to/original/myproject/templates/landing.html  /path/to/new/newproject/templates/
cp /path/to/original/myproject/templates/login.html    /path/to/new/newproject/templates/
cp /path/to/original/myproject/templates/register.html /path/to/new/newproject/templates/
cp /path/to/original/myproject/templates/dashboard.html /path/to/new/newproject/templates/
```

If the new project already has its own `landing.html` or `dashboard.html`, you will need to merge the content manually rather than overwriting those files. See the note on template conflicts at the end of this guide.

---

## Step 3 — Register the App in `settings.py`

Open the new project's `settings.py` and add `'accounts'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',    # <-- add this
]
```

Also add the `LOGIN_URL` setting so that Django's `@login_required` decorator knows where to redirect unauthenticated users:

```python
LOGIN_URL = 'login'
```

Add this anywhere at the bottom of `settings.py`.

---

## Step 4 — Configure the Templates Directory

If it is not already there, update the `DIRS` key inside `TEMPLATES` in `settings.py` so Django can find the HTML files:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],    # <-- make sure this line exists
        ...
    },
]
```

If `DIRS` already contains other paths (from the existing project), just append `BASE_DIR / 'templates'` to the list rather than replacing it:

```python
'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'other_templates'],
```

---

## Step 5 — Wire Up the URLs

Open the new project's root `urls.py` (located at `newproject/urls.py`) and include the accounts URL patterns.

### Option A — Mount at the root

This makes the accounts pages available at `/`, `/login/`, `/register/`, etc., exactly as in the original project:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

### Option B — Mount under a prefix

If the new project already uses `/` for something else, you can mount the accounts app under a sub-path:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('yourexistingapp.urls')),
]
```

With this setup, the pages will be at `/accounts/login/`, `/accounts/register/`, `/accounts/dashboard/`, etc.

If you use a prefix, you also need to update the `href` links inside the HTML templates to match the new paths, or switch them to use Django's `{% url %}` tag (recommended — see the note on URL tags below).

---

## Step 6 — Run Migrations

The accounts app uses Django's built-in `User` model, which comes from `django.contrib.auth`. That app is already in `INSTALLED_APPS` by default, so you do not need to create any new migration files. However, if the new project has not been migrated yet, run:

```bash
python manage.py migrate
```

If the new project was already migrated (it already has a database), Django will check for any unapplied migrations from the accounts app. Since the accounts app itself has no custom models, there will be nothing new to apply and the command will complete immediately.

---

## Step 7 — Verify

Start the development server:

```bash
python manage.py runserver
```

Then check each route works as expected:

| URL | Expected result |
|---|---|
| `/` | Landing page with Login and Register buttons |
| `/login/` | Login form |
| `/register/` | Registration form |
| `/dashboard/` | Redirects to `/login/` if not logged in; shows greeting if logged in |
| `/logout/` | Logs out and redirects to landing |

---

## What You Do Not Need to Copy

The following files from the original project are not part of the `accounts` app and should not be copied:

- `manage.py` — specific to the original project
- `myproject/settings.py` — specific to the original project
- `myproject/urls.py` — you update the new project's own `urls.py` instead
- `db.sqlite3` — the database; each project has its own
- Any migration files other than `accounts/migrations/__init__.py` — migrations are regenerated per project

---

## Notes on Common Situations

### The new project already has its own `urls.py` entries

No problem. Just add `include('accounts.urls')` alongside the existing entries as shown in Option A or B above. Django evaluates URL patterns in order and stops at the first match, so make sure more specific paths come before the catch-all `''` root path.

### The new project uses a different database (PostgreSQL, MySQL, etc.)

The accounts app works with any database Django supports. No changes to the app code are needed. Django's ORM and the built-in `User` model are database-agnostic. Just make sure the `DATABASES` setting in the new project's `settings.py` is configured correctly for your database, then run `migrate` as normal.

### Avoiding hardcoded URLs in templates — use `{% url %}`

The templates in this app use hardcoded paths like `href="/login/"`. This works fine when mounted at the root, but breaks if you mount the app under a prefix (Option B above). The more robust approach is to use Django's built-in `{% url %}` template tag, which resolves a URL by its name rather than its path:

```html
<!-- Instead of this: -->
<a href="/login/"><button>Login</button></a>

<!-- Use this: -->
<a href="{% url 'login' %}"><button>Login</button></a>
```

This way, regardless of where the app is mounted, the links always resolve to the correct path. It is good practice to do this for all internal links in any Django project.

### Template name conflicts

If the new project already has a `landing.html` or `dashboard.html`, do not overwrite them. Instead, either:

- Rename the accounts templates (e.g., `accounts_landing.html`) and update the corresponding `render()` calls in `accounts/views.py` to match the new names, or
- Place the accounts templates inside a subdirectory to namespace them:

```
templates/
    accounts/
        landing.html
        login.html
        register.html
        dashboard.html
```

Then update the view calls accordingly:

```python
def landing(request):
    return render(request, 'accounts/landing.html')

def login_view(request):
    ...
    return render(request, 'accounts/login.html')
```

This namespacing approach is the Django-recommended convention for reusable apps and prevents any template name collisions regardless of the host project's structure.

### The new project uses a custom User model

If the new project defines its own `AUTH_USER_MODEL` in `settings.py` (i.e., a custom user model), the `accounts` app's `register_view` uses `User.objects.create_user()` which imports Django's default `User` directly. You should update the import in `views.py` to use `get_user_model()` instead, which always returns whatever user model the project is configured to use:

```python
# Replace this:
from django.contrib.auth.models import User

# With this:
from django.contrib.auth import get_user_model
User = get_user_model()
```

No other changes are needed. The rest of the view logic (`authenticate`, `login`, `@login_required`) already handles custom user models automatically.

---

## Summary Checklist

Use this as a quick reference each time you export the app:

- [ ] Copy `accounts/` folder to the new project root
- [ ] Copy the four HTML templates into the new project's `templates/` folder
- [ ] Add `'accounts'` to `INSTALLED_APPS` in `settings.py`
- [ ] Add `LOGIN_URL = 'login'` to `settings.py`
- [ ] Confirm `BASE_DIR / 'templates'` is in `TEMPLATES['DIRS']` in `settings.py`
- [ ] Add `include('accounts.urls')` to the new project's root `urls.py`
- [ ] Run `python manage.py migrate`
- [ ] Test all five routes in the browser
- [ ] (Optional) Switch hardcoded `href` paths to `{% url %}` tags in templates
- [ ] (Optional) Namespace templates under `templates/accounts/` if conflicts exist
- [ ] (Optional) Switch to `get_user_model()` if the project uses a custom user model
