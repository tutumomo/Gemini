
import gradio as gr
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

def gemini_chat(input_text):
    response = chat.send_message(input_text)
    return [input_text, "Gemini: " + response.text]

iface = gr.Interface(fn=gemini_chat, inputs=["text"], outputs=["text", "text"], live=False, title="Gemini 聊天機器人")
iface.launch()
