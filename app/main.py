from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.history import router as history_router

app = FastAPI(
    title="AI-Powered Document Assistant",
    version="1.0.0",
    description="A Retrieval-Augmented Generation (RAG) API for answering questions from PDF documents."
)

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Register API Routers
# -----------------------------
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(history_router)


@app.get(
    "/",
    tags=["Health Check"]
)
def root():
    return {
        "message": "AI-Powered Document Assistant API is running."
    }


@app.get(
    "/health",
    tags=["Health Check"]
)
def health():
    return {
        "status": "healthy"
    }