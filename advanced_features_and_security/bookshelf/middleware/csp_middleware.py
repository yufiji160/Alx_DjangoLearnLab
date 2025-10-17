from django.utils.deprecation import MiddlewareMixin

class SimpleCSPMiddleware(MiddlewareMixin):
    """
    Adds a Content-Security-Policy header to reduce risk of XSS.
    This is a conservative default; adjust `CSP` to match your asset hosts.
    """
    def process_response(self, request, response):
        # Example CSP — restriction
        csp = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "font-src 'self' data:; "
            "connect-src 'self'; "
            "frame-ancestors 'none'; "
            "base-uri 'self';"
        )

        if "Content-Security-Policy" not in response:
            response["Content-Security-Policy"] = csp
        return response
