import sys
import streamlit as st
from src.rag import ask_amazn

st.set_page_config(
    page_title="amazn ai",
    page_icon="♾️",
)
st.title("amazn ai")
st.write("Your smart amazon ai assiatant and customer support ai")

query=st.input_text(
    "Ask amazn ai something!",
    placeholder="ask about products recommedation"
)
if st.button("Find Products"):
    if not query.strip():
        st.warning("First enter what you want!")
    else:
        try:
           with st.spinner("X is Thinking"):
              answer=ask_amazn(query)
              st.write(answer)
        except Exception as e:
            st.error("Something went wrong. Please try again!")
