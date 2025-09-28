from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    redis_url: str = "redis://localhost:6379/0"
    external_api_url: str = "https://catfact.ninja/fact"
    env: str = "dev"
    model_config = ConfigDict(env_file=".env")


settings = Settings()
