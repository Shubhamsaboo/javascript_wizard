import streamlit as st
import pandas as pd
from gpt3_prompt import generate_prompt

st.set_page_config(
    page_title="JS Chatbot",
    page_icon="🤖",
    layout="centered")

st.sidebar.image("artifacts/giphy.gif", use_column_width=True)

api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

st.sidebar.write("Made with ❤️ by [@Saboo_Shubham_](https://twitter.com/Saboo_Shubham_)")

st.sidebar.write("Powered by [OpenAI](https://openai.com/) & [Streamlit](https://streamlit.io/)")

if api_key:
    st.title("Java Script Wizard 🪄 ")
    
    st.image("artifacts/js_wiz.png")

    inp = st.text_input('Describe your Query! 📚')
    
    if st.button('Submit ✨'):
        # Generate the caption
        answer = generate_prompt(inp, api_key)

        st.write("Response 👇")

        # Show the image    
        st.info(answer)
        
else:
    st.error("🔑 API Key Not Found!")
    st.write("💡 No OpenAI API key? Get yours [here](https://openai.com/blog/api-no-waitlist/)!")