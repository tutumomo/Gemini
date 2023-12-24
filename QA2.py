import google.generativeai as genai
from dotenv import load_dotenv
import os
import gradio as gr

# 載入環境變數
load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

from langchain_google_genai import ChatGoogleGenerativeAI

def chatbot(query, history=None):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    # 確保 history 不為 None
    if history is None:
        history = ""

    # 將新的查詢添加到對話歷史中
    updated_history = history + "\nYou: " + query

    # 調用模型進行對話
    result = llm.invoke(query)

    # 將模型的回答也添加到對話歷史中
    updated_history += "\nGemini Pro: " + result.content

    # 返回更新後的對話歷史
    return updated_history, updated_history

chatbot_interface = gr.Interface(
    fn=chatbot, 
    inputs=[gr.Textbox(lines=2, placeholder="Type your message here..."), gr.State()],
    outputs=[gr.Textbox(), gr.State()],
    title="Gemini Pro Chatbot",
    description="Interact with Gemini Pro using gradio and view the conversation history in the same text box."
)

chatbot_interface.launch()
