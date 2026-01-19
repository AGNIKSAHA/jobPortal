from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL =os.getenv("DB_URL") 
# "postgresql://postgres:9868@localhost:5432/library_db"
if not DATABASE_URL:
    raise RuntimeError("DB_URL environment variable is not set")

engine = create_engine(DATABASE_URL)

from app.models.job import Job
from app.models.employer import Employer
from app.models.candidate import Candidate
from app.models.application import Application
from app.models.resume import Resume

def init_db():
    SQLModel.metadata.create_all(engine)
