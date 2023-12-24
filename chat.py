# Gemini 最基本功能命令列聊天機器人
import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat()

while True:
    message = input("You: ")
    response = chat.send_message(message)

    print("Gemini: " + response.text)

