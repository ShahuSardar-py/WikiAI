#imports 
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser 
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
import os

#key loading 
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

#setting the llm. using gemini-1.5-flash
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0.9)



# ref
#chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
#topic = 'Why will AI change the world'
#response = chain.invoke(input=topic)
#print(response)


#funtion to get the response 
def get_response(data,style):
    prompt_template = PromptTemplate.from_template("""
        Topic content: {data}. User has selected {style} category
                                                   The provided content is sourced from Wikipedia. Understand and summarize it according to the style the user wants it in. Here is a manual for you to understand user's intent.
                                                   If category is "For presentations" then: Create detailed, structured summaries suitable for academic or professional submissions.
                                                   If category is "General Knowledge & Understanding" then: Summarize the topic in plain and simple language suitable for a general audience, avoiding technical terms.
                                                   If category is "Fact-Checking" then: Provide a factual, bullet-pointed summary of the topic, emphasizing verifiable information and avoiding interpretations.
                                                    NO PREAMBLE
                                                   """
    )
    prompt_template.invoke({"data": data, "style": style})
    chain_response =  prompt_template| llm
    try:
        res = chain_response.invoke({"data": data,"style": style})
        return res.content
    
    except Exception :
        return None