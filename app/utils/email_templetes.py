def new_job_posted(candidate_name: str, job_title: str) -> str:
    return f"""
    <h3>Hello {candidate_name},</h3>
    <p>A new job <b>{job_title}</b> has been posted that matches your profile.</p>
    <p>Log in to apply.</p>
    """


def application_confirmation(candidate_name: str, job_title: str) -> str:
    return f"""
    <h3>Hi {candidate_name},</h3>
    <p>Your application for <b>{job_title}</b> was submitted successfully.</p>
    """

def employer_notification(employer_name: str, job_title: str) -> str:
    return f"""
    <h3>Hello {employer_name},</h3>
    <p>A new candidate has applied for your job <b>{job_title}</b>.</p>
    """
