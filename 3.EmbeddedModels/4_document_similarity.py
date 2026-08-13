from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=300)

documents = [
    "Virat Kohli is an Indian cricketer know for his aggressive batting and leadership.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many bating records.",
    "MS Dhoni is a former Indian international cricketer and the former captain of the Indian cricket team.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Who is an Indian fast bowler known for his unorthodox action and yorkers?"

vector = embeddings.embed_query(query)

result = embeddings.embed_documents(documents)

scores = cosine_similarity([vector], result)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x : x[1])[-1]

print(documents[index])
print("similartiy socre is:", score)