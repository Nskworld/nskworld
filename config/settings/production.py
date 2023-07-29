""" 
本番環境の設定ファイル
"""
# マネージドライブラリ
import environ
import os

# カスタムライブラリ
from settings import base

# 変数
BASE_DIR = base.BASE_DIR
ENV = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))
# VARIABLE_NAME = env("VARIABLE_NAME")

# 設定
ALLOWED_HOSTS = []
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
# TODO: envファイルに中身を移す
# 参考: あきよこ本 P.137
DATABASES = {
    "production" : {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "ATOMIC_REQUESTS": "",
        "TIME_ZONE": ""
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
    "handolers": {
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
        "level": "INFO",
    },
    # その他のロガー
    "loggers": {
        # Django本体が出力するロガー全般を扱うロガー
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False,
        },
    }
}