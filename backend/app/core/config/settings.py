from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRESQL_DATABASE_URL: str

    class Meta:
        config = '.env'

settings = Settings()
