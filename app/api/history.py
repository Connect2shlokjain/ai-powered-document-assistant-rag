from fastapi import APIRouter

from app.services.history_service import HistoryService

router = APIRouter(
    prefix="/history",
    tags=["Chat History"]
)

history_service = HistoryService()


@router.get("/")
async def get_chat_history():
    """
    Retrieve complete chat history.
    """
    return history_service.get_history()


@router.delete("/")
async def clear_chat_history():
    """
    Delete all stored chat history.
    """
    history_service.clear_history()

    return {
        "message": "Chat history cleared successfully."
    }