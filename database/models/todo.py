from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from database import Base
import uuid


class Todo(Base):
    __tablename__ = "todo"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(30), nullable=False)
    text = Column(String(255), nullable=True)

    def __repr__(self):
        return f'Title: {self.title} \t ID: {self.id}'