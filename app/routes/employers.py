from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List

from app.core.deps import get_session
from app.models.employer import Employer
from app.models.job import Job
from app.schemas.employer import EmployerCreate, EmployerRead, EmployerUpdate


router = APIRouter()

@router.post("/", response_model=EmployerRead, status_code=201)
def create(payload: EmployerCreate, session: Session = Depends(get_session)):
    employer = Employer(**payload.model_dump())
    session.add(employer)
    session.commit()
    session.refresh(employer)
    return employer

@router.get("/{employer_id}", response_model=EmployerRead)
def get(employer_id: int, session: Session = Depends(get_session)):
    return session.get(Employer, employer_id)


@router.put("/{employer_id}", response_model=EmployerRead)
def update(
    employer_id: int,
    payload: EmployerUpdate,
    session: Session = Depends(get_session)
):
    employer = session.get(Employer, employer_id)
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(employer, k, v)
    session.add(employer)
    session.commit()
    session.refresh(employer)
    return employer


@router.get("/{employer_id}/jobs", response_model=List[Job])
def jobs(employer_id: int, session: Session = Depends(get_session)):
    return session.exec(
        select(Job).where(Job.employer_id == employer_id)
    ).all()

