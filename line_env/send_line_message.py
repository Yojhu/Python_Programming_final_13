import os
import sys
import requests
from dotenv import load_dotenv

# 載入 .env
load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
USER_ID = os.getenv("LINE_USER_ID")

if not CHANNEL_ACCESS_TOKEN or not USER_ID:
    print("請先在 .env 中設定 LINE_CHANNEL_ACCESS_TOKEN 和 LINE_USER_ID")
    sys.exit(1)

PUSH_ENDPOINT = "https://api.line.me/v2/bot/message/push"


def send_text_message(to: str, text: str) -> None:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
    }

    body = {
        "to": to,
        "messages": [
            {
                "type": "text",
                "text": text,
            }
        ],
    }

    resp = requests.post(PUSH_ENDPOINT, headers=headers, json=body, timeout=10)

    if resp.status_code != 200:
        print("送出失敗，status:", resp.status_code)
        print("response:", resp.text)
    else:
        print("已送出訊息：", text)


def send_name(text):
    send_text_message(USER_ID, text)
