from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mcczu_db',
        'USER': 'root',
        'PASSWORD': 'Jhr000430@',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    },
}

INTERNAL_IPS = ['127.0.0.1']
