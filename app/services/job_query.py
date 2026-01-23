from typing import Optional
from sqlmodel import select, col
from app.models.job import Job, JobType, JobStatus


def build_job_query(
    *,
    q: Optional[str] = None,
    location: Optional[str] = None,
    job_type: Optional[JobType] = None,
    experience_level: Optional[str] = None,
    status: Optional[JobStatus] = None,
    cursor: Optional[int] = None,
):
    statement = select(Job)

    # 🔍 search
    if q:
        statement = statement.where(
            col(Job.title).ilike(f"%{q}%") |
            col(Job.description).ilike(f"%{q}%")
        )

    # 🎯 filters
    if location:
        statement = statement.where(
            col(Job.location).ilike(f"%{location}%")
        )

    if job_type:
        statement = statement.where(Job.job_type == job_type)

    if experience_level:
        statement = statement.where(Job.experience_level == experience_level)

    if status:
        statement = statement.where(Job.status == status)

    if cursor:
        statement = statement.where(col(Job.id) < cursor)

    return statement.order_by(col(Job.id).desc())
