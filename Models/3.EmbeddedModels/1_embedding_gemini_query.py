from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=32)

vector = embeddings.embed_query("Delhi is the capital of India")

print(vector)

#Run using:- Python Models/3.EmbeddedModels/1_embedding_gemini_query.py
