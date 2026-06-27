import os
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.models.response_models import UploadResponse
from app.services.pdf_service import PDFService
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/upload",
    tags=["PDF Upload"]
)

UPLOAD_DIRECTORY = "uploaded_pdfs"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

pdf_service = PDFService()
rag_service = RAGService()


@router.post(
    "/",
    response_model=UploadResponse
)
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, extract text page-wise,
    generate embeddings, and store them in ChromaDB.
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = Path(UPLOAD_DIRECTORY) / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    pages = pdf_service.extract_text(str(file_path))

    result = rag_service.index_document(
        pages=pages,
        filename=file.filename
    )

    return UploadResponse(
        message="Document uploaded and indexed successfully.",
        filename=result["filename"],
        chunks_indexed=result["chunks_indexed"]
    )