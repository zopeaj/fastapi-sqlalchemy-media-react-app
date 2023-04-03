from typing import Generator
from app.db.session import SessionLocal


def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
