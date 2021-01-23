from .base import *


# For the deployment checklist automatically, you should use a command 'python manage.py check --deploy'

DEBUG = False

ALLOWED_HOSTS = [".myUrl.com"]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if os.environ.get("DJANGO_SETTINGS_MODULE") == "config.settings.production":
    DATABASES = {
        "default": {
            "ENGINE": os.environ["RDS_DB_ENGINE"],
            "NAME": os.environ["RDS_DB_NAME"],
            "USER": os.environ["RDS_USERNAME"],
            "PASSWORD": os.environ["RDS_PASSWORD"],
            "HOST": os.environ["RDS_HOSTNAME"],
            "PORT": os.environ["RDS_PORT"],
            "ATOMIC_REQUESTS": True,
        }
    }
    # redirect URL
    REDIRECT_URL = "https://myUrl.com"

# HTTPS for the security
# make ensure the browser to use HTTPS instead of HTTP for the cookie
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# for preventing XSS (Cross-site Scripting)
SECURE_BROWSER_XSS_FILTER = True  # X-XSS-Protection:1, mode=block
SECURE_CONTENT_TYPE_NOSNIFF = True  # CSP(Content Security Policy)
X_FRAME_OPTIONS = "DENY"  # If there is a good reason for your site to serve other parts of itself in a frame, you should change it to 'SAMEORIGIN' (DEFAULT) (or maybe 'ALLOW FROM example.com')

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 3  # to first use a small value for testing (one hour). Once you confirm that all assets are served securely on your site, increase this value so that infrequent visitors will be protected (1 year)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # for subdomains
SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = (
    False  # the SecurityMiddleware redirects all non-HTTPS request to HTTPS
)


# CSRF_TOKEN
CSRF_COOKIE_DOMAIN = "myurl"
CSRF_TRUSTED_ORIGINS = [".myurl"]


# for reverse proxy in front of django
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
