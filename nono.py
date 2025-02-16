import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# 获取 OpenAI API Key（从环境变量）
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def chat_with_ai(user_id, user_input):
    """
    Basic AI chat function with simple memory.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_id = data.get("user_id")  # Placeholder for tracking users
    user_input = data.get("message")
    
    reply = chat_with_ai(user_id, user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 自动获取 Railway 端口
    app.run(host="0.0.0.0", port=port)
