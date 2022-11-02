from sqlalchemy import Column, Integer, Float, Boolean, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from datetime import datetime

from db.base_class import Base


class Category(Base):
    id = Column(Integer, index=True, primary_key=True, unique=True)
    title = Column(String(128))

    item = relationship("Item", back_populates="category")


class Item(Base):
    id = Column(Integer, index=True, primary_key=True, unique=True)
    title = Column(String(128))
    description = Column(Text)
    status = Column(Boolean)
    price = Column(Float)
    created = Column(DateTime, server_default=func.now())
    updated = Column(DateTime, onupdate=func.now())

    category_id = Column(ForeignKey("category.id", ondelete="CASCADE"))
    category = relationship("Category", back_populates="item")
