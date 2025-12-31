from fastapi import APIRouter, UploadFile, File
from core.rag_pipeline import (
    extract_text_from_pdfs,
    chunk_text,
    build_vector_store,
    rag_answer
)
import io

router = APIRouter()

@router.post("/chat")
def chat(question: str, files: list[UploadFile] = File(...)):
    file_buffers = [io.BytesIO(f.file.read()) for f in files]
    for buf, f in zip(file_buffers, files):
        buf.name = f.filename

    text, _ = extract_text_from_pdfs(file_buffers)
    chunks = chunk_text(text)

    vector_store, embedder = build_vector_store(chunks)
    answer, sources = rag_answer(question, vector_store, embedder)

    return {
        "answer": answer,
        "sources": sources
    }
