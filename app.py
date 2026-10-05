import time
import streamlit as st
from src.agent import run_agent

st.set_page_config(page_title="Amazn AI", page_icon="♾️")
st.markdown("""<style>
.stApp {background: radial-gradient(circle at top, #15213D 0%, #0A101F 60%);}
#MainMenu, footer {visibility: hidden;}
[data-testid="stSidebar"] {background: #0D1526; border-right: 1px solid #22304F;}
[data-testid="stChatMessage"] {background: #111B33; border: 1px solid #22304F; border-radius: 14px;}
.stButton > button {width: 100%; text-align: left; background: #111B33; color: #DCE6F8; border: 1px solid #2F4372;}
.stButton > button:hover {border-color: #FF9900; color: #FF9900;}
h1 {background: linear-gradient(90deg, #FF9900, #22D3EE); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
</style>""", unsafe_allow_html=True)
EXAMPLES = [
    "Find the best products under ₹4,000",
    "How can I return a product?",
    "How long does a refund take?",
    "Where is my order ORD1026?",
]

def stream(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.01)

if "messages" not in st.session_state:
    st.session_state.messages = []
with st.sidebar:
    st.subheader("Try asking")
    for ex in EXAMPLES:
        if st.button(ex):
            st.session_state.example = ex
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

st.title("Amazn AI")
st.caption("Product search, customer support and live order tracking in one assistant")
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

query = st.chat_input("Ask about products, orders, returns, refunds...") or st.session_state.pop("example", None)
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    with st.chat_message("assistant"):
        try:
            with st.status("Searching tools and thinking...") as status:
                answer = str(run_agent(query))
                status.update(label="Done", state="complete")
            st.write_stream(stream(answer))
        except Exception as e:
            answer = "Sorry, something went wrong while processing that. Please try again."
            st.error(answer)
            st.caption(f"Details: {e}")
    st.session_state.messages.append({"role": "assistant", "content": answer})
