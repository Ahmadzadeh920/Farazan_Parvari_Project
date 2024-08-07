
"""
Django settings for Farazan_Parvari_Project project.
Generated by 'django-admin startproject' using Django 1.11.20.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import jwt

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '43r#%&8gujs8t(6a$2tjv1fh^c!+crital2@!r7e&m+q2b*0g*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'Farzand_Parvari_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'Chat_app',# for online chat
    #'channels',
    'widget_tweaks',
    #'channels_presence',
    'celery',
    'django_celery_beat',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'Farazan_Parvari_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [
            os.path.join(BASE_DIR, 'Farzand_Parvari_app/templates'),
            os.path.join(BASE_DIR, 'Chat_app/templates'),
        ],
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

WSGI_APPLICATION = 'Farazan_Parvari_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Farzand', #farzand_parvari
        'USER': 'Farzand_Parvari',# farzand_parvar
        'PASSWORD': '123456789', # 123
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
    {
        'NAME': 'Farzand_Parvari_app.validators.CustomPasswortValidator',

     },

]
# Sending Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Host for sending e-mail.
EMAIL_HOST = 'smtp.farzand-parvari.ir'
# Port for sending e-mail.
EMAIL_PORT = 587
EMAIL_HOST_USER = 'security@farzand-parvari.ir'
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = 'farzand$secure5512'
EMAIL_USE_TLS =False

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'


APPEND_SLASH=False
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    # this render in json format not browsable
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',

    )
}

JWT_AUTH = {
    # Authorization:Token xxx
    'JWT_AUTH_HEADER_PREFIX': 'Token',
}

ACCOUNT_LOGOUT_ON_GET = False # add method get to logout
OLD_PASSWORD_FIELD_ENABLED = True #  to use old_password in change password
LOGOUT_ON_PASSWORD_CHANGE = False # keep the user logged in after password change

# Paasword Reset
REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'Farzand_Parvari_app.Serializer.PasswordResetSerializer',
}
CSRF_COOKIE_NAME = "csrftoken"
LOGIN_REDIRECT_URL = 'index.html'
#_______________________________Chat online
from django.urls import reverse

#redis_host = os.environ.get('REDIS_HOST', 'localhost')

#CHANNEL_LAYERS = {
    #"default": {
        #"BACKEND": "asgi_redis.RedisChannelLayer",
        #"CONFIG": {
             #"hosts": [(redis_host, 6379)],
        #},
        #"ROUTING": "Chat_app.routing.channel_routing",
   # },
#}
