from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import openai
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']="pr-ordinary-weasel-11"


prompt=ChatPromptTemplate(
    [
        ('system',"you are helpfull assistant.please response to the user queries"),
         ('user',"question:{question}") 
     ]

)

llm=ChatOpenAI(model='gpt-3.5-turbo')
outputparser=StrOutputParser()
chain= prompt|llm|outputparser

st.title("Langchain Chat with OPENAI")

input_text=st.text_input("Search the Topic You want to know")

if input_text:
    st.write(chain.invoke({"question":input_text}))