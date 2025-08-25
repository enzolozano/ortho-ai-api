from sqlalchemy.orm import Session
from schemas.exams import ExamCreate
from repository import exam_repository

def get_exams(db: Session):
    return exam_repository.list_exams(db)

def get_exams_by_patient(db: Session, patient_id: int):
    return exam_repository.get_exams_by_patient(db, patient_id=patient_id)

def get_exams_by_doctor(db: Session, doctor_id: int):
    return exam_repository.get_exams_by_doctor(db, doctor_id=doctor_id)

def get_exams_with_photo(db: Session):
    return exam_repository.get_exams_with_photo(db)

def create_exam(db: Session, exam: ExamCreate):
    return exam_repository.create_exam(db, exam=exam)