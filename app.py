from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        response = client.models.generate_content(
            model="gemini-2.5-flash",

            contents=prompt
        )

        return jsonify({"result": response.text})

    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
