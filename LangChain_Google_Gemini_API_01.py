from dotenv import load_dotenv
load_dotenv()

from IPython.display import display
from IPython.display import Markdown
import textwrap

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import google.generativeai as genai

import os
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name = "gemini-pro")

prompt_parts = [
    "寫一個 Python 的函式，然後向初學者解釋函式的用法，請使用繁體中文",
]

response = model.generate_content(prompt_parts)

print(response.text)

import PIL.Image

img = PIL.Image.open('coffee-roll.jpg')
img

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)

to_markdown(response.text)

response = model.generate_content(
    [
        "根據這張圖片寫一篇簡短的、引人入勝的部落格文章。 它應該包括照片中物體的描述並談論我在東京的旅程", 
        img
    ], 
    stream=True
)
response.resolve()

to_markdown(response.text)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("保持健康的最佳做法是什麼？")
to_markdown(result.content)


