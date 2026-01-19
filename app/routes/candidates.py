from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.deps import get_session
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateRead, CandidateUpdate
from app.utils.db_helpers import get_or_404
router = APIRouter()


@router.post("/", response_model=Candidate, status_code=201)
def create_candidate(
    payload: Candidate,
    session: Session = Depends(get_session)
):
    session.add(payload)
    session.commit()
    session.refresh(payload)
    return payload


@router.get("/{candidate_id}", response_model=CandidateRead)
def get_candidate(
    candidate_id: int,
    session: Session = Depends(get_session)
):
    candidate = get_or_404(
        session=session,
        model=Candidate,
        obj_id=candidate_id,
        resource_name="Candidate"
    )

    return candidate


@router.put("/{candidate_id}", response_model=CandidateRead)
def update(
    candidate_id: int,
    payload: CandidateUpdate,
    session: Session = Depends(get_session)
):
    candidate = session.get(Candidate, candidate_id)
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(candidate, k, v)
    session.add(candidate)
    session.commit()
    session.refresh(candidate)
    return candidate


@router.patch("/{candidate_id}", response_model=Candidate)
def update_candidate(
    candidate_id: int,
    payload: CandidateUpdate,
    session: Session = Depends(get_session)
):
    candidate = get_or_404(session, Candidate, candidate_id, "Candidate")

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(candidate, field, value)

    session.add(candidate)
    session.commit()
    session.refresh(candidate)

    return candidate

