from sqlmodel import Session, select
from fastapi import HTTPException

from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate,JobStatus
from app.services.email_service import notify_candidates_new_job
# ---------------------------------------------------
# Create a new job
# ---------------------------------------------------
# def create_job(
#     *,
#     session: Session,
#     employer_id: int,
#     payload,
# ) -> Job:
#     """
#     Create a new job post.
#     """
#     data = payload.model_dump(exclude={"employer_id","status"})
#     job = Job(
#         employer_id=employer_id,
#         **data,
#         status=JobStatus.PUBLISHED,  # or default in model
#     )

#     session.add(job)
#     session.commit()
#     session.refresh(job)

#     # 🔔 EMAIL TRIGGER (AFTER COMMIT)
#     notify_candidates_new_job(job, session)

#     return job

def create_job(
    *,
    session: Session,
    employer_id: int,
    payload,
) -> Job:
    data = payload.model_dump(exclude={"employer_id", "status"})

    job = Job(
        employer_id=employer_id,
        **data,
        status=JobStatus.PUBLISHED,
    )

    session.add(job)
    session.commit()
    session.refresh(job)

    return job

# ---------------------------------------------------
# Get job by ID
# ---------------------------------------------------
def get_job(job_id: int, session: Session) -> Job:
    job = session.get(Job, job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job
# ---------------------------------------------------
# Update job
# ---------------------------------------------------
def update_job(job_id: int, payload: JobUpdate, session: Session) -> Job:
    job = get_job(job_id, session)

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(job, key, value)

    session.add(job)
    session.commit()
    session.refresh(job)
    return job
# ---------------------------------------------------
# Delete job
# ---------------------------------------------------
def delete_job(job_id: int, session: Session) -> None:
    job = get_job(job_id, session)
    session.delete(job)
    session.commit()
