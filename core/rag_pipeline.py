from pypdf import PdfReader
from core.embedder import Embedder
from core.vector_store import VectorStore
from core.llm_client import LLMClient

def extract_text_from_pdfs(files):
    full_text = ""
    file_map = []

    for file in files:
        reader = PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + " "
                file_map.append(file.name)

    return full_text, file_map

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        chunks.append(text[start:start+chunk_size])
        start += chunk_size - overlap

    return chunks

def build_vector_store(chunks):
    embedder = Embedder()
    embeddings = embedder.embed_texts(chunks)

    store = VectorStore(len(embeddings[0]))
    store.add(embeddings, chunks)

    return store, embedder

def rag_answer(question, vector_store, embedder):
    query_embedding = embedder.embed_query(question)
    retrieved = vector_store.search(query_embedding)

    context = "\n\n".join([chunk for chunk, _ in retrieved])

    prompt = f"""
You are a document QA assistant.

CONTEXT:
{context}

QUESTION:
{question}

RULES:
- Answer strictly from context
- If missing, say so clearly
"""

    llm = LLMClient()
    answer = llm.generate(prompt)

    sources = [chunk[:200] + "..." for chunk, _ in retrieved]

    return answer, sources
