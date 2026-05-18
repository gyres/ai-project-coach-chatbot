import uuid
from pathlib import Path

from openai import OpenAI, OpenAIError

from app.core.config import Settings
from app.models.chat import ChatManager


class ChatService:
    """Business logic for creating chats and generating assistant replies."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.chat_manager = ChatManager()
        self.openai_client = OpenAI(api_key=settings.openai_api_key)
        self.system_prompt = self.load_system_prompt(settings.system_prompt_path)

    def load_system_prompt(self, file_path: Path) -> str:
        """Load the system prompt from file."""
        try:
            return file_path.read_text(encoding="utf-8")
        except OSError as exc:
            raise RuntimeError(f"Unable to load system prompt: {exc}") from exc

    def create_chat(self, user_id: str) -> str:
        """Create a new chat session for a user."""
        chat_id = str(uuid.uuid4())
        self.chat_manager.create_chat(user_id=user_id, chat_id=chat_id)
        return chat_id

    def process_message(self, user_id: str, chat_id: str, message: str) -> str:
        """Store the user message, call OpenAI, then store the assistant response."""
        if self.chat_manager.get_chat(user_id, chat_id) is None:
            raise ValueError("Chat not found")

        self.chat_manager.add_message(
            user_id=user_id,
            chat_id=chat_id,
            role="user",
            content=message,
        )

        try:
            response = self.openai_client.responses.create(
                model=self.settings.openai_model,
                instructions=self.system_prompt,
                input=self.chat_manager.get_conversation(user_id, chat_id),
                temperature=0.7,
                max_output_tokens=900,
                store=False,
            )
        except OpenAIError as exc:
            raise RuntimeError(f"OpenAI API request failed: {exc}") from exc

        ai_message = response.output_text.strip()
        if not ai_message:
            raise RuntimeError("OpenAI returned an empty response")

        self.chat_manager.add_message(
            user_id=user_id,
            chat_id=chat_id,
            role="assistant",
            content=ai_message,
        )

        return ai_message