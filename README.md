# DjangoBlog — Django Blogging Platform

A blogging platform built with **Django 6.1**. Visitors browse posts by category, read individual posts and leave comments, and search across posts. Logged-in staff manage everything — categories, posts, and users — through a custom admin-style dashboard, separate from Django's built-in `/admin/`.

## Features

### Public site
- **Home page** — all categories, featured *Published* posts, and the rest of the published post feed, plus About/social-link content
- **Category pages** — posts filtered by category (`category/<category_id>/`)
- **Post detail** — full post view with title, featured image, body, and comments; logged-in users can post a comment directly on the page (a `POST` to the same URL creates the `Comment`)
- **Search** — keyword search across post title, short description, and body, restricted to `Published` posts
- **Site-wide context** — every page has access to the category list and social links via context processors, so nav/footer content doesn't need to be passed in per view
- **About & social links** — an About section and a list of social platform links (not uploaded directly, but referenced by `blog.context_processors.get_social_link` and confirmed in the database schema)

### Blog data model
- **`Category`** — unique name, timestamps
- **`Blog`** — title, unique slug, category, author (`auth.User`), featured image, short description, body, `status` (Draft/Published, defaults to Draft), `is_featured` flag, timestamps
- **`Comment`** — linked to a blog post and the commenting user, free-text comment, timestamps

### Auth
- **Registration** — Django's `UserCreationForm` extended with an `email` field
- **Login / logout** using Django's built-in `auth.User`

### Dashboard (`/dashboard/`, login required)
- **Overview** — category and post counts
- **Category management** — list, add, edit, delete categories
- **Post management** — list, add, edit, delete posts; on add/edit, the slug is auto-generated from the title (`slugify(title) + '-' + id`) so it stays unique even across same-titled posts; the logged-in user is set as the post's author automatically
- **User management** — list, add, edit, delete users, including staff/superuser flags, groups, and permissions — built on Django's own `User` model via `UserCreationForm`
- Only the `dashboard` index view itself enforces `@login_required`; the category/post/user management views don't have that decorator in the code shared, so access control for those may rely on something else (e.g. template-level checks or middleware not included here) — worth double-checking before deploying

### About & social links (`aboutUs` app)
- **`About`** — a single heading + description block (site-wide "about" content), intended to be a singleton: admin's `AboutAdmin.has_add_permission` is meant to block adding a second `About` once one exists — but the method never actually returns `True`/`False` (the branches don't have a `return`), so as written it always evaluates falsy and blocks adding *any* `About` via the admin, even the first
- **`SocialLink`** — platform name + URL, for social links shown via `blog.context_processors.get_social_link`
- Standard Django admin, with `Blog` customized: list view shows title/category/author/status/featured, `is_featured` is editable inline, and slug auto-populates from title

## Tech Stack

- **Backend:** Django 6.1 (Python)
- **Database:** SQLite (`db.sqlite3`)
- **Forms/UI:** `django-crispy-forms` + `crispy-bootstrap4`
- **Image handling:** Pillow (blog featured images, uploaded to `upload/%Y/%m/%d/`)
- **Email:** Django's console email backend (development-only — not wired to SMTP)

See `requirements.txt` for the full dependency list.

## Project Structure

```
djangoblog/               # Project package
  ├── settings.py            # Django settings (SQLite, crispy forms, console email)
  ├── urls.py                 # Root URLconf: admin, home, category, blog detail/search, auth, dashboard
  ├── views.py                 # home, register, login_view, logout_view
  ├── wsgi.py / asgi.py
  └── forms.py                 # RegistrationForm (extends UserCreationForm with email)

blog/                     # Category, Blog, Comment models; category/post-detail/search views; context processors
  ├── models.py
  ├── admin.py
  ├── context_processors.py    # get_context (categories), get_social_link
  ├── views.py                 # category_post, blogs (detail + comment POST), search
  └── urls.py                   # category/<category_id>/

aboutUs/                  # About, SocialLink models
  ├── models.py
  └── admin.py                 # AboutAdmin (intends to cap About to a singleton — see note below)

dashboard/                # Staff-facing CRUD for categories, posts, and users
  ├── forms.py                 # CategoryForm, BlogForm, AddUserForm, EditUserForm
  ├── views.py                  # dashboard, categories/add/edit/delete, post/add/edit/delete, users/add/edit/delete
  └── urls.py

manage.py                 # Django management entry point
requirements.txt          # Python dependencies
db.sqlite3                 # SQLite database (includes existing data/migrations)
LICENSE                    # MIT License
```


## Getting Started

### Prerequisites

- Python 3.10+ (Django 6.1 requires a recent Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rohitrai01/<repo-name>.git
   cd <repo-name>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```



5. **Create a superuser** (for `/admin/`, and to log into `/dashboard/`)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` to view the site, and `/dashboard/` to manage content.

### Notes for production

- `SECRET_KEY` is currently hardcoded in `settings.py` and `DEBUG = True` with an empty `ALLOWED_HOSTS` — both need to change before deploying anywhere.
- The email backend is set to console output only; swap in an SMTP backend for real registration/notification emails.
- Double-check access control on the dashboard's category/post/user management views (see note above) before exposing this publicly.
- Fix `AboutAdmin.has_add_permission` (see note above) if you want the "singleton About" behavior it's clearly intended to have.

## Key URLs

| Path | Purpose |
|---|---|
| `/` | Home page (categories, featured posts, post feed, about) |
| `/admin/` | Django admin |
| `/category/<category_id>/` | Posts in a category |
| `/blog/<slug>` | Single blog post + comments |
| `/blog/search/?keyword=...` | Keyword search |
| `/register/`, `/login/`, `/logout/` | Auth |
| `/dashboard/` | Dashboard overview (login required) |
| `/dashboard/categories/`, `/add/`, `/edit/<id>/`, `/delete/<id>/` | Category CRUD |
| `/dashboard/post/`, `/add/`, `/edit/<pk>/`, `/delete/<pk>/` | Post CRUD |
| `/dashboard/users/`, `/add/`, `/edit/<pk>/`, `/delete/<pk>/` | User CRUD |


