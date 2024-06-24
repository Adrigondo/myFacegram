"""
Django settings for myFacegram project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO Implement rotating keys
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO Add host from back4app
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'myfacegram-bohfye0n.b4a.run',
    'https://myfacegram-bohfye0n.b4a.run',
    'node85a.containers.back4app.com',
    'https://node85a.containers.back4app.com',
]
CSRF_TRUSTED_ORIGINS = ['https://myfacegram-bohfye0n.b4a.run']
CSRF_ALLOWED_ORIGINS = ['https://myfacegram-bohfye0n.b4a.run']
CORS_ORIGINS_WHITELIST = ['https://myfacegram-bohfye0n.b4a.run']
CSRF_USE_SESSIONS=True
CSRF_COOKIE_SECURE=False
# Application definition

INSTALLED_APPS = [
    # daphne
    "daphne",
    "storages",
    
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'posts',
    'users',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'myFacegram.middleware.ProfileCompletionMiddleware',
]

ROOT_URLCONF = 'myFacegram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
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

WSGI_APPLICATION = 'myFacegram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = 'https://stariluz.github.io/myFacegram/'
STATICFILES_DIRS = [
    (BASE_DIR / 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

LOGIN_URL = '/users/login/'

SRF_COOKIE_SECURE=True

# TODO Configure Cache

# Daphne
ASGI_APPLICATION = "myFacegram.asgi.application"

# Storage
# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#             "bucket_name": os.environ['AWS_STORAGE_BUCKET_NAME'],
#             "endpoint_url": f"https://{os.environ['AWS_ACCOUNT_ID']}.r2.cloudflarestorage.com",
#             "access_key": os.environ["AWS_ACCESS_KEY_ID"],
#             "secret_key": os.environ["AWS_SECRET_ACCESS_KEY"],
#             "default_acl": "private",
#             "signature_version": "s3v4",
#         },
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#     },
# }

AWS_ACCOUNT_ID=os.environ['AWS_ACCOUNT_ID']
DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
AWS_S3_ENDPOINT_URL = f'https://{AWS_ACCOUNT_ID}.r2.cloudflarestorage.com'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = 'private'
AWS_S3_SIGNATURE_VERSION='s3v4'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/'