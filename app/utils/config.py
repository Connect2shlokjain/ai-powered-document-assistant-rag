import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # ==============================
    # Groq Configuration
    # ==============================
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME")

    # ==============================
    # Embedding Model
    # ==============================
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    # ==============================
    # ChromaDB Configuration
    # ==============================
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME")

    # ==============================
    # Chunking Configuration
    # ==============================
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

    # ==============================
    # SQLite Configuration
    # ==============================
    DATABASE_URL = os.getenv("DATABASE_URL")


settings = Settings()