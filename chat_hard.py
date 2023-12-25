# Gemini 命令列聊天機器人 hrad 版，不懂跟簡單版有何不同?
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# chat = model.start_chat() # 改成 message
messages = []


while True:
    message = input("You: ")
    messages.append({
        "role": "user",
        "parts": [message],
    })
    response = model.generate_content(messages)
    messages.append({
        "role": "model",
        "parts": [response.text],
    })

    print("Gemini: " + response.text)

