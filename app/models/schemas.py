from pydantic import BaseModel, Field, field_validator


class CreateChatResponse(BaseModel):
    chat_id: str
    message: str


class SendMessageRequest(BaseModel):
    chat_id: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)

    @field_validator("chat_id", "message")
    @classmethod
    def must_not_be_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Value cannot be blank")
        return value


class SendMessageResponse(BaseModel):
    message: str