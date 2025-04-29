from flask import Flask, jsonify, send_from_directory
import os
import requests
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route("/api/key")
def get_key():
    return jsonify({"apiKey": os.getenv("NYT_API_KEY")})

@app.route("/api/articles")
def get_articles():
    NYT_API_KEY = os.getenv("NYT_API_KEY")
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        "q": "(Sacramento) OR (UC Davis) OR (Davis, CA)",
        "api-key": NYT_API_KEY
    }
    response = requests.get(url, params=params)
    articles = response.json()
    return jsonify(articles)

@app.route("/")
@app.route("/<path:path>")
def serve_frontend(path=""):
    if path != "" and os.path.exists(f"static/{path}"):
        return send_from_directory("static", path)
    return send_from_directory("templates", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))