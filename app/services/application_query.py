from sqlmodel import select, col
from sqlmodel import Session
from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job

def get_applications_by_job(
    session: Session,
    job_id: int
):
    statement = (
    select(Application, Candidate)
    .join(
        Candidate,
        col(Candidate.id) == col(Application.candidate_id)
    )
    .where(col(Application.job_id) == job_id)
)

    results = session.exec(statement).all()

    # reshape result into response-friendly objects
    applications = []
    for application, candidate in results:
        applications.append({
            "id": application.id,
            "job_id": application.job_id,
            "status": application.status,
            "applied_at": application.applied_at,
            "candidate": candidate
        })

    return applications

def get_applications_by_candidate(
    session: Session,
    candidate_id: int
):
    statement = (
        select(Application, Job)
        .join(
            Job,
            col(Job.id) == col(Application.job_id)
        )
        .where(col(Application.candidate_id) == candidate_id)
        .order_by(col(Application.applied_at).desc())
    )

    results = session.exec(statement).all()

    return [
        {
            "id": application.id,
            "job_id": application.job_id,
            "status": application.status,
            "applied_at": application.applied_at,
            "job": job,
        }
        for application, job in results
    ]

