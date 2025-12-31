import streamlit as st
import requests

st.set_page_config(page_title="RAG PDF Chatbot")

st.title("📄 RAG-based PDF Chatbot")

API_URL = "http://127.0.0.1:8000/chat"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

question = st.text_input("Ask a question")

if st.button("Ask"):
    if not uploaded_files or not question:
        st.warning("Upload PDFs and enter a question.")
    else:
        with st.spinner("Thinking..."):
            files = [("files", (f.name, f, "application/pdf")) for f in uploaded_files]
            response = requests.post(
                API_URL,
                params={"question": question},
                files=files
            )

        if response.status_code == 200:
            data = response.json()
            st.session_state.chat_history.append({
                "q": question,
                "a": data["answer"],
                "sources": data["sources"]
            })

if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()

for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['q']}")
    st.markdown(f"**Bot:** {chat['a']}")
    with st.expander("Sources"):
        for src in chat["sources"]:
            st.write(src)
    st.markdown("---")
