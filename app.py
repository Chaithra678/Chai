from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)  # <- ee line mukhya

# Gemini API key set madi
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/")
def home():
    return "Chai AI is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("message")
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
