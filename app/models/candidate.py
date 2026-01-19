from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
from sqlalchemy import Column, JSON
from enum import Enum

class ExperienceLevel(str, Enum):
    FRESHER = "FRESHER"
    JUNIOR = "JUNIOR"
    MID = "MID"
    SENIOR = "SENIOR"


class JobType(str, Enum):
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"
    INTERNSHIP = "INTERNSHIP"

class Candidate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    email: str

    
    skills: List[str] = Field(
        sa_column=Column(JSON),
        default_factory=list
    )

    experience_level: ExperienceLevel
    preferred_job_type: JobType
    preferred_location: Optional[str] = None 

    created_at: datetime = Field(default_factory=datetime.utcnow)