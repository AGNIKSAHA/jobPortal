from sqlmodel import Session
from fastapi import HTTPException

from app.models.resume import Resume
# ---------------------------------------------------
# Save resume metadata after upload
# ---------------------------------------------------
def create_resume(
    candidate_id: int,
    file_url: str,
    file_type: str,
    session: Session
) -> Resume:
    resume = Resume(
        candidate_id=candidate_id,
        file_url=file_url,
        file_type=file_type
    )

    session.add(resume)
    session.commit()
    session.refresh(resume)
    return resume
# ---------------------------------------------------
# Get resume by ID
# ---------------------------------------------------
def get_resume(resume_id: int, session: Session) -> Resume:
    resume = session.get(Resume, resume_id)
    if not resume:
        raise HTTPException(404, "Resume not found")
    return resume
