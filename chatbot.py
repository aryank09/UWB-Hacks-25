# chat_api.py

from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Load your OpenAI key and system prompt
os.environ["OPENAI_API_KEY"] = open("keys.txt").read().strip()
SYSTEM_PROMPT = open("chatbot_system.txt").read().strip()

# Initialize the OpenAI client
client = OpenAI()

@app.route("/chat", methods=["POST"])
def chat():
    # Extract the user's message from the JSON payload
    user_msg = request.json.get("message", "")
    
    # Call the OpenAI Chat Completions API
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_msg},
        ],
        temperature=0.7
    )
    
    # Grab GPT's reply and return it as JSON
    answer = resp.choices[0].message.content
    return jsonify({"reply": answer})

if __name__ == "__main__":
    # Run the Flask development server on port 5000
    app.run(debug=True, port=5000)
