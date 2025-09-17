from pydantic import BaseModel
from datetime import date, datetime

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    photo_url: str
    role: int
    birth_date: date

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    photo_url: str
    role: int
    birth_date: date
    created_at: datetime