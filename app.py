import streamlit as st
from autocorrect_engine import correct_text

st.set_page_config(
    page_title="AI Autocorrect Tool",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ AI Autocorrect Tool")

st.write("Enter a sentence with spelling mistakes.")

user_input = st.text_area(
    "Type Here",
    height=200
)

if st.button("Correct Sentence"):

    if user_input.strip() != "":

        corrected = correct_text(user_input)

        st.subheader("Corrected Sentence")

        st.success(corrected)

    else:
        st.warning("Please enter text.")