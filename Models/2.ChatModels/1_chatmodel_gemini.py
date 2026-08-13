from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

response = model.invoke("Hello, how are you?")

print(response.content[0]['text'])

#Run using:- Python Models/2.ChatModels/1_chatmodel_gemini.py