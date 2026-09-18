from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str
    stt_model: str = "whisper-1"
    stt_language: str = "pl"

    model_config = SettingsConfigDict(env_file=".env")

    model_name: str = "gpt-4o-mini" 
    faq_path: Path = Path("data/faq.md")


settings = Settings()