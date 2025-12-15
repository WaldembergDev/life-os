from .base import *

SECRET_KEY = 'django-insecure-rbq7w3+901_%f)^d3xk)oy%y=zs!)trxwsce^w6r0czx0s(ku*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}