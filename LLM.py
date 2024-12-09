import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0.9)

def get_response(data, style):
    prompt_template = PromptTemplate.from_template("""
        Topic content: {data}. User has selected {style} category
        The provided content is sourced from Wikipedia. Understand and summarize it according to the style the user wants it in.
        Here is a manual for you to understand user's intent.
        If category is "For presentations" then: Create detailed, structured summaries suitable for academic or professional submissions.
        If category is "General Knowledge & Understanding" then: Summarize the topic in plain and simple language suitable for a general audience, avoiding technical terms.
        If category is "Fact-Checking" then: Provide a factual, bullet-pointed summary of the topic, emphasizing verifiable information and avoiding interpretations.
        NO PREAMBLE
    """)
    try:
        chain_response = prompt_template | llm
        res = chain_response.invoke({"data": data, "style": style})
        return res.content
    except Exception:
        return None
