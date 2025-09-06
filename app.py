from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv  

load_dotenv()

#environment call

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']= "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("PROJECT_NAME")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")

#Create Chatbot

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please provide response to the user queries"),
    ("user", "{question}"),
    ("assistant", "Hello! How can I assist you today?")
])

#streamlit framework
st.title("Chatbot with Langchain and OpenAI")
input_text = st.text_input("Search for any information you want")

#open AI LLM Model
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
output_parser = StrOutputParser()

#chain

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))