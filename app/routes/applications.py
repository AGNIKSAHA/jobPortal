from fastapi import APIRouter, Depends, BackgroundTasks
from typing import List
from sqlmodel import Session
from app.core.deps import get_session
from app.models.application import Application
from app.schemas.application import (
    ApplicationCreate,
    ApplicationRead,
    ApplicationStatusUpdate
)
from app.services.application_service import (
    apply_job,
    update_application_status
)

from app.models.application_read import ApplicationWithCandidate, ApplicationWithJob
from app.services.application_query import get_applications_by_job, get_applications_by_candidate
from app.services.email_service import send_application_emails

router = APIRouter()


@router.post("/apply")
def apply(
    payload: ApplicationCreate,
    background_tasks: BackgroundTasks,
    session: Session = Depends(get_session),
):
    application = apply_job(payload, session)

    # 🔔 Background email task
    assert application.id is not None
    background_tasks.add_task(
        send_application_emails,
        application.id,
        session,
    )

    return application



@router.get(
    "/candidate/{candidate_id}",
    response_model=List[ApplicationWithJob]
)
def get_applications_for_candidate(
    candidate_id: int,
    session: Session = Depends(get_session)
):
    return get_applications_by_candidate(session, candidate_id)


@router.get(
    "/job/{job_id}",
    response_model=List[ApplicationWithCandidate]
)
def get_applications_for_job(
    job_id: int,
    session: Session = Depends(get_session)
):
    return get_applications_by_job(session, job_id)



@router.patch("/{application_id}/status", response_model=ApplicationRead)
def update_status(
    application_id: int,
    payload: ApplicationStatusUpdate,
    session: Session = Depends(get_session)
):
    return update_application_status(application_id, payload, session)
