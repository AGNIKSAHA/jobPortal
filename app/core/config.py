import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    # Application settings
    APP_NAME: str = os.getenv("APP_NAME", "Job Board API")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Email / SMTP settings
    EMAIL_HOST: str | None = os.getenv("EMAIL_HOST")
    EMAIL_PORT: int = int(os.getenv("EMAIL_PORT", "587"))
    EMAIL_USERNAME: str | None = os.getenv("EMAIL_USERNAME")
    EMAIL_PASSWORD: str | None = os.getenv("EMAIL_PASSWORD")
    EMAIL_FROM: str | None = os.getenv("EMAIL_FROM")

    # Toggle email sending (useful for local dev)
    EMAIL_ENABLED: bool = os.getenv("EMAIL_ENABLED", "false").lower() == "true"


# Single shared settings instance
settings = Settings()

def validate_email_settings() -> None:
    if not settings.EMAIL_ENABLED:
        return

    missing = [
        name for name, value in {
            "EMAIL_HOST": settings.EMAIL_HOST,
            "EMAIL_USERNAME": settings.EMAIL_USERNAME,
            "EMAIL_PASSWORD": settings.EMAIL_PASSWORD,
            "EMAIL_FROM": settings.EMAIL_FROM,
        }.items()
        if value is None
    ]

    if missing:
        raise RuntimeError(
            f"Missing email configuration: {', '.join(missing)}"
        )

