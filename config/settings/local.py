""" 
ローカル環境の設定ファイル
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
ALLOWED_HOSTS = ["*"]
# TODO: envファイルに中身を移してテストする
# 参考: あきよこ本 P.137
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = base.DATABASES
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
            "format": "[{name}] {asctime} [{levelname}] {pathname}:{lineo:d} "
                      "{message}",
            "style": "{"
        }
    },
    # ハンドラ
    "handolers": {
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
        # Django本体が出力するロガー全般を扱うロガー
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        # 発行されるSQL文を出力するためのロガー
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    }
}
