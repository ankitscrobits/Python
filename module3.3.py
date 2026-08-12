import os
from dotenv import load_dotenv
import requests

load_dotenv()

variable_name = "GEMINI_API_KEY"
secret = os.getenv(variable_name)

if not secret:
    raise ValueError(f"{variable_name} is missing")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={secret}"

header = { 
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {"text": "What is the capital of France?"}
            ]
        }
    ],
    "generationConfig": {
        "temperature": 0.7
    }
}

response = requests.post(
    url,
    headers=header,
    json=data
)

print("Status code: ", response.status_code)
print("Response: ", response.json())