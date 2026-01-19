from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
from sqlalchemy import Column, JSON

from app.schemas.job import JobStatus, JobType


class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    employer_id: int

    title: str
    description: str
    location: str

    job_type: JobType
    experience_level: str

    skills: List[str] = Field(
        sa_column=Column(JSON),  # PostgreSQL JSON column
        default_factory=list
    )

    salary_min: Optional[int] = None
    salary_max: Optional[int] = None

    status: JobStatus = JobStatus.PUBLISHED

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )


