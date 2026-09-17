from .base import *

# =========================================================
# DEVELOPMENT
# =========================================================

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-local-development-key"
)

DEBUG = True

ALLOWED_HOSTS = ["*"]