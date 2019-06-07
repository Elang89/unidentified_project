from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=lambda: uuid4())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
