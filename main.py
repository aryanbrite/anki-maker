import streamlit as st
import pdfplumber
from google import genai

st.set_page_config(
    page_icon="📚",
    page_title="FlashCard",
    layout="wide"
)
client=genai.Client(api_key="")

st.header("AI ANki Maker")
cl1, cl2, cl3 = st.columns([2,3,2])
with cl2:
    b=st.file_uploader("Upload PDF",type=["pdf"])
    a=st.button("Submit")

if a and b:
    st.balloons()
    with pdfplumber.open(b) as pdf:
        txt=""
        for i in pdf.pages:
            a=i.extract_text()
            if a:
                txt=txt+a
        prompt = f""" you are a flashcard generator. convert this text into question answer flashcard.
        rules 
        - keep answer short and concise. 
        - you are suposed to write based on the text i am providing.
        - no JSON
        - no extra text

        Return flashcards in this format:

        Q: ...
        A: ...

        Q: ...
        A: ...

        text:
        {txt}
        """

        responce= client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        s=responce.split("\n\n")
elif a:
    with cl2:
        st.warning("Please upload file first")








