from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud, models, schemas
from api import dependencies

router = APIRouter()


@router.get("/")
async def read_item(
        db: Session = Depends(dependencies.get_async_session),
        category_id: int = None,
        skip: int = 0,
        limit: int = 100

) -> Any:
    items = await crud.item.get_multi_by_owner(
        db=db, category_id=category_id, skip=skip, limit=limit
    )
    return items


@router.post("/create_item", response_model=schemas.Item)
async def create_item(
        *,
        db: Session = Depends(dependencies.get_async_session),
        item_in: schemas.ItemCreate,
        category_id: int,
) -> Any:
    """
    Create new item.
    """
    item = await crud.item.create_with_category(db=db, obj_in=item_in, category_id=category_id)
    return item


