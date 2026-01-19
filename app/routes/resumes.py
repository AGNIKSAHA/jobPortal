from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlmodel import Session

from app.core.deps import get_session
from app.schemas.resume import ResumeRead
from app.services.resume_service import create_resume
from app.services.resume_service import create_resume, get_resume

router = APIRouter()



@router.post("/upload", response_model=ResumeRead, status_code=201)
def upload_resume(
    candidate_id: int,
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    if not file.content_type:
        raise HTTPException(400, "File type could not be determined")

    file_url = f"/uploads/{file.filename}"

    return create_resume(
        candidate_id=candidate_id,
        file_url=file_url,
        file_type=file.content_type,
        session=session
    )



@router.get("/{resume_id}", response_model=ResumeRead)
def read_resume(
    resume_id: int,
    session: Session = Depends(get_session)
):
    return get_resume(resume_id, session)

