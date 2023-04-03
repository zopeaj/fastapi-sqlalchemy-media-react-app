import os, sys
from dotenv import load_dotenv
load_dotenv()
file = os.environ['FILE_PATH']
sys.path.append(file)

from typing import Generator
from app.db.session import SessionLocal


def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
