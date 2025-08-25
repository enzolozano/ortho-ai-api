from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repository import user_login_repository
from schemas.users_login import LoginRequest, RegisterRequest

def get_users_login(db: Session):
    return user_login_repository.list_users_login(db)

def get_by_login_request(db: Session, login_request: LoginRequest):
    db_user_login = user_login_repository.get_by_login_request(db, login_request=login_request)
    if db_user_login is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return db_user_login

def register(db: Session, register_request: RegisterRequest):
    return user_login_repository.register(db, register_request=register_request)
