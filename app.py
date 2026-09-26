import sys
from pathlib import Path
import streamlit as st
from src.rag import ask_product_rag

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))
st.set_page_config(
    page_title="Amazn AI",
    page_icon="♾️"
)

st.title("Amazn AI")
st.write(
    "Your smart Amazon product finder "
    "and customer support AI assistant."
)

query = st.text_input(
    "Ask Amazn AI something!",
    placeholder="Ask about product recommendations..."
)

if st.button("Find Products"):

    if not query.strip():
        st.warning("First enter what you want!")
    else:
        try:
            with st.spinner("Amazn  is thinking..."):
                answer = ask_product_rag(query)

            st.write(answer)

        except Exception as e:
            st.error("Something went wrong. Please try again.")
            print(f"Amazon AI error: {e}")
