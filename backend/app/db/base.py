import os, sys
from dotenv import load_dotenv
load_dotenv()
file = os.environ['FILE_PATH']
sys.path.append(file)

from app.db.base_class import Base

