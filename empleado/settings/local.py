import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'udemy_empleado',
        'USER': 'postgres',
        'PASSWORD': 'devincap@3*',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS= [BASE_DIR / 'static']

MEDIA_ROOT = os.path.join(BASE_DIR,'media/')
MEDIA_URL = '/media/'