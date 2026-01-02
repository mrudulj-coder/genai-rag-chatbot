# 📄 RAG-based PDF Chatbot

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions grounded strictly in the document content.  
The system combines semantic retrieval with an LLM to produce accurate, explainable answers.

---

## ✨ Features

- Upload and chat with **multiple PDF documents**
- Automatic PDF text extraction
- Intelligent chunking with overlap
- Semantic search using embeddings + FAISS
- Grounded answers (hallucination-aware)
- Source snippets shown for every answer
- FastAPI backend with Swagger UI
- Streamlit-based web interface
- Clean, modular architecture

---

## 🧠 How It Works (RAG Pipeline)

1. **PDF Upload**
   - User uploads one or more PDFs
2. **Text Extraction**
   - Text is extracted page-wise from PDFs
3. **Chunking**
   - Text is split into overlapping chunks
4. **Embedding**
   - Chunks are converted into vectors using SentenceTransformers
5. **Semantic Retrieval**
   - FAISS retrieves the most relevant chunks for a query
6. **Answer Generation**
   - LLM generates answers strictly from retrieved context
7. **Source Attribution**
   - Retrieved chunks are returned as answer sources

---

## 🏗️ Project Structure

```text
rag-pdf-chatbot/
├── app.py                  # FastAPI entry point
├── api/
│   └── routes.py           # API endpoints
├── core/
│   ├── llm_client.py       # LLM interface (Groq)
│   ├── embedder.py         # Text embeddings
│   ├── vector_store.py     # FAISS vector index
│   └── rag_pipeline.py    # End-to-end RAG logic
├── frontend/
│   └── streamlit_app.py    # Web interface
├── data/                   # Sample / temporary data
├── requirements.txt
├── .env                    # API keys (not committed)
├── .gitignore
└── README.md
```

---

## 🛠 Tech Stack

- **Language:** Python  
- **Backend:** FastAPI, Uvicorn  
- **Frontend:** Streamlit  
- **LLM:** LLaMA 3.1 via Groq API  
- **Embeddings:** SentenceTransformers  
- **Vector Store:** FAISS  
- **PDF Parsing:** PyPDF  

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/genai-rag-chatbot.git
cd genai-rag-chatbot
```

### 2️⃣ Create virtual environment
```bash
python -m venv .venv
```

Activate:
- **Windows**
```bash
.venv\Scripts\activate
```

- **Mac / Linux**
```bash
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables

Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the Application

### Backend (FastAPI)
```bash
uvicorn app:app --reload
```

Open Swagger UI:
```text
http://127.0.0.1:8000/docs
```

---

### Frontend (Streamlit)
In a new terminal:
```bash
streamlit run frontend/streamlit_app.py
```

The web UI will open automatically in your browser.

---

## 🧪 Example Usage

1. Upload one or more PDF documents
2. Ask a question such as:
   > *“Give me a brief understanding of machine learning”*
3. View:
   - Answer generated from documents
   - Source snippets used to generate the answer

---

## 🧩 Design Principles

- Retrieval is deterministic and transparent
- LLM is used **only after** retrieval
- Answers are grounded in document context
- Modular codebase for easy extension
- No black-box frameworks

---

## 🚧 Known Limitations

- Vector store is in-memory (resets on restart)
- No authentication
- No cloud deployment (local-only by design)

---

## 🔮 Future Improvements

- Persistent FAISS index
- Source highlighting with page numbers
- Streaming responses
- Frontend enhancements (chat UI, file management)
- Optional cloud deployment

---

## 📌 Disclaimer

This project is built for **learning and portfolio demonstration purposes**.  
LLM outputs should be validated before real-world usage.

---
