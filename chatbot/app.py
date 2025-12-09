from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
#langsmith
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


#promptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "your are a helpful assistant. Please response to the user queries"),
        ("user", "Question: {question}")
    ]

)

#streamlit framework

st.title("LANGCHAIN-chatbot")
input_text = st.text_input("search the topic you want")

#gemini LLM

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))



