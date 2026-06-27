from typing import List

from pydantic import BaseModel


class SourceReference(BaseModel):
    document: str
    page: int
    chunk: int


class UploadResponse(BaseModel):
    message: str
    filename: str
    chunks_indexed: int


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: List[SourceReference]


class HealthResponse(BaseModel):
    status: str


class HistoryResponse(BaseModel):
    id: int
    question: str
    answer: str
    created_at: str