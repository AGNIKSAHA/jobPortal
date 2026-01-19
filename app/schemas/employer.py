from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime


# ---------------------------------------------------
# Base schema
# ---------------------------------------------------
class EmployerBase(SQLModel):
    company_name: str                 # Company name
    industry: str                     # Industry type
    contact_email: str                # Official email
    location: Optional[str] = None    # Company location



# ---------------------------------------------------
# Create schema
# ---------------------------------------------------
class EmployerCreate(EmployerBase):
    pass


# ---------------------------------------------------
# Update schema
# ---------------------------------------------------
class EmployerUpdate(SQLModel):
    company_name: Optional[str] = None
    industry: Optional[str] = None
    contact_email: Optional[str] = None
    location: Optional[str] = None


# ---------------------------------------------------
# Read schema
# ---------------------------------------------------
class EmployerRead(EmployerBase):
    id: int
    created_at: datetime


