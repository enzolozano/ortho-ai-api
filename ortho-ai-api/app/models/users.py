from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from data.database import Base

doctor_patient = Table(
    "doctor_patient",
    Base.metadata,
    Column("doctor_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("patient_id", Integer, ForeignKey("users.id", primary_key=True))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    document = Column(Text, unique=True, index=True, nullable=False)
    phone = Column(String)
    photo_url = Column(String)
    role = Column(Integer)
    birth_date = Column(Date)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    login = relationship(
        "UserLogin", 
        back_populates="user", 
        uselist=False)

    patients = relationship(
        "User", 
        secondary=doctor_patient, 
        primaryjoin=id == doctor_patient.c.doctor_id, 
        secondaryjoin=id == doctor_patient.c.patient_id,
        backref="doctors")