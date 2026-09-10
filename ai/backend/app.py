from flask import Flask
from flask_cors import CORS
from routes_api import api

app = Flask(__name__)
CORS(app)

app.register_blueprint(api, url_prefix="/api")


@app.route("/")
def home():
    return {
        "status": "success",
        "message": "AccessRoute AI Backend is running"
    }


@app.route("/api/health")
def health():
    return {
        "status": "healthy",
        "service": "AccessRoute AI"
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)