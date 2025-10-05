from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class UserCreate(BaseModel):
    name: str
    email: str
    document: object
    phone: str
    responsible_doctor: Optional[int] = None
    photo_url: str
    role: int
    birth_date: date

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    document: object
    phone: str
    photo_url: str
    role: int
    birth_date: date
    created_at: datetime