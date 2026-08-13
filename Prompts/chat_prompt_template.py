
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system', "You are a helpfull {domain} expert"),
    ('human', "Exppain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({"domain": "Physics", "topic": "What is gravity?"})

print(prompt)

#Run using:- python Prompts\chat_prompt_template.py
