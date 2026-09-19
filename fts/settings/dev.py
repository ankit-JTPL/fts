from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "[::1]",
]

# Optional: Output emails to terminal instead of actually sending via Gmail
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"