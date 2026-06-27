from fastapi import APIRouter, HTTPException

from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse
from app.services.history_service import HistoryService
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/chat",
    tags=["Question Answering"]
)

rag_service = RAGService()
history_service = HistoryService()


@router.post(
    "/",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):
    """
    Ask questions from uploaded PDF documents.
    """

    try:
        result = rag_service.answer_question(
            question=request.question
        )

        history_service.save_chat(
            question=result["question"],
            answer=result["answer"]
        )

        return ChatResponse(
            question=result["question"],
            answer=result["answer"],
            sources=result["sources"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )