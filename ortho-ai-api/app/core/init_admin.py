from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import FastAPI
from data.database import engine, SessionLocal, Base
from models.users import User
from models.user_login import UserLogin
from core.security import hash_password
import json

app = FastAPI()

Base.metadata.create_all(bind=engine)

def create_default_admin():
    db: Session = SessionLocal()

    try:
        admin_user = db.query(User).filter(User.role == 2).first()

        if not admin_user:
            admin_user = User(
                name="Administrador do Sistema",
                email="admin@sistema.com",
                document="",
                phone="0000000000",
                photo_url="",
                role=2,
                birth_date=datetime(2000, 1, 1),
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)

        admin_login = db.query(UserLogin).filter(UserLogin.user_id == admin_user.id).first()

        if not admin_login:
            new_login = UserLogin(
                user_id=admin_user.id,
                username="admin",
                password=hash_password("admin"),
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.add(new_login)
            db.commit()
    finally:
        db.close()