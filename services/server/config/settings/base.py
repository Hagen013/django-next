# Django basic settings

import os
import environ

env = environ.Env()
env.read_env()

# PATHS
# ------------------------------------------------------------------------------
ROOT_DIR = environ.Path(__file__) - 4  # (services/server/config/settings/base.py - 4 = project/)
SERVICE_DIR = ROOT_DIR.path('server/')
# ------------------------------------------------------------------------------
# PATHS END


# ROUTING
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'
# ------------------------------------------------------------------------------
# ROUTING END


# SECURITY SETINGS
# ------------------------------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY')
# ------------------------------------------------------------------------------
# SECURITY SETINGS END


# APPLICATIONS CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]

THIRD_PARTY_APPS = [
]

LOCAL_APPS = [
    'core',
    'djnext'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# ------------------------------------------------------------------------------
# APPLICATIONS CONFIGURATION END


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# ------------------------------------------------------------------------------
# APPLICATIONS CONFIGURATION END


# TEMPLATES CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'djnext.backend.Backend',
        'DIRS': [
            '../client/pages/',
        ],
        'OPTIONS': {
            'context_processors': []
        },
    }
]

# ------------------------------------------------------------------------------
# TEMPLATES CONFIGURATION END


# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
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
# ------------------------------------------------------------------------------
# PASSWORD VALIDATION END


# STATIC FILES START
# ------------------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(ROOT_DIR.path('client/')),
)
# ------------------------------------------------------------------------------
# STATIC FILES END

# INTERNATIONALIZATION START
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = False
USE_L10N = True
USE_TZ = True
# ------------------------------------------------------------------------------
# INTERNATIONALIZATION END


# WSGI CONFIGURATION
# ------------------------------------------------------------------------------
WSGI_APPLICATION = 'config.wsgi.application'
# ------------------------------------------------------------------------------
# WSGI CONFIGURATION END