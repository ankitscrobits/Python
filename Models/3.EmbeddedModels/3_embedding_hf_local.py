from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",)

documents = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Paris is the capital of France",
    "New York is the most populous city in the United States"
]

vector = embeddings.embed_documents(documents)

print(str(vector))

#Run using:- Python Models/3.EmbeddedModels/3_embedding_hf_local.py
