import os, sys
from dotenv import load_dotenv
load_dotenv()
file = os.environ['FILE_PATH']
sys.path.append(file)

from app.db.base import Base
from sqlalchemy import String, Column, Integer


class Customer(Base):


