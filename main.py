import streamlit as st
import pdfplumber
 
st.set_page_config(
    page_icon="📚",
    page_title="FlashCard",
    layout="wide"
)

st.header("AI ANki Maker")
cl1, cl2, cl3 = st.columns([2,3,2])
with cl2:
    b=st.file_uploader("Upload PDF",type=["pdf"])
    a=st.button("Submit")

if a and b:
    st.balloons()
elif a:
    with cl2:
        st.warning("Please upload file first")




