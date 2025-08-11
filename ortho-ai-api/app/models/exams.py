from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from data.database import Base

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("users.id"), unique=True, index=True, nullable=False)
    doctor_id = Column(Integer, ForeignKey("users.id"), unique=True, index=True, nullable=False)
    diagnosis = Column(String, unique=True, nullable=False)
    diagnosis_photo_url = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)