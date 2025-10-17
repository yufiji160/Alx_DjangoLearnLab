# SECURITY.md — Security measures implemented

## Summary
This project includes several security hardenings:
- DEBUG = False for production
- SECURE_BROWSER_XSS_FILTER, SECURE_CONTENT_TYPE_NOSNIFF, X_FRAME_OPTIONS set
- SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE set (HTTPS required)
- Basic Content Security Policy via SimpleCSPMiddleware
- Forms use Django forms/ModelForm to validate inputs
- Views use Django ORM with parameterized queries (avoid raw SQL string interpolation)
- Templates include {% csrf_token %} and rely on Django auto-escaping

## Testing approach
- Manual form submissions (POST) to confirm CSRF tokens are required.
- Try submitting form without CSRF token (should get 403).
- Test search input: inject SQL-like input — ORM filters should treat it as a string and not run SQL.
- Use curl to check headers:
  curl -I https://your-site.example.com/
  Look for Content-Security-Policy header, X-Frame-Options, X-Content-Type-Options.

## Notes
- Many cookie/security flags require HTTPS. For local testing, you may disable `SECURE_SSL_REDIRECT` and cookie secure flags, but enable them in production.
