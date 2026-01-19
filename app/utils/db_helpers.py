from fastapi import HTTPException, status
from sqlmodel import Session
from typing import Type, TypeVar

T = TypeVar("T")

def get_or_404(
    session: Session,
    model: Type[T],
    obj_id: int,
    resource_name: str
) -> T:
    """
    Fetch a database object by ID or raise HTTP 404.
    """
    obj = session.get(model, obj_id)

    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource_name} with id {obj_id} not found"
        )

    return obj
