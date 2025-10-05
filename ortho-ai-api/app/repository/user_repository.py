from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserCreate
from datetime import datetime
import json


def list_users(db: Session):
    return db.query(User).order_by(User.id)

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users_by_role(db: Session, role: int):
    return db.query(User).filter(User.role == role).order_by(User.id)

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, document=json.dumps(user.document), phone=user.phone, photo_url=user.photo_url, role=user.role, birth_date=user.birth_date, created_at=datetime.now(),updated_at=datetime.now())

    if user.responsible_doctor:
        doctor = get_user(db, user_id=user.responsible_doctor)

        if not doctor:
            raise ValueError("Médico informado não encontrado.")
        
        if doctor.role != 1:
            raise ValueError("Usuário informado não é um médico.")
        
        doctor.patients.append(db_user)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: User):
    db.merge(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return None
    db.delete(user)
    db.commit()
