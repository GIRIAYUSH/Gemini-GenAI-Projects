from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai 
import os 
from PIL import Image
import streamlit as st


genai.configure(api_key=os.getenv("Gemini_Api"))

# Function to load Gemini-Pro-Vision 
model=genai.GenerativeModel("gemini-pro-vision")

#response function 
def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text
#converting image into byte stream data 
def input_image_setup(uploaded_file):
    if uploaded_file is not None: 
        bytes_data=uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError["No file Uploaded"]

#Initialize StreamLit Application 
st.set_page_config(page_title="Gemini Invoice Extractor")
st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file=st.file_uploader("Choose the image of your invoice",type=["jpg","jpeg","png"])

if uploaded_file is not None: 
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)


submit=st.button("Tell me about the invoice")

input_prompt="""
You are an expert in understanding invoices. We will upload an image as invoices and you will have to answer any questions based on the uploaded invoice image
"""

# If submit button is clicked 
if submit and uploaded_file:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is :")
    st.write(response)





