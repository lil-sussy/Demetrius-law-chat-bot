"""
Django settings for demetriusapp project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

MAX_QUERY_DOCUMENTS = 5
ENLARGE_CONTEXT_WITH_QUOTES = False
DISTANCE_THRESHOLD = 0.44  # Arbitrary value
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760*100  # 10MB * 100
LAW_COLLECTIONS_DB = './database/chromadb/law_collections'
JUDGMENT_COLLECTIONS_DB = './database/chromadb/judgment_collections'
INPUT_TOKEN_PRICING = 0.01 #$ / 1K tokens
OUTPUT_TOKEN_PRICING = 0.03 #$ / 1K tokens
# INPUT_TOKEN_PRICING = 0.0015 #$ / 1K tokens gpt3
# OUTPUT_TOKEN_PRICING = 0.0020 #$ / 1K tokens gpt3

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from decouple import config
SECRET_KEY = config('SECRET_KEY')

OPENAI_TOKEN = config('OPENAI_TOKEN')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
  ),
}

AUTH_USER_MODEL = 'users.Profile'

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'your_secret_key',  # Change this to a random secret key
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
    'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
    'AUTH_COOKIE_SECURE': DEBUG,    # Whether the auth cookies should be secure (https:// only).
    'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
    'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
    'AUTH_COOKIE_SAMESITE': 'none' if DEBUG else 'Lax',  # Whether to set the flag restricting cookie leaks on cross-site requests.
                                    # This can be 'Lax', 'Strict', or None to disable the flag.
}

WS_PORT = 8001

CORS_ALLOWED_ORIGINS = [
  "http://localhost:8000",
  "http://localhost:3000",
]
CORS_ORIGIN_WHITELIST = [
  "http://localhost:8000",
  "http://localhost:3000",
]
ALLOWED_HOSTS = [
  '*',
]
CSRF_TRUSTED_ORIGINS = [
  "http://localhost:8000",
  "http://localhost:3000",
]

# Application definition

INSTALLED_APPS = [
  'demetriusapp',
  'judgement_summary_tool',
  'law_chatbot',
  'users',
  
  'corsheaders',
  'rest_framework',
  'debug_toolbar',
  'django_pdb',
  'channels',
  
  # 'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'debug_toolbar.middleware.DebugToolbarMiddleware',
  'django_pdb.middleware.PdbMiddleware',
  
  'law_chatbot.middleware.corsMiddleware',
]

ROOT_URLCONF = 'demetriusapp.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['demetrius_react/build/'],
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

ASGI_APPLICATION = 'law_chatbot.urls.application'
WSGI_APPLICATION = 'demetriusapp.wsgi.application'

# Configure channel layer (using Redis as backend)
CHANNEL_LAYERS = {
  'default': {
    'BACKEND': 'channels_redis.core.RedisChannelLayer',
    'CONFIG': {
        "hosts": [('127.0.0.1', 8002)],  # Configure your Redis server
    },
  },
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': BASE_DIR / 'db.sqlite3',
  }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

import os

import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, ' frontend/build')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build'),  # Example: '../my-react-app/build'
    os.path.join(BASE_DIR, 'frontend/build/static'),
    BASE_DIR / 'database/judgment_files/',
]

# Where to collect static files to serve them
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ensure you have a correct favicon path
FAVICON_PATH = os.path.join(BASE_DIR, 'demetrius_react/build/favicon.ico')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
if DEBUG:
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"STATICFILES_DIRS: {STATICFILES_DIRS}")
    logging.debug(f"STATIC_ROOT: {STATIC_ROOT}")