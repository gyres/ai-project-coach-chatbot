from typing import Literal, TypedDict


Role = Literal["user", "assistant"]


class ChatMessage(TypedDict):
    role: Role
    content: str


class ChatData(TypedDict):
    messages: list[ChatMessage]


class ChatManager:
    """In-memory chat storage.

    For learning, this is okay. In production, replace this with a database or cache.
    """

    def __init__(self) -> None:
        self.chats: dict[str, dict[str, ChatData]] = {}

    def create_chat(self, user_id: str, chat_id: str) -> None:
        """Create a new chat for a user."""
        self.chats.setdefault(user_id, {})[chat_id] = {"messages": []}

    def get_chat(self, user_id: str, chat_id: str) -> ChatData | None:
        """Get a chat by user_id and chat_id."""
        return self.chats.get(user_id, {}).get(chat_id)

    def add_message(self, user_id: str, chat_id: str, role: Role, content: str) -> None:
        """Add a message to an existing chat."""
        chat = self.get_chat(user_id, chat_id)
        if chat is None:
            raise ValueError("Chat not found")

        chat["messages"].append({"role": role, "content": content})

    def get_conversation(self, user_id: str, chat_id: str) -> list[ChatMessage]:
        """Get the user/assistant conversation history."""
        chat = self.get_chat(user_id, chat_id)
        if chat is None:
            raise ValueError("Chat not found")

        return chat["messages"]