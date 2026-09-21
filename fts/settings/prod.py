import os
from .base import *

DEBUG = False

# Add your actual production domains/IPs
ALLOWED_HOSTS = [
    "fts-er1o.onrender.com",
    ".onrender.com",
    "localhost",
    "127.0.0.1",
]

# HTTPS & Proxy Settings (Critical if behind Nginx/Traefik)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True

# Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Browser Protections
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# CSRF (HTTPS only in production)
CSRF_TRUSTED_ORIGINS = [
    "https://fts-er1o.onrender.com",
    "https://*.onrender.com",
]