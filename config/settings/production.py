""" 
本番環境の設定ファイル
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
MEDIA_ROOT = DEFAULT_MEDIA_ROOT
MEDIA_ROOT = DEFAULT_MEDIA_ROOT
DEFAULT_AUTO_FIELD = DEFAULT_DEFAULT_AUTO_FIELD


## カスタム設定

# 環境変数
env = environ.Env()
environ.Env.read_env(os.path.join(f"{BASE_DIR}/config/settings/env/", ".env_production"))
SECRET_KEY = env("SECRET_KEY")

# 各種設定
ALLOWED_HOSTS = [env("ALLOWED_HOST")]

DATABASES = {
    "default" : {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "route404",
        "USER": "route404user",
        "PASSWORD": env("DB_PASSWORD"),
        "HOST":  env("DB_HOST"),
        "PORT": "5432",
        "ATOMIC_REQUESTS": True
    }
}
DEBUG = False
LOGGING = {
    # 「1」で固定
    "version": 1,
    # 作成済みのロガーを無効化しないための設定
    "disable_existing_loggers": False,
    # ログフォーマット
    "formatters": {
        # 本番用
        "production": {
            "format": "%(asctime)s [%(levelname)s] %(process)d %(thread)d  "
                      "%(pathname)s: %(lineno)d %(message)s"
        }
    },
    # ハンドラ
    "handlers": {
        # ファイル出力用ハンドラ
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/var/log/route404/app.log",
            "formatter": "production"
        }
    },
    # ロガー
    "loggers": {
        # 自作アプリケーション全般のログを拾うロガー
        "": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False
        },
        # Django本体が出力するロガー全般を扱うロガー
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False
        }
    }
}
