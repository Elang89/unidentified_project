from main import db
from datetime import datetime
from uuid import uuid4
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = db.Column('id', UUID(as_uuid=True), primary_key=True,
                   default=lambda: uuid4())
    form_data = db.Column(JSON)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())
