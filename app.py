import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import time
start = time.time()
from src.agent import amazn_agent
st.write(f"Import time: {time.time() - start:.1f}s")

st.set_page_config(
    page_title="Amazn AI",
    page_icon="♾️",
    layout="centered"
)
st.title("♾️ Amazn AI")
st.caption("Your smart Amazon product finder and customer support AI assistant")


query = st.text_input(
    "Ask Amazn AI something!",
    placeholder="Ask about product recommendations..."
)

col1, col2 = st.columns([1, 4])
with col1:
    go = st.button("Get result", use_container_width=True)

if go:
    if not query.strip():
        st.warning("First enter what you want!")
    else:
        try:
            with st.spinner("Amazn is thinking..."):
                answer = amazn_agent.run(query)

            st.success("Answer ready")
            with st.container(border=True):
                st.markdown(answer)

            with st.expander("Show query details"):
                st.write("**Query:**", query)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()
st.caption("Built with Streamlit • Powered by Groq + smolagents")
