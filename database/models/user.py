from enum import Enum as En
import uuid

from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    login = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)

    def __repr__(self):
        return f'Login: {self.login} \t ID: {self.id}'
