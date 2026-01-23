from fastapi import APIRouter, Depends, HTTPException, Query,BackgroundTasks

from sqlmodel import Session, select
from typing import List, Optional

from app.core.deps import get_session
from app.models.job import Job, JobType, JobStatus
from app.schemas.job import JobCreate, JobRead, JobUpdate
from app.services.job_service import create_job, get_job, update_job, delete_job
from app.services.job_query import build_job_query
from app.utils.pagination import apply_pagination
from app.services.email_service import notify_candidates_new_job
router = APIRouter()


# @router.post("/")
# def create(payload: JobCreate, session: Session = Depends(get_session)):
#     return create_job(
#         session=session,
#         employer_id=payload.employer_id,
#         payload=payload,
#     )
@router.post("/")
def create(
    payload: JobCreate,
    background_tasks: BackgroundTasks,
    session: Session = Depends(get_session),
):
    job = create_job(
        session=session,
        employer_id=payload.employer_id,
        payload=payload,
    )

    assert job.id is not None

    # 🔔 Background email task
    background_tasks.add_task(
        notify_candidates_new_job,
        job.id,
        session,
    )

    return job

# @router.get("/", response_model=List[JobRead])
# def list_jobs(session: Session = Depends(get_session)):
#     return session.exec(select(Job)).all()

@router.get("/", response_model=List[JobRead])
def list_jobs(
    session: Session = Depends(get_session),

    # pagination
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),

    # infinite scroll
    cursor: Optional[int] = None,

    # search & filters
    q: Optional[str] = None,
    location: Optional[str] = None,
    job_type: Optional[JobType] = None,
    experience_level: Optional[str] = None,
    status: Optional[JobStatus] = None,
):
    statement = build_job_query(
        q=q,
        location=location,
        job_type=job_type,
        experience_level=experience_level,
        status=status,
        cursor=cursor,
    )

    statement = apply_pagination(
        statement,
        page=page,
        limit=limit,
        cursor=cursor
    )

    return session.exec(statement).all()



@router.get("/{job_id}", response_model=JobRead)
def retrieve(job_id: int, session: Session = Depends(get_session)):
    return get_job(job_id, session)


@router.put("/{job_id}", response_model=JobRead)
def update(job_id: int, payload: JobUpdate, session: Session = Depends(get_session)):
    return update_job(job_id, payload, session)
