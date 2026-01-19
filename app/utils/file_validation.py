from fastapi import UploadFile, HTTPException


ALLOWED_RESUME_TYPES = {
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

MAX_FILE_SIZE_MB = 5


def validate_resume_file(file: UploadFile) -> str:
    """
    Validates resume upload and returns a guaranteed `str` content type
    """

    if not file.content_type:
        raise HTTPException(
            status_code=400,
            detail="File type could not be determined"
        )

    if file.content_type not in ALLOWED_RESUME_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Invalid resume file type"
        )

    return file.content_type
