from langchain_core.prompts import load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

st.header('Reasearch Tool')

paper_input = st.selectbox("Select Research Paper Name", ["Select...", "Attention Is ll You Need", " BERT: Pre-training of Deep Bidrectional Transformers", "GPT-3: Lnaguage Models are FEW-Shot LEarners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium(3-5 paragraphs)", "Long (deltailed explanation)"])

template = load_prompt('template.json')

if paper_input != "Select...":
    if st.button('Summerize'):
        chain = template | model
        result = chain.invoke({
            'paper_input':paper_input,
            'style_input': style_input,
            'length_input': length_input
        })
        st.write(result.content[0]['text'])

# Run Using:- streamlit run Prompts/prompt_ui.py