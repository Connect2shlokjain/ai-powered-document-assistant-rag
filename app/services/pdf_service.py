import fitz
from pathlib import Path


class PDFService:
    """
    Service responsible for extracting text
    page by page from PDF documents.
    """

    @staticmethod
    def extract_text(pdf_path: str) -> list[dict]:
        """
        Extract text page-wise.

        Returns
        -------
        [
            {
                "page":1,
                "text":"..."
            },
            {
                "page":2,
                "text":"..."
            }
        ]
        """

        path = Path(pdf_path)

        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        document = fitz.open(pdf_path)

        pages = []

        for page_number, page in enumerate(document, start=1):

            text = page.get_text().strip()

            if text:

                pages.append(
                    {
                        "page": page_number,
                        "text": text
                    }
                )

        document.close()

        return pages