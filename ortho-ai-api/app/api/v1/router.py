from fastapi import APIRouter
from .endpoints.auth import router
base_router = APIRouter()

base_router.include_router(router, tags=["auth"], prefix="/v1")