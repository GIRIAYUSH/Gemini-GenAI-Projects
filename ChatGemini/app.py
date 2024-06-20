from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st 
import os 
import google.generativeai as genai


genai.configure(api_key=os.getenv("Gemini_Api"))

### function to load gemini pro model and get responses. 

model=genai.GenerativeModel("gemini-pro")
def get_gemnini_response(question):
    response=model.generate_content(question)
    return response.text



st.set_page_config(page_title="QandA Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemnini_response(input)
    st.subheader("The response is")
    st.write(response)



