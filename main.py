import streamlit as st
import google.generativeai as genai
API_KEY = "AQ.Ab8RN6KqEtc4OOMdBvAShYAFi1hEZ8FkErGcFh8R4bu2jGSiNg"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("Ibrahim's A-Level Business studies Tutor")

question = st.text_area(
    "Welcome, Ask a Business Studies question"
)

if st.button("Submit"):
    prompt = f"""
    ...
    """

    response = model.generate_content(prompt)
    st.write(response.text)