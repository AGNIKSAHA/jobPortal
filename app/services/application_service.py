from sqlmodel import Session, select
from fastapi import HTTPException

from app.models.application import Application
from app.models.job import Job,JobStatus
from app.schemas.application import (
    ApplicationCreate,
    ApplicationStatusUpdate,
    ApplicationStatus
)
from app.services.email_service import send_application_emails


def apply_job(payload: ApplicationCreate, session: Session) -> Application:
    job = session.get(Job, payload.job_id)
    if not job or job.status != JobStatus.PUBLISHED:
        raise HTTPException(410, "Job is not available")

    existing = session.exec(
        select(Application).where(
            Application.job_id == payload.job_id,
            Application.candidate_id == payload.candidate_id,
        )
    ).first()

    if existing:
        raise HTTPException(409, "Already applied to this job")

    application = Application(**payload.model_dump())

    session.add(application)
    session.commit()
    session.refresh(application)

    return application




def update_application_status(
    application_id: int,
    payload: ApplicationStatusUpdate,
    session: Session
) -> Application:
    application = session.get(Application, application_id)
    if not application:
        raise HTTPException(404, "Application not found")

    application.status = payload.status

    session.add(application)
    session.commit()
    session.refresh(application)

    return application
