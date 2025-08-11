from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import exams as exam_schema
from services import exam_service
from data.database import get_db

router = APIRouter()

@router.post(
    "/",
    response_model=exam_schema.ExamResponse,
    summary="Criar um novo registro de exame",
    description="Adiciona ao banco um registro do exame de um paciente realizado por um médico."
)
async def create_exam(exam: exam_schema.ExamCreate, db: Session = Depends(get_db)):
    return exam_service.create_exam(db, exam=exam)

@router.get(
    "/",
    response_model=List[exam_schema.ExamResponse],
    summary="Listar todos os exames do sistema",
    description="Retorna uma lista de todos os exames cadastrados no sistema."
)
async def list_exams(db: Session = Depends(get_db)):
    return exam_service.get_exams(db)

@router.get(
    "/by_patient/{patient_id}",
    response_model=List[exam_schema.ExamResponse],
    summary="Listar todos os exames do sistema por paciente",
    description="Retorna uma lista de todos os exames cadastrados no sistema a partir do paciente."
)
async def get_exams_by_patient(patient_id: int, db: Session = Depends(get_db)):
    return exam_service.get_exams_by_patient(db, patient_id=patient_id)

@router.get(
    "/by_doctor/{doctor_id}",
    response_model=List[exam_schema.ExamResponse],
    summary="Listar todos os exames do sistema por médico",
    description="Retorna uma lista de todos os exames cadastrados no sistema a partir do médico."
)
async def get_exams_by_doctor(doctor_id: int, db: Session = Depends(get_db)):
    return exam_service.get_exams_by_doctor(db, doctor_id=doctor_id)

@router.get(
    "/with_photo",
    response_model=List[exam_schema.ExamResponse],
    summary="Listar todos os exames do sistema com foto",
    description="Retorna uma lista de todos os exames cadastrados no sistema que contenham foto do diagnóstico."
)
async def get_exams_with_photo(db: Session = Depends(get_db)):
    return exam_service.get_exams_with_photo(db)
