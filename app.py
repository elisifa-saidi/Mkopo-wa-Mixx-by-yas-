from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/submit-step3", methods=["POST"])
def submit_step3():
    return {"message": "POST WORKS"}

if __name__ == "__main__":
    app.run()
