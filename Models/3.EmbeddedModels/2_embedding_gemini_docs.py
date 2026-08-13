from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=32)

documents = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Paris is the capital of France",
    "New York is the most populous city in the United States"
]

result = embeddings.embed_documents(documents)

print(str(result))

#Run using:- Python Models/3.EmbeddedModels/2_embedding_gemini_docs.py