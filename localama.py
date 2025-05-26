import streamlit as st
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
  # correct class name
#from langchain_community.llms.ollama import Ollama
#from langchain_community.llms import Ollama

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  
os.environ["LLAMA_API_KEY"] = os.getenv("LLAMA_API_KEY")        
os.environ["LANGCHAIN_TRACING_V2"] = "true"  # fixed typo

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Query: {Query}"),
])   

# Streamlit UI
st.title("News Reasearch Tool")
input_text = st.text_input("Enter your question 1:") 

# LLM configuration
llm = Ollama(model="llama3.2:1b")

#llm = Ollama(model="gemma3", temperature=0.1)
output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Button to generate response
if st.button("Submit"):
    if input_text:
        with st.spinner("Generating response..."):
            response = chain.invoke({"Query": input_text})  # .invoke is preferred
            st.success(response)
    else:
        st.warning("Please enter a query.")



























        

