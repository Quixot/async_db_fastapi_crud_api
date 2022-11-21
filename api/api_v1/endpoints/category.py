from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud, models, schemas
from api import dependencies

router = APIRouter()


@router.post("/create_category")
async def create_category(
        *,
        db: Session = Depends(dependencies.get_async_session),
        item_in: schemas.CategoryCreate,
) -> Any:
    """
    Create new category.
    """
    category = await crud.category.create_category(db=db, obj_in=item_in)
    return category
