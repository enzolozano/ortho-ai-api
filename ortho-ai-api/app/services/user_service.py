from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.users import UserCreate
from repository import user_repository

def get_users(db: Session):
    return user_repository.list_users(db)

def get_user(db: Session, user_id: int):
    db_user = user_repository.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return db_user

def get_users_by_role(db: Session, role: int):
    return user_repository.get_users_by_role(db, role=role)

def create_user(db: Session, user: UserCreate):
    db_user = user_repository.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user_repository.create_user(db, user=user)

def delete_user(db: Session, user_id: int):
    db_user = user_repository.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    user_repository.delete_user(db, user_id=user_id)
    return {"message": "Usuário deletado com sucesso"}