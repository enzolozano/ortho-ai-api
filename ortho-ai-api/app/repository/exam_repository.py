from sqlalchemy.orm import Session
from models.exams import Exam
from schemas.exams import ExamCreate
from datetime import datetime

def list_exams(db: Session):
    return db.query(Exam).order_by(Exam.id)

def get_exams_by_patient(db: Session, patient_id: int):
    return db.query(Exam).filter(Exam.patient_id == patient_id).order_by(Exam.id)

def get_exams_by_doctor(db: Session, doctor_id: int):
    return db.query(Exam).filter(Exam.doctor_id == doctor_id).order_by(Exam.id)

def get_exams_with_photo(db: Session):
    return db.query(Exam).filter(Exam.diagnosis_photo_url != "").order_by(Exam.id)

def create_exam(db: Session, exam: ExamCreate):
    db_exam = Exam(
        patient_id=exam.patient_id,
        doctor_id=exam.doctor_id,
        diagnosis=exam.diagnosis,
        diagnosis_photo_url=exam.diagnosis_photo_url,
        created_at = datetime.now(),
        updated_at = datetime.now()
    )
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam