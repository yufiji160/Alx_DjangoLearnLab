# Authentication System Documentation

## Overview
This authentication system provides user registration, login, logout, and profile management using Django's built-in authentication framework.

## Features
- Secure user registration with email verification field
- Login and logout using Django’s auth views
- Profile update (username, email, bio, and image)
- CSRF protection on all forms
- Passwords stored using Django’s PBKDF2 hashing

## Routes
| Path | Description |
|------|--------------|
| `/register/` | User registration page |
| `/login/` | User login page |
| `/logout/` | Logs out the current user |
| `/profile/` | Profile view and edit page |

## Security Notes
- All forms use CSRF tokens.
- Passwords are hashed automatically.
- Profile view is protected by `@login_required`.