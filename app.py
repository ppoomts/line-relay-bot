from flask import Flask, request
import requests
import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "ใส่_CHANNEL_ACCESS_TOKEN"
CHANNEL_SECRET = "ใส่_CHANNEL_SECRET"

AIO_USERNAME = "ใส่_USERNAME"
AIO_KEY = "ใส่_AIO_KEY"
FEED_NAME = "fear"

def send_to_adafruit(value):
    url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME}/data"
    headers = {
        "X-AIO-Key": AIO_KEY,
        "Content-Type": "application/json"
    }
    data = {"value": value}
    requests.post(url, json=data, headers=headers)

def reply_message(reply_token, text):
    url = "https://api.line.me/v2/bot/message/reply"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    data = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text}]
    }
    requests.post(url, json=data, headers=headers)

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.json
    events = body.get("events", [])
    
    for event in events:
        if event["type"] == "message":
            user_message = event["message"]["text"].upper()
            reply_token = event["replyToken"]

            if user_message == "ON":
                send_to_adafruit("ON")
                reply_message(reply_token, "รีเลย์เปิดแล้ว ✅")

            elif user_message == "OFF":
                send_to_adafruit("OFF")
                reply_message(reply_token, "รีเลย์ปิดแล้ว ❌")

            else:
                reply_message(reply_token, "พิมพ์ ON หรือ OFF")

    return "OK"

if __name__ == "__main__":
    app.run()
