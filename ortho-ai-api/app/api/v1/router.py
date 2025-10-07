from fastapi import APIRouter
from .endpoints import auth, users
base_router = APIRouter()

base_router.include_router(auth.router, tags=["Authentication"], prefix="/v1/auth")
base_router.include_router(users.router, tags=["Users"], prefix="/v1/users")