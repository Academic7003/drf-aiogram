from decouple import config
import os
from pathlib import Path
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ["*"]


CSRF_TRUSTED_ORIGINS = ['http://localhost', 'http://127.0.0.1:8000', 'http://185.196.214.19']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'comments.apps.CommentsConfig',
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DRF.urls'

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

WSGI_APPLICATION = 'DRF.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': config('POSTGRES_DB'),
         'USER': config('POSTGRES_USER'),
         'PASSWORD': config('POSTGRES_PASSWORD'),
         'HOST': 'db',
         'PORT': 5432,
     }
 }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,

#     'formatters': {
#         "main_format": {
#             "format": "-"*20+"\n{asctime} - {filename} - {message}",
#             "style": "{",
#                     }
#                   },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': "main_format",
#         },
#         "file": {
#             "class": "logging.FileHandler",
#             "formatter": "main_format",
#             "filename": f"{datetime.datetime.today().date()}.log"
#         }
#     },
#     'loggers': {
#         'django_warning': {
#             'handlers': ['console', 'file'],
#             'level': 'WARNING',
#             'propagate': False,
#         },
#     },
# }
