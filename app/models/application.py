from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
from enum import Enum

class ApplicationStatus(str, Enum):
    APPLIED = "APPLIED"
    REVIEWING = "REVIEWING"
    SHORTLISTED = "SHORTLISTED"
    REJECTED = "REJECTED"
    HIRED = "HIRED"  

class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int = Field(foreign_key="job.id")
    candidate_id: int = Field(foreign_key="candidate.id")
    resume_id: int = Field(foreign_key="resume.id")
    status: ApplicationStatus = Field(default=ApplicationStatus.APPLIED)
    applied_at: datetime = Field(default_factory=datetime.utcnow)
