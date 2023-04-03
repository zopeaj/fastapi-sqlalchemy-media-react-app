from pydantic import BaseSettings
from typing import Any, Optional

class Settings(BaseSettings):
    POSTGRESQL_DATABASE_URL: Optional[str] = None
    SERVER_NAME: Optional[str] = None
    LOCAL_VAR_APP_IMAGES: Optional[str] = None

    class Meta:
        config = '.env'

settings = Settings()
