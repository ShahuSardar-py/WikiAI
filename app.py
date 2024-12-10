#imports
import streamlit as st
from wiki import search_and_fetch
from LLM import get_response

#setting streamlit page
st.set_page_config(
    page_icon='🤖',
    page_title="WikiAI"

)

st.title("WikiAI 📖")
st.markdown("Get reliable AI summaries for various usecases. Trusted inforamtion, sourced from :green[Wikipedia]")
st.divider()


user_input= st.text_input("Search WikiAI",
                          "Enter keywords")

content_style = st.selectbox(
    "I need summary for:",
    ["For presentations", "General Knowledge & Understanding", "Fact-Checking"]
)
submit= st.button("Search & Summarize", icon=":material/robot:")


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

with st.expander("About WikiAI"):
    st.write('''
        A simple LLM application running on Gemini 1.5 flash. Let's you get fast and personlized AI summaries with information soruced only from _Wikipedia_
    
    ''')

