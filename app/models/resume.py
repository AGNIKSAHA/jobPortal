from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class Resume(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    candidate_id: int = Field(foreign_key="candidate.id")
    file_url: str
    file_type: str
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
