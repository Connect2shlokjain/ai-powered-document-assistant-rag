from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.utils.config import settings


class ChunkService:
    """
    Service responsible for splitting extracted text
    into smaller overlapping chunks.
    """

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_text(self, text: str) -> list[str]:
        """
        Split text into chunks.

        Args:
            text (str): Extracted document text.

        Returns:
            list[str]: List of text chunks.
        """
        return self.text_splitter.split_text(text)