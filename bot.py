import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = "1531725836:gtdNnvf_l6l7r67HpKAYEvMWCk1-vtq15P4"
BASE = f"https://ble.ir/{TOKEN}"
DEST = "@3_dar_100"

def send_message(text):
    requests.post(f"{BASE}/sendMessage", json={
        "chat_id": DEST,
        "text": text
    })

@app.route("/", methods=["POST"])
def webhook():
    update = request.json
    msg = update.get("message")
    if not msg:
        return "ok"

    text = msg.get("text", "")

    formatted = f"""
📌 پیام جدید
—————————————
{text}
—————————————
📡 قالب پایه هومن
"""

    send_message(formatted)
    return "ok"

app.run()
