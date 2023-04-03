from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config.settings import settings

engine = create_engine(settings.POSTGRESQL_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
