from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class UserCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    photo_url: Optional[str] = None
    role: int
    birth_date: Optional[date] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    photo_url: str
    role: int
    birth_date: date
    created_at: datetime