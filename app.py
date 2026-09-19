import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.vectordb import load_langchain_embedding
from src.vectordb import load_vector_store
from src.llm import load_llm
from src.rag import rag_with_llm
from src.llm import retrieve_documents
import streamlit as st

st.set_page_config(
    page_title="Amazn AI",
    page_icon="👾"
)

st.tile("Amazn AI")
st.write("Your smart AI assistant product finder with agent layer.")

query=st.text_input(
    "Ask amazn what product what product you are finding!",
    placeholder="Get product recemmendation"
)

if st.button("Find Product"):
    if not query.strip():
        st.warning("Fird add what product you are finding!")
    else:
        try:
            with st.spinner("Amazn ai is thinking"):
                answer=retrieve_documents(query)
                st.write(answer)
        except Exception as e:
            st.error("Something went wrong please try again!")
