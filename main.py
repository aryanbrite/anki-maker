import streamlit as st
import pdfplumber
from google import genai
import pandas as pd

st.set_page_config(
    page_icon="📚",
    page_title="FlashCard",
    layout="wide"
)
st.logo("https://cdn.hackclub.com/019e7928-ee48-79b3-8073-8098df0d8b90/Anki%20AI%20(1).png", size="large")


left, centre, right = st.columns([1,7,1])
with centre:
    st.title("Turn Medical Notes into Anki Cards in Seconds")
    st.caption("AI-powered flashcard generation for doctors and medical students.")
    st.divider()
    st.write("Doctors and medical students typically spend 1 to 4 hours per day making and reviewing Anki cards, It should be this hard !")
    st.write("")
    st.write("")





client=genai.Client(api_key=st.secrets["gemini_api"])

cl1, cl2, cl3 = st.columns([2,3,2])
with cl2:
    b=st.file_uploader("Upload PDF",type=["pdf"])
    a=st.button("Submit")

if a and b:
    with cl2:
        with st.spinner("Reading PDF"):
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
    with cl2:
        with st.spinner("Generating Flashcard"):
            responce= client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )
            result = responce.text
            blocks = result.strip().split("\n\n")

    flashcards = []

    for block in blocks:
        if "Q:" in block and "A:" in block:
            lines = block.split("\n")

            if len(lines) >= 2:
                q = lines[0].replace("Q:", "").strip()
                a = lines[1].replace("A:", "").strip()

                flashcards.append({"q": q, "a": a})
    cc1,cc2 = st.columns([8,2])
    with cc1:
        st.markdown("# Preview")
        st.divider()
        for card in flashcards:
            st.markdown(f"""
                        ### Question
                        {card["q"]}""")
            st.markdown(f"""
                        ### Answer
                        {card["a"]}""")
            st.divider()
    with cc2:
        df = pd.DataFrame(flashcards)
        csv = df.to_csv(index=False)
        st.download_button(
            label = "Download Anki File",
            file_name = "anki-maker.csv",
            mime = "text/csv",
            data=csv,
        )


    st.balloons()
elif a:
    with cl2:
        st.warning("Please upload file first")
        








