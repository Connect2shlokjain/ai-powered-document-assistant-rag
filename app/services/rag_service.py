import uuid

from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.chroma_service import ChromaService
from app.services.llm_service import LLMService


class RAGService:
    """
    Orchestrates the complete Retrieval-Augmented Generation (RAG) workflow.
    """

    def __init__(self):
        self.chunk_service = ChunkService()
        self.embedding_service = EmbeddingService()
        self.chroma_service = ChromaService()
        self.llm_service = LLMService()

    def index_document(self, pages: list[dict], filename: str):
        """
        Index a document page by page while preserving page numbers.
        """

        # -----------------------------------------
        # IMPORTANT
        # Every new upload starts with a fresh
        # knowledge base.
        # -----------------------------------------
        self.chroma_service.reset_collection()

        all_chunks = []
        all_embeddings = []
        all_metadata = []
        all_ids = []

        chunk_counter = 1

        for page in pages:

            page_number = page["page"]
            text = page["text"]

            if not text.strip():
                continue

            chunks = self.chunk_service.split_text(text)

            if not chunks:
                continue

            embeddings = self.embedding_service.generate_embeddings(chunks)

            for chunk, embedding in zip(chunks, embeddings):

                all_chunks.append(chunk)

                all_embeddings.append(embedding)

                all_metadata.append(
                    {
                        "source": filename,
                        "page": page_number,
                        "chunk": chunk_counter
                    }
                )

                all_ids.append(str(uuid.uuid4()))

                chunk_counter += 1

        self.chroma_service.add_documents(
            chunks=all_chunks,
            embeddings=all_embeddings,
            metadatas=all_metadata,
            ids=all_ids
        )

        return {
            "filename": filename,
            "chunks_indexed": len(all_chunks)
        }

    def answer_question(self, question: str):
        """
        Retrieve relevant chunks and generate an answer.
        """

        query_embedding = self.embedding_service.generate_embedding(question)

        results = self.chroma_service.similarity_search(
            query_embedding=query_embedding,
            top_k=5
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = "\n\n".join(documents)

        answer = self.llm_service.generate_answer(
            context=context,
            question=question
        )

        sources = []

        seen = set()

        for metadata in metadatas:

            key = (
                metadata["source"],
                metadata["page"],
                metadata["chunk"]
            )

            if key in seen:
                continue

            seen.add(key)

            sources.append(
                {
                    "document": metadata["source"],
                    "page": metadata["page"],
                    "chunk": metadata["chunk"]
                }
            )

        return {
            "question": question,
            "answer": answer,
            "sources": sources
        }