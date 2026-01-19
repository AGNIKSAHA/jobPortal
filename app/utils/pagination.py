from typing import TypeVar, Optional
from sqlmodel.sql.expression  import SelectOfScalar


T = TypeVar("T")

def apply_pagination(
    statement: SelectOfScalar[T],
    *,
    page: int,
    limit: int,
    cursor: Optional[int] = None,
) -> SelectOfScalar[T]:
    """
    Apply offset or cursor pagination to a SQLModel select query.
    """
    if cursor is None:
        offset = (page - 1) * limit
        statement = statement.offset(offset)

    return statement.limit(limit)

