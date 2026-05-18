from functools import lru_cache

from app.core.config import get_settings
from app.services.chat_service import ChatService


@lru_cache
def get_chat_service() -> ChatService:
    """Create one ChatService instance for the app."""
    return ChatService(settings=get_settings())