from fastapi import APIRouter
from .endpoints import auth, users
base_router = APIRouter()

base_router.include_router(auth.router, tags=["auth"], prefix="/v1")
base_router.include_router(users.router, tags=["users"], prefix="/v1")