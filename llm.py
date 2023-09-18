import os
from dotenv import load_dotenv
import langchain
from langchain.chat_models import ChatOpenAI
from langchain.cache import InMemoryCache
from langchain.schema import HumanMessage, SystemMessage
import streamlit as st

def llm(files):

    load_dotenv()

    langchain.llm_cache = InMemoryCache()

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

    messages = [
        SystemMessage(content="You are a Code Documenter. You take in the code and create a readme markdown documentation of the code using examples and snippets from the code."),
    ]

    for file in files:
        messages.append(HumanMessage(content=file))

    with st.spinner("Generating documentation..."):
        res = chat(messages).content

    st.success("Documentation generated successfully!")
    st.markdown(res)

    return res