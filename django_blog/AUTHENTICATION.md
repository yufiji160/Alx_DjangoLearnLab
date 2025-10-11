# AUTHENTICATION.md

## Purpose
This file explains how authentication and blog post permissions work in this project.

## Login / Logout
- Django's built-in auth views are used for login/logout.
- Ensure `LOGIN_URL` and `LOGIN_REDIRECT_URL` are set in settings.py, e.g.:
  LOGIN_URL = '/accounts/login/'
  LOGIN_REDIRECT_URL = '/'

## Posts & Permissions
- Only authenticated users may create posts (enforced via `LoginRequiredMixin`).
- Only the author may edit or delete their post (enforced via `UserPassesTestMixin`).
- The `Post` model includes `author` (ForeignKey to `auth.User`) and `created_at`.
- Views:
  - ListView: public
  - DetailView: public
  - CreateView: authenticated only
  - UpdateView/DeleteView: author only

## How author is set
The `PostCreateView.form_valid()` method sets:
`form.instance.author = self.request.user`

## Running / Testing
- Make migrations: `python manage.py makemigrations` then `migrate`
- Create a superuser: `python manage.py createsuperuser`
- Start server: `python manage.py runserver`
- Run tests: `python manage.py test blog`

## Notes
- You can add additional permission checks or admin moderation as needed.
