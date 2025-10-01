from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas import users_login as user_login_schema
from services import user_login_service
from data.database import get_db

router = APIRouter()

@router.get(
    "/",
    response_model=List[user_login_schema.UserLoginResponse],
    summary="Listar todos os logins de usuário",
    description="Lista todos os logins associados aos usuários do sistema."
)
async def list_users_login(db: Session = Depends(get_db)):
    return user_login_service.get_users_login(db)

@router.get(
    "/by_user/{user_id}",
    response_model=user_login_schema.UserLoginResponse,
    summary="Retorna o login do usuário pelo id",
    description="Retorna o login associado ao usuário do sistema pelo id"
)
async def get_auth_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_login_service.get_user_login_by_id(db, user_id)

@router.post(
    "/login",
    response_model=user_login_schema.UserLoginResponse,
    summary="Realizar o login de um usuário",
    description="Realiza o login de um usuário a partir do usuário e senha cadastrados."
)
async def login(login_request: user_login_schema.LoginRequest, db: Session = Depends(get_db)):
    return user_login_service.get_by_login_request(db, login_request=login_request)

@router.post(
    "/register",
    response_model=user_login_schema.UserLoginResponse,
    summary="Registrar um novo login",
    description="Registra um novo login para um usuário específico do sistema."
)
async def register(register_request: user_login_schema.RegisterRequest, db: Session = Depends(get_db)):
    return user_login_service.register(db, register_request=register_request)

@router.delete(
    "/{user_id}",
    summary="Excluir uma autenticação pelo id do usuário",
    description="Exclui uma autenticação no sistema a partir do id do usuário."
)
async def delete_auth(user_id: int, db: Session = Depends(get_db)):
    return user_login_service.delete(db, user_id)