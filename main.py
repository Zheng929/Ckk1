from flask import Flask, request
import requests

app = Flask(__name__)

# 換成你自己的 LINE Channel Access Token 和接收者 ID
LINE_CHANNEL_ACCESS_TOKEN = "🔑 在這裡貼上你的 Channel Token"
TO_USER_ID = "👤 在這裡貼上你自己的 LINE 使用者 ID"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("收到訊息：", data)

    # 從 webhook 傳入資料中抓出 message 欄位
    msg = data.get("message", "⚠️ 未提供訊息")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"
    }

    body = {
        "to": TO_USER_ID,
        "messages": [{
            "type": "text",
            "text": msg
        }]
    }

    res = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=body)
    print("LINE回應：", res.text)
    return "OK", 200

@app.route("/", methods=["GET"])
def health():
    return "LINE Bot Webhook is Running!", 200