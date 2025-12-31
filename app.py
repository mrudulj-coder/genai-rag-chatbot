from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="RAG PDF Chatbot",
    description="Chat with PDFs using Retrieval-Augmented Generation",
    version="1.0"
)

app.include_router(router)
