from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-3.6-flash")

print(llm.invoke("Hello, how are you?"))

#Run using:- Python Models/1.LLMs/1_llm_demo.py