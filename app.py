from flask import Flask, jsonify
import os
from datetime import datetime, timezone
import socket

app = Flask(__name__)

@app.route("/")
def home():
    current_info = {
        "service": "cloud-microservice",
        "status": "running",
        "version": "1.0.0",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "environment": os.getenv("ENV", "development"),
        "host": socket.gethostname()
    }
   
    return jsonify(current_info)

@app.route("/health")
def health():
    return jsonify(
        status="alles gut"
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)