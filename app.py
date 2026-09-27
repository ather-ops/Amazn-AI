import streamlit as st
from src.agent import amazn_agent

st.set_page_config(
    page_title="Amazn AI",
    page_icon="♾️"
)

st.title("♾️ Amazn AI")
st.caption("Amazon product and customer support assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input(
    "Ask about products, orders, returns, refunds..."
)

if query:
    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = amazn_agent.run(query)
                st.markdown(answer)
            except Exception as e:
                answer = f"Error: {e}"
                st.error(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
