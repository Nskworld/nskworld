"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: DEFAULT_BASE_DIR / 'subdir'.
DEFAULT_BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Application definition
DEFAULT_INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bear",
    "bunny",
    "coala",
    "snake"
]

DEFAULT_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEFAULT_ROOT_URLCONF = "config.urls"

DEFAULT_TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(DEFAULT_BASE_DIR, "templates")],
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

DEFAULT_WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DEFAULT_DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DEFAULT_BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

DEFAULT_AUTH_PASSWORD_VALIDATORS = [
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

DEFAULT_LANGUAGE_CODE = "ja"

DEFAULT_TIME_ZONE = "Asia/Tokyo"

DEFAULT_USE_I18N = True

DEFAULT_USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

DEFAULT_STATIC_URL = "static/"
DEFAULT_STATICFILES_DIRES = [DEFAULT_BASE_DIR / "static"]
DEFAULT_STATIC_ROOT = f"/var/www/{DEFAULT_BASE_DIR.name}/static"

# Media files
DEFAULT_MEDIA_URL = "/media/"
DEFAULT_MEDIA_ROOT = f"/var/www/{DEFAULT_BASE_DIR.name}/media"

# Test in local environment
DEFAULT_MEDIA_ROOT =  DEFAULT_BASE_DIR / "media_root"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# デフォルトファイルストレージを S3 に設定
FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'