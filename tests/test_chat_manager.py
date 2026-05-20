import pytest

from ai_project_coach_chatbot.models.chat import ChatManager


def test_create_chat():
    manager = ChatManager()

    manager.create_chat(user_id="user1", chat_id="chat1")

    chat = manager.get_chat(user_id="user1", chat_id="chat1")

    assert chat is not None
    assert chat["messages"] == []


def test_add_message():
    manager = ChatManager()
    manager.create_chat(user_id="user1", chat_id="chat1")

    manager.add_message(
        user_id="user1",
        chat_id="chat1",
        role="user",
        content="Hello",
    )

    conversation = manager.get_conversation(user_id="user1", chat_id="chat1")

    assert conversation == [
        {
            "role": "user",
            "content": "Hello",
        }
    ]


def test_add_message_to_missing_chat_raises_error():
    manager = ChatManager()

    with pytest.raises(ValueError, match="Chat not found"):
        manager.add_message(
            user_id="user1",
            chat_id="missing-chat",
            role="user",
            content="Hello",
        )