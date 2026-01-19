from sqlmodel import SQLModel
from datetime import datetime
from app.models.candidate import Candidate
from app.models.application import ApplicationStatus
from app.models.job import Job

class ApplicationWithCandidate(SQLModel):
    id: int
    job_id: int
    status: ApplicationStatus
    applied_at: datetime
    candidate: Candidate


class ApplicationWithJob(SQLModel):
    id: int
    job_id: int
    status: ApplicationStatus
    applied_at: datetime

    job: Job