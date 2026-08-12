import os
from dotenv import load_dotenv

load_dotenv()

variable_name = "OPENAI_API_KEY"
secret = os.getenv(variable_name)

if not secret:
    raise ValueError(f"{variable_name} is missing")

print("Secret loaded sucessfully")