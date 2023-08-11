""" 
本番環境の設定ファイル
"""
# マネージドライブラリ
import environ
import os

# カスタムライブラリ
from .base import *

# 環境変数
env = environ.Env()
environ.Env.read_env(os.path.join(f"{BASE_DIR}/config/settings/env/", ".env_production"))
SECRET_KEY = env("SECRET_KEY")

# 設定
ALLOWED_HOSTS = []

# TODO: envファイルに中身を移す
# 参考: あきよこ本 P.137
DATABASES = {
    "production" : {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "route404",
        "USER": "route404user",
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
        "TIME_ZONE": "Asia/Tokyo"
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
            "format": "{asctime} <{process:d}, {thread:d}> [{lebelname}] "
                      "{pathname}: {lineno:d} {message}",
            "style": "{"
        }
    },
    # ハンドラ
    "handlers": {
        # ファイル出力用ハンドラ
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": f"/var/log/{BASE_DIR.name}/app.log",
            "formatter": "production"
        }
    },
    # ルートロガー
    "root": {
        "handlers": ["file"],
        "level": "INFO"
    },
    # その他のロガー
    "loggers": {
        # Django本体が出力するロガー全般を扱うロガー
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False
        },
    }
}