# NOTE:
# This file contains ONLY email-related business logic.
# Actual SMTP client lives in app/utils/email.py

from sqlmodel import Session, select

from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job
from app.models.employer import Employer

from app.utils.email import send_email
from app.utils.email_templetes import (
    application_confirmation,
    employer_notification,
    new_job_posted
)

# def send_application_emails(
#     application: Application,
#     session: Session,
# ) -> None:
#     """
#     Send all emails related to a job application:
#     1. Confirmation email to candidate
#     2. Notification email to employer
#     """

#     # -------------------------------------------------
#     # Fetch related entities (single responsibility)
#     # -------------------------------------------------
#     candidate = session.get(Candidate, application.candidate_id)
#     job = session.get(Job, application.job_id)

#     if candidate is None or job is None:
#         # Data integrity issue; do not attempt emails
#         return

#     employer = session.get(Employer, job.employer_id)
#     if employer is None:
#         return

#     # -------------------------------------------------
#     # Email to Candidate (Confirmation)
#     # -------------------------------------------------
#     send_email(
#         to_email=candidate.email,
#         subject="Application Submitted Successfully",
#         html_body=application_confirmation(
#             candidate_name=candidate.name,
#             job_title=job.title,
#         ),
#     )

#     # -------------------------------------------------
#     # Email to Employer (New Application Notification)
#     # -------------------------------------------------
#     send_email(
#         to_email=employer.contact_email,
#         subject="New Candidate Applied for Your Job",
#         html_body=employer_notification(
#             employer_name=employer.company_name,
#             job_title=job.title,
#         ),
#     )


def send_application_emails(
    application_id: int,
    session: Session,
) -> None:
    """
    Background task: send application-related emails
    """

    application = session.get(Application, application_id)
    if not application:
        return

    candidate = session.get(Candidate, application.candidate_id)
    job = session.get(Job, application.job_id)

    if not candidate or not job:
        return

    employer = session.get(Employer, job.employer_id)
    if not employer:
        return

    # Candidate confirmation
    send_email(
        to_email=candidate.email,
        subject="Application Submitted",
        html_body=application_confirmation(
            candidate_name=candidate.name,
            job_title=job.title,
        ),
    )

    # Employer notification
    send_email(
        to_email=employer.contact_email,
        subject="New Job Application",
        html_body=employer_notification(
            employer_name=employer.company_name,
            job_title=job.title,
        ),
    )


def notify_candidates_new_job(
    job_id: int,
    session: Session,
) -> None:
    job = session.get(Job, job_id)
    if not job:
        return

    candidates = session.exec(select(Candidate)).all()

    for candidate in candidates:
        send_email(
            to_email=candidate.email,
            subject="New Job Posted",
            html_body=new_job_posted(
                candidate_name=candidate.name,
                job_title=job.title,
            ),
        )



