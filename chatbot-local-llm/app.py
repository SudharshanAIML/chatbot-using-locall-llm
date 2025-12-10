from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

#streamlit
import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()

#langsmit
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"     

#local deepseek model deepseek-r1:1.5b
LOCAL_LLM = os.getenv("LOCAL_LLM")

#prompt_template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "your are a Tech Geek . please, respond to the users question and Don't give reasoning <think>, just provide the direct answer"),
        ("user", "Question: {question}")
    ]
)

#streamlit framewort

st.title("Langchain Chatbot Local LLM API")
input_text = st.text_input("ASK ANY QUESTION")

#Ollama local LLM

llm = Ollama(model = LOCAL_LLM)
output_parser = StrOutputParser()
chain = prompt_template|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

