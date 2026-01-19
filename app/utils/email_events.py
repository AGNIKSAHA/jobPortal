from app.utils.email import send_email
from app.utils.email_templetes import (
    new_job_posted,
    application_confirmation,
    employer_notification,
)

def notify_candidates_new_job(candidates, job):
    for candidate in candidates:
        send_email(
            to_email=candidate.email,
            subject="New Job Opportunity",
            html_body=new_job_posted(candidate.name, job.title),
        )


def send_application_confirmation(candidate, job):
    send_email(
        to_email=candidate.email,
        subject="Application Submitted",
        html_body=application_confirmation(candidate.name, job.title),
    )


def notify_employer_new_application(employer, job):
    send_email(
        to_email=employer.email,
        subject="New Job Application",
        html_body=employer_notification(employer.name, job.title),
    )
