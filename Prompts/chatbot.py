from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input('User:: ')
    if user_input.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content[0]['text']))
    print(f'Chatbot:: {response.content[0]['text']}')
    
print(chat_history)

#Run using:- python Prompts\chatbot.py