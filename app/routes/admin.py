from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.deps import get_session
from app.models.job import Job
from app.schemas.job import JobStatus

router = APIRouter()

@router.patch("/jobs/{job_id}/approve")
def approve(job_id: int, session: Session = Depends(get_session)):
    job = session.get(Job, job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    job.status = JobStatus.PUBLISHED
    session.add(job)
    session.commit()

    return {"message": "Job approved"}


@router.patch("/jobs/{job_id}/close")
def close(job_id: int, session: Session = Depends(get_session)):
    job = session.get(Job, job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    job.status = JobStatus.CLOSED
    session.add(job)
    session.commit()

    return {"message": "Job closed"}

