from .database import Base
from sqlalchemy import Column, String, Integer

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, unique=True, nullable=False)
    short_code = Column(String, unique=True, index=True, nullable=False)
    visit_count = Column(Integer, default=0)
