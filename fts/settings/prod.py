from .base import *


# =========================================================
# PRODUCTION
# =========================================================

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = False


ALLOWED_HOSTS = []


# =========================================================
# SECURITY
# =========================================================

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True  


# =========================================================
# CSRF
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    "https://yourdomain.com",
    "https://www.yourdomain.com",
]