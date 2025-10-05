from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import users as user_schema
from services import user_service
from data.database import get_db

router = APIRouter()

@router.post(
    "/", 
    response_model=user_schema.UserResponse,
    summary="Criar um novo usuário",
    description="Cria um novo usuário no sistema com os dados fonecidos."
)
async def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db=db, user=user)

@router.put(
    "/{user_id}",
    response_model=user_schema.UserResponse,
    summary="Atualuzar um usuário existente",
    description="Atualiza um usuário já existente no sistema com os dados fornecidos."
)
async def update_user(user_id: int, user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_service.update_user(db=db, user=user, user_id=user_id)

@router.get(
    "/", 
    response_model=List[user_schema.UserResponse],
    summary="Listar os usuários do sistema",
    description="Retorna uma lista de todos os usuários cadastrados no sistema."
)
async def list_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get(
    "/{user_id}", 
    response_model=user_schema.UserResponse,
    summary="Pesquisar um usuário pelo id",
    description="Retorna um usuário com o id igual ao fornecido."
)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id=user_id)

@router.get(
    "/by_role/{role}",
    response_model=List[user_schema.UserResponse],
    summary="Listar os usuários pelo tipo",
    description="Retorna uma lista de usuários a partir do tipo (Paciente, Médico ou Administrador)"
)
async def get_users_by_role(role: int, db: Session = Depends(get_db)):
    return user_service.get_users_by_role(db, role=role)

@router.get(
    "/patients/by_doctor/{doctor_id}",
    response_model=List[user_schema.UserResponse],
    summary="Listar os pacientes a partir do médico responsável",
    description="Retorna uma lista dos pacientes a partir do id do médico responsável"
)
async def get_patients_by_doctor(doctor_id: int, db: Session = Depends(get_db)):
    return user_service.get_patients_by_doctor(db, doctor_id=doctor_id)

@router.delete(
    "/{user_id}",
    summary="Excluir um usuário pelo id",
    description="Exclui um usuário no sistema a partir do id do mesmo."
)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(db, user_id=user_id)