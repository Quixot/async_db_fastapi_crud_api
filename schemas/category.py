from typing import Optional

from pydantic import BaseModel


# Shared properties
class CategoryBase(BaseModel):
    title: Optional[str] = None


# Properties to receive on item creation
class CategoryCreate(CategoryBase):
    title: str


# Properties to receive on item update
class CategoryUpdate(CategoryBase):
    pass


# Properties shared by models stored in DB
class CategoryInDBBase(CategoryBase):
    id: int
    title: str

    class Config:
        orm_mode = True


# Properties to return to client
class Category(CategoryInDBBase):
    pass


# Properties properties stored in DB
class CategoryInDB(CategoryInDBBase):
    pass
