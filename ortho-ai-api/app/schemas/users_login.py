from datetime import datetime
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    user_id: int
    username: str
    password: str

class UserLoginResponse(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime