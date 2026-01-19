from sqlmodel import SQLModel
from typing import Optional, List
from datetime import datetime
from enum import Enum


# ---------------------------------------------------
# Job type enum
# ---------------------------------------------------
class JobType(str, Enum):
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"
    INTERNSHIP = "INTERNSHIP"
    FREELANCE = "FREELANCE"


# ---------------------------------------------------
# Job status enum
# ---------------------------------------------------
class JobStatus(str, Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    CLOSED = "CLOSED"


# ---------------------------------------------------
# Base schema
# ---------------------------------------------------
class JobBase(SQLModel):
    employer_id: int                  # Job owner
    title: str                        # Job title
    description: str                  # Job description
    location: str                     # Job location / Remote
    job_type: JobType                 # Type of job
    skills: List[str]                 # Required skills
    experience_level: str             # Experience requirement
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None

# ---------------------------------------------------
# Create schema
# ---------------------------------------------------
class JobCreate(JobBase):
    status: JobStatus = JobStatus.PUBLISHED


# ---------------------------------------------------
# Update schema
# ---------------------------------------------------
class JobUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    job_type: Optional[JobType] = None
    skills: Optional[List[str]] = None
    experience_level: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    status: Optional[JobStatus] = None


# ---------------------------------------------------
# Read schema
# ---------------------------------------------------
class JobRead(JobBase):
    id: int
    status: JobStatus
    created_at: datetime
