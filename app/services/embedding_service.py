from sentence_transformers import SentenceTransformer

from app.utils.config import settings


class EmbeddingService:
    """
    Service responsible for generating embeddings
    for document chunks and user queries.
    """

    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def generate_embedding(self, text: str) -> list[float]:
        """
        Generate embedding for a single text.

        Args:
            text (str): Input text.

        Returns:
            list[float]: Embedding vector.
        """
        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()

    def generate_embeddings(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.

        Args:
            texts (list[str]): List of text chunks.

        Returns:
            list[list[float]]: List of embedding vectors.
        """
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.tolist()