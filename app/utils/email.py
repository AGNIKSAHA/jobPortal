import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings


def send_email(
    to_email: str,
    subject: str,
    html_body: str,
) -> None:
    """
    Send an HTML email using SMTP.

    - Uses settings from app.core.config
    - Respects EMAIL_ENABLED flag
    - Raises clear errors if config is missing
    """

    # Skip sending emails if disabled (local/dev)
    if not settings.EMAIL_ENABLED:
        print(
            f"[EMAIL DISABLED] To={to_email} | Subject={subject}"
        )
        return

    # Validate required email configuration
    if settings.EMAIL_HOST is None:
        raise RuntimeError("EMAIL_HOST is not configured")

    if settings.EMAIL_USERNAME is None:
        raise RuntimeError("EMAIL_USERNAME is not configured")

    if settings.EMAIL_PASSWORD is None:
        raise RuntimeError("EMAIL_PASSWORD is not configured")

    if settings.EMAIL_FROM is None:
        raise RuntimeError("EMAIL_FROM is not configured")

    # Build email message
    msg = MIMEMultipart()
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(html_body, "html"))


    # Send email via SMTP
    try:
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(
                settings.EMAIL_USERNAME,
                settings.EMAIL_PASSWORD
            )
            server.send_message(msg)

    except Exception as exc:
        raise RuntimeError(
            f"Failed to send email to {to_email}"
        ) from exc
