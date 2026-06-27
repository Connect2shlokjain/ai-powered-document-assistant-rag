from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Request model for asking questions.
    """

    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Question to ask from the uploaded documents."
    )