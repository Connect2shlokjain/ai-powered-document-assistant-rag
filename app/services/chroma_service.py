import chromadb
from chromadb.config import Settings

from app.utils.config import settings


class ChromaService:
    """
    Service responsible for interacting with ChromaDB.
    """

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_PATH,
            settings=Settings(anonymized_telemetry=False)
        )

        self.collection = self.client.get_or_create_collection(
            name=settings.COLLECTION_NAME
        )

    def add_documents(
        self,
        chunks: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
        ids: list[str]
    ):
        """
        Store document chunks and embeddings in ChromaDB.
        """

        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

    def similarity_search(
        self,
        query_embedding: list[float],
        top_k: int = 5
    ):
        """
        Retrieve the most relevant document chunks.
        """

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results

    def document_count(self):
        """
        Returns total indexed chunks.
        """

        return self.collection.count()

    def reset_collection(self):
        """
        Delete all stored embeddings.
        """

        self.client.delete_collection(settings.COLLECTION_NAME)

        self.collection = self.client.get_or_create_collection(
            name=settings.COLLECTION_NAME
        )