from fastapi import APIRouter
from app.services import chat_service
from app.models.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return chat_service.generate_response(request.question)