from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    MODE: str
    DRIVER: str
    USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[str] = None
    DB_NAME: str

    @property
    def URL(self):
        if self.MODE == "TEST":
            return f"{self.DRIVER}:///{self.DB_NAME}"
        return (
            f"{self.DRIVER}://{self.USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class DictConfig:
        env_file = ".env"


settings = Settings()
