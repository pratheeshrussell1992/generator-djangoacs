"""
Django settings for <%= project_name %> project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .database import database_setting, database_apps
from .auth_setting import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(BASE_DIR,'<%= project_name %>', 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from django.core.management.utils import get_random_secret_key
            SECRET_KEY = get_random_secret_key()
            secret = open(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY
OAUTH_CLIENTID = OAUTH_CLIENTID_SETTING
OAUTH_CLIENT_SECRET = OAUTH_CLIENT_SETTING

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TO MAKE TRAILING SLASH IN URL OPTIONAL
APPEND_SLASH=False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # our custom apps
    'modules.user',
    'modules.sample', 
    # swagger
    'drf_yasg',
    # for rest framework
    'rest_framework', 
    # default apps
	'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS.extend(AUTH_APPS)
INSTALLED_APPS.extend(database_apps)



# Code generators
# https://github.com/Brobin/drf-generators
INSTALLED_APPS_DEV = [
]

if DEBUG:
    INSTALLED_APPS.extend(INSTALLED_APPS_DEV)


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = '<%= project_name %>.urls'

AUTH_USER_MODEL ='user.user'

SIMPLE_JWT = JWT_SETTING
REST_FRAMEWORK = REST_FRAMEWORK_PERMISSIONS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '<%= project_name %>.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

#imported from database.py file
DATABASES = database_setting


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'