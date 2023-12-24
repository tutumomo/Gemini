import google.generativeai as genai
from dotenv import load_dotenv
import os
import gradio as gr

# 載入環境變數
load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

from langchain_google_genai import ChatGoogleGenerativeAI

# 創建一個保存對話歷史的變量
conversation_history = []

def chatbot(query):
    global conversation_history

    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    # 將新的查詢添加到對話歷史中
    conversation_history.append("You: " + query)

    # 調用模型進行對話
    result = llm.invoke(query)

    # 將模型的回答也添加到對話歷史中
    conversation_history.append("Gemini Pro: " + result.content)

    # 將整個對話歷史作為字串返回
    return "\n".join(conversation_history)

chatbot_interface = gr.Interface(fn=chatbot, 
                                inputs="text",
                                outputs="text",
                                title="Gemini Pro Chatbot",
                                description="Interact with Gemini Pro using gradio and view the conversation history.")

chatbot_interface.launch()
