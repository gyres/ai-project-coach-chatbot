from functools import lru_cache

from ai_project_coach_chatbot.core.config import get_settings
from ai_project_coach_chatbot.services.chat_service import ChatService


@lru_cache
def get_chat_service() -> ChatService:
    """Create one ChatService instance for the app."""
    return ChatService(settings=get_settings())