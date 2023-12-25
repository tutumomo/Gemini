import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("寫一首跟貓有關的詩", stream=True)

for chunk in response:
    print(chunk.text, end="", flush=True)

print()
