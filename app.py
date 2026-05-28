from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest")

#Gemini response function
def get_gemini_response(input_prompt, image_data, user_query):
    response = model.generate_content([input_prompt, image_data[0],user_query])
    return response.text

#Image processing function
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


st.set_page_config(
    page_title = "ROBOBILL",
    page_icon="💪",
    layout = "centered",
)
#sidebar
st.sidebar.title("Robobill 💪💪")
st.sidebar.write("Ai- powered expense assistant")
st.sidebar.info("""
How to use:
1.upload an image of a bill/receipt
2.give a prompt
3.click the submit button
"""    
)
st.sidebar.success("Powered by Gemini AI")

#main page
st.title("RoboBill 💪")
st.subheader("AI powered agentic system that uses your bills to generate an expense report")
st.write("""
Upload your bills or invoices image into our website and get your expenses analyzed instantly.
         """)

input_query = st.text_input("Ask something about your bill",placeholder = "Summarize this bill and tell me the toal expense")
uploaded_file = st.file_uploader("Upload Receipt/Invoice Image",type=["jpg","jpeg","png","webp"])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(
        image,
        caption = "Uploaded Receipt",
        use_container_width = True
    )

submit = st.button("Analyze Bill")

input_prompt = """
You are an AI powered finance assistant
Analyze the uploaded receipt,invoice or bill carefully

Provide us:
1.Store or buisness name
2.Date of purchase
3.Total amount spent
4.List of purchased items
5.Expense summary
6.Feedback or suggestions on the spending

Rules: 
keep the formatting clean
use numbered points
make the response professional
keep the explainations beginner friendly

At the end thank the user for using RoboBill 💪
"""

if submit:
    if uploaded_file is not None:
        image_data = input_image_details(uploaded_file)
        with st.spinner("Analyzing your bill with Gemini Ai..."):
            response = get_gemini_response(input_prompt,image_data,input_query)
            st.subheader("Result of Analysis")
            st.write(response)
    else:
        st.warning("Please upload a receipt image first")