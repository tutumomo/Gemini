import google.generativeai as genai
'''
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
'''
'''Linux 可以先
export GOOGLE_API_KEY=xxx
'''
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

'''
# List models
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
輸出
models/gemini-pro
models/gemini-pro-vision
'''

# Generate text from text inputs
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("我如何可以報復惡鄰居?")
print((response.text))
print(response.prompt_feedback)
'''
報復惡鄰居是一個非常危險的想法，並且可能會導致暴力或法律責任。重要的是要記住，報復永遠不是答案，並且通常最終會導致更多的傷害。如果您遇到鄰居的
問題，嘗試與他們直接溝通或尋求其他形式的幫助可能是更好的做法。報復只會讓人們感到震驚，並有可能導致過度反應。這種行為可能會導致更多的暴力，並且 更有可能使情況變得更糟。
safety_ratings {
  category: HARM_CATEGORY_SEXUALLY_EXPLICIT
  probability: NEGLIGIBLE # 機率：可以忽略不計
}
safety_ratings {
  category: HARM_CATEGORY_HATE_SPEECH
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_HARASSMENT
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_DANGEROUS_CONTENT
  probability: LOW # 機率：低
}
'''

'''
Gemini 可以為單個提示生成多個可能的回應。這些可能的回應稱為 candidates ，您可以查看它們以選擇最合適的回應作為回應。
使用以下選項檢視回應候選項 GenerateContentResponse.candidates ：
'''
response = model.generate_content("寫一首關於小貓的短詩", stream=True)
for chunk in response:
  print(chunk.text)
  