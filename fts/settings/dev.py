import os
from .base import *

# =========================================================
# DEVELOPMENT ENVIRONMENT SETTINGS
# =========================================================

DEBUG = True

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY",)

ALLOWED_HOSTS = ["*"]

# Database overrides matching your .env variables
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# Optional: Output emails to the terminal instead of sending actual messages during testing
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"