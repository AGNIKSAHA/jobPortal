from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Employer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str
    industry: str
    contact_email: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    location: Optional[str] = None   