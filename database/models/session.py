import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class Session(Base):
    __tablename__ = 'session'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    refresh_token = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    fingerprint = Column(String(255))

    user = relationship("User", foreign_keys=[user_id])
