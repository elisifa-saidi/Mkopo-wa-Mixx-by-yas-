from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/submit-step3", methods=["POST"])
def submit_step3():
    return {"message": "POST WORKS"}

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)
