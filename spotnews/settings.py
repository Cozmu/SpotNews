"""
Django settings for spotnews project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import sys
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( # configurações para rodar imagens no server
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = (
#     "django-insecure-#w%dqt6v!2#uts4b1zms_)*cx!dld2qg7p9=m83j5@am=s(9$4"
# )
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me') # configuração necessaria para deploy

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True
DEBUG = bool(int(os.environ.get('DEBUG', 0))) # configuração necessaria para deploy

ALLOWED_HOSTS = [ # configuração necessaria para deploy
    os.environ.get("RAILWAY_STATIC_URL", ""),
    ".localhost",
    "127.0.0.1",
    "[::1]",
]

CSRF_TRUSTED_ORIGINS = ["https://" + os.environ.get("RAILWAY_STATIC_URL", "")] # configuração necessaria para deploy


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "news",
    "news_rest",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "spotnews.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "spotnews.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get('MYSQLDATABASE'), # "spotnews_database"
        "USER": os.environ.get('MYSQLUSER'), # os.getenv("DB_USER", "root")
        "PASSWORD": os.environ.get('MYSQLPASSWORD'), # os.getenv("DB_PASSWORD", "password")
        'HOST': os.environ.get('MYSQLHOST'), #'db_service'
        "PORT":  os.environ.get('MYSQLPORT'), # "3306"
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATE_FORMAT = "d/m/Y"

MEDIA_URL = "/img/"
MEDIA_ROOT = BASE_DIR / "static"

if "test" in sys.argv or "pytest" in sys.argv:
    MEDIA_URL = ""
    MEDIA_ROOT = BASE_DIR / "tests"
    STORAGE = {"default": "django.core.files.storage.FileSystemStorage"}

STATICFILES_DIRS = [
    BASE_DIR / "static/img",
]

STATIC_TEST_DIR = os.path.join(BASE_DIR, "tests")

REST_FRAMEWORK = {
    "DEFAULT_DATETIME_FORMAT": "%Y-%m-%d",
}

WHITE_NOISE_AUTOREFRESH = True
