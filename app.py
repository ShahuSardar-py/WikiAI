import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser 
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import wikipedia
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from wiki import search_and_fetch
from LLM import get_response

st.set_page_config(
    page_icon='🤖',
    page_title="WikiAI"
)

user_input= st.text_input("Search WikiAI")
content_style = st.selectbox(
    "I need summary for:",
    ["For presentations", "General Knowledge & Understanding", "Fact-Checking"]
)
submit= st.button("Search & Summarize")


if submit:
    if user_input:
        content = search_and_fetch(user_input)
        if content:
            # Generate summary using the selected style
            title, page_content = content
            summary = get_response(page_content, content_style)
            st.subheader(f"AI Summary for {content_style} on {title}")
            st.write(summary)
    else:
        st.error("Please enter a keyword.")



