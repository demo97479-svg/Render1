import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client = OpenAI()
st.set_page_config(page_title="PDF based Q and A App",layout="centered")
st.title("🟥PDF based Q and A App")
with st.sidebar:
    st.header("AI Powered Resume Intelligence")
    question=st.text_input("Enter Job Role")
    file=st.file_uploader("Upload a file",type=["pdf"])
if file is not None:   #not none= uploaded a pdf      none- not uploaded pdf
    reader=PdfReader(file)
    pdf_text=" "
    for page in reader.pages:
        text=page.extract_text()
        pdf_text=pdf_text+text+"\n"
    if st.button("View Analysis"):
        prompt=f'''from {pdf_text}
- Extract resume content, including education, technical skills, experience, and projects.
- Compare resume content with the job role {question}.
- Generate a compatibility score.
- Identify matching skills and missing or underrepresented skills.
- Provide actionable suggestions for resume improvement.
- Generate a structured analysis report for the candidate.
-	Give ATS Score also.
'''
        response=client.responses.create(model="gpt-4.1-mini",input=prompt)
        st.write(response.output_text)
else:
    st.write("File not found")    
       