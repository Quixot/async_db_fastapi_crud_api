from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa


class Category(Base):
    id = Column(Integer, index=True, primary_key=True, unique=True)
    title = Column(String(128))

    item = relationship("Item", back_populates="category")
