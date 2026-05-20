import uuid

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ai_project_coach_chatbot.core.config import BASE_DIR
from ai_project_coach_chatbot.core.dependencies import get_chat_service
from ai_project_coach_chatbot.schemas.chat_schema import (
    CreateChatResponse,
    SendMessageRequest,
    SendMessageResponse,
)
from ai_project_coach_chatbot.services.chat_service import ChatService


router = APIRouter()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def get_or_create_user_id(request: Request) -> str:
    """Use the signed browser session to identify the current user."""
    if "user_id" not in request.session:
        request.session["user_id"] = str(uuid.uuid4())
    return request.session["user_id"]


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    get_or_create_user_id(request)
    return templates.TemplateResponse(request, "chat.html")


@router.post("/api/create_chat", response_model=CreateChatResponse)
async def create_chat(
    request: Request,
    chat_service: ChatService = Depends(get_chat_service),
):
    user_id = get_or_create_user_id(request)
    chat_id = chat_service.create_chat(user_id=user_id)

    return CreateChatResponse(
        chat_id=chat_id,
        message="Chat created successfully",
    )


@router.post("/api/send_message", response_model=SendMessageResponse)
async def send_message(
    request: Request,
    payload: SendMessageRequest,
    chat_service: ChatService = Depends(get_chat_service),
):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Session expired")

    try:
        ai_response = chat_service.process_message(
            user_id=user_id,
            chat_id=payload.chat_id,
            message=payload.message,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return SendMessageResponse(message=ai_response)