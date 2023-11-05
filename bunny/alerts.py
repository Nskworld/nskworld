# Slack通知を飛ばす処理を管理するファイル
import json
import logging
import requests

# loggerを初期化する
logger = logging.getLogger('Logging')
logger.setLevel(20)
sh = logging.StreamHandler()
logger.addHandler(sh)

def SendMessageToSlack(webhook_url, message):
    """ Slackへ通知を発行する関数

    Args:
        webhook_url (str): 通知先チャンネルのWebhook URL
        message (str): 通知内容
    """
    try:
        requests.post(webhook_url, data = json.dumps({
            "text": message
        }))
        return logger.info(f'Slack通知を発行しました: {message}')
    except:
        logger.error('Slackへの通知に失敗しました。')
