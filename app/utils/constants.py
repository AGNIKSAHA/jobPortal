from enum import Enum

class JobStatus(str, Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    CLOSED = "CLOSED"

class ApplicationStatus(str, Enum):
    APPLIED = "APPLIED"
    SHORTLISTED = "SHORTLISTED"
    INTERVIEW = "INTERVIEW"
    REJECTED = "REJECTED"
    HIRED = "HIRED"

class JobType(str, Enum):
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"
    INTERNSHIP = "INTERNSHIP"
    FREELANCE = "FREELANCE"
