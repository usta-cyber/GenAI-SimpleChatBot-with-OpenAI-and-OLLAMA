from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import ollamallm
from langchain_ollama.llms import OllamaLLM
from dotenv import load_dotenv
import os
import streamlit as st


load_dotenv()
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']="pr-ordinary-weasel-11"


prompt= ChatPromptTemplate(
    [
        ("system","How can i asssit you today,please respond to user query"),
        ("user","Question:{question}")
    ]
)


llm=OllamaLLM(model="llama2")
parser=StrOutputParser()

chain=prompt|llm|parser

st.title("Chat with OLLAMA")
input=st.text_input("Search the Topic:")
if input:
    st.write(chain.invoke({"question":input}))
