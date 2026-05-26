import requests
import schedule
import time
from datetime import datetime

# ─── CONFIG ───────────────────────────────────────────────────────────────────
PAGE_ACCESS_TOKEN = "EAAWFfbzaNu8BRiaeKxxuuhLXe3A0FV0CM7SHdQtJKnaFd9GWiqOF4tiXb4biBsKas6ZAvvR8koS6peXnOd4G9agaefv466obFrDo0XkzMu38vXMZAEY3G3nHPGLyJZCgHkAGbZASYVssgrO75V9krwKkkfS6uACjtbLT4fg7PIj536EOWBS0UG4o0ygSBrsdwLaZBNxKQ"
RECIPIENT_PSID    = "26867085002941301"
MESSAGE_TEXT      = "Đừng lọ nhé Hào béo <3."  # Edit your message here
SEND_TIME         = SEND_TIME = "00:00"  # midnight UTC = 7am Hanoi time
# ──────────────────────────────────────────────────────────────────────────────


def send_messenger_message():
    url = "https://graph.facebook.com/v19.0/me/messages"

    payload = {
        "recipient": {"id": RECIPIENT_PSID},
        "message":   {"text": MESSAGE_TEXT},
        "messaging_type": "MESSAGE_TAG",
        "tag": "ACCOUNT_UPDATE"
    }

    params = {"access_token": PAGE_ACCESS_TOKEN}

    response = requests.post(url, json=payload, params=params)

    if response.status_code == 200:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Message sent successfully.")
    else:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Failed: {response.status_code} - {response.text}")


def main():
    print(f"Bot started. Sending daily at {SEND_TIME}.")
    send_messenger_message()  # Send once immediately on start to test
    schedule.every().day.at(SEND_TIME).do(send_messenger_message)

    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
