from sqlmodel import SQLModel
from datetime import datetime


# ---------------------------------------------------
# Upload schema
# Used in: POST /resumes/upload
# ---------------------------------------------------
class ResumeCreate(SQLModel):
    candidate_id: int                 # Owner of resume


# ---------------------------------------------------
# Read schema
# ---------------------------------------------------
class ResumeRead(SQLModel):
    id: int
    candidate_id: int
    file_url: str                     # Storage URL
    file_type: str                    # pdf / doc / docx
    uploaded_at: datetime


