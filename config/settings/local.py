""" 
ローカル環境の設定ファイル
"""
# マネージドライブラリ
import environ
import os

# カスタムライブラリ
from .base import *

## デフォルト設定
BASE_DIR = DEFAULT_BASE_DIR
INSTALLED_APPS = DEFAULT_INSTALLED_APPS
MIDDLEWARE = DEFAULT_MIDDLEWARE
ROOT_URLCONF = DEFAULT_ROOT_URLCONF
TEMPLATES = DEFAULT_TEMPLATES
WSGI_APPLICATION = DEFAULT_WSGI_APPLICATION
AUTH_PASSWORD_VALIDATORS = DEFAULT_AUTH_PASSWORD_VALIDATORS
LANGUAGE_CODE = DEFAULT_LANGUAGE_CODE
TIME_ZONE = DEFAULT_TIME_ZONE
USE_I18N = DEFAULT_USE_I18N
USE_TZ = DEFAULT_USE_TZ 
STATIC_URL = DEFAULT_STATIC_URL
STATICFILES_DIRES = DEFAULT_STATICFILES_DIRES
STATIC_ROOT = DEFAULT_STATIC_ROOT
MEDIA_URL = DEFAULT_MEDIA_URL
DEFAULT_AUTO_FIELD = DEFAULT_DEFAULT_AUTO_FIELD

## 設定

# 環境変数の設定
env = environ.Env()
environ.Env.read_env(os.path.join(f"{BASE_DIR}/config/settings/env/", ".env_local"))

# Amazon S3 設定
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME") 
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN")

# 各種設定
ALLOWED_HOSTS = ["127.0.0.1"]
DATABASES = DEFAULT_DATABASES
DEBUG = True
LOGGING = {
    # 「1」で固定
    "version": 1,
    # 作成済みのロガーを無効化しないための設定
    "disable_existing_loggers": False,
    # ログフォーマット
    "formatters": {
        # ローカル用
        "local": {
            "format": "[{name}] {asctime} [{levelname}] {pathname}:{lineno:d} "
                      "{message}",
            "style": "{"
        }
    },
    # ハンドラ
    "handlers": {
        # コンソール出力用ハンドラ
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "local"
        }
    },
    # ルートロガー
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    # その他のロガー
    "loggers": {
        # logsアプリケーションのロガー
        "logs": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        },
        # Django本体が出力するロガー全般を扱うロガー
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        # 発行されるSQL文を出力するためのロガー
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
SECRET_KEY = env("SECRET_KEY")
WEBHOOK_URL = env("WEBHOOK_URL")