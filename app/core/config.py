import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]      # app/
PROJECT_ROOT = BASE_DIR.parent                      # repo root


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    session_secret_key: str
    openai_model: str = "gpt-5.4-nano"
    app_host: str = "0.0.0.0"
    app_port: int = 3000
    system_prompt_path: Path = BASE_DIR / "data" / "system_prompt.txt"


@lru_cache
def get_settings() -> Settings:
    """Load application settings once and reuse them."""
    load_dotenv(PROJECT_ROOT / ".env")

    openai_api_key = os.getenv("OPENAI_API_KEY")
    session_secret_key = os.getenv("SESSION_SECRET_KEY")

    if not openai_api_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Add it to your project root .env file."
        )

    if not session_secret_key:
        raise RuntimeError(
            "Missing SESSION_SECRET_KEY. Add it to your project root .env file."
        )

    return Settings(
        openai_api_key=openai_api_key,
        session_secret_key=session_secret_key,
        openai_model=os.getenv("OPENAI_MODEL", "gpt-5.4-nano"),
        app_host=os.getenv("APP_HOST", "0.0.0.0"),
        app_port=int(os.getenv("APP_PORT", "3000")),
    )