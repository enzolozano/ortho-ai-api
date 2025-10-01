from sqlalchemy.orm import Session
from models.user_login import UserLogin
from schemas.users_login import LoginRequest, RegisterRequest
from datetime import datetime
from core.security import hash_password, verify_password

def list_users_login(db: Session):
    return db.query(UserLogin).order_by(UserLogin.id)

def get_by_login_request(db: Session, login_request: LoginRequest):
    user = db.query(UserLogin).filter(
        UserLogin.username == login_request.username
    ).first()

    if user and verify_password(login_request.password, user.password):
        return user
    else:
        return None
    
def get_by_user_id(db: Session, user_id: int):
    auth = db.query(UserLogin).filter(
        UserLogin.user_id == user_id
    ).first()

    if auth:
        return auth
    else:
        return None

def register(db: Session, register_request: RegisterRequest):
    db_user_login = UserLogin(
        user_id = register_request.user_id,
        username = register_request.username,
        password = hash_password(register_request.password),
        created_at = datetime.now(),
        updated_at = datetime.now()
    )
    db.add(db_user_login)
    db.commit()
    db.refresh(db_user_login)
    return db_user_login

def delete_user_login(db: Session, user_id: int):
    db_user_login = db.query(UserLogin).filter(UserLogin.user_id == user_id).first()
    if db_user_login is None:
        return None
    db.delete(db_user_login)
    db.commit()