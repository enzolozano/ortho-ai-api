import sys

sys.dont_write_bytecode = True

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Callable
from loguru import logger
from data.database import engine, Base
from core.init_admin import create_default_admin

from exceptions.exceptions import (
    OrthoAiApiError,
    ResourceNotFoundError
)

from api.v1.router import base_router as router
from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION

app = FastAPI(
    title=PROJECT_NAME, 
    debug=DEBUG, 
    version=VERSION,
    description="API para gerenciamento de pacientes e médicos com leitura de Raio-X por inteligência artificial",
    contact={
        "name": "Equipe de TCC - Curso de Ciência da Computação",
        "email": "enzo.malozano@gmail.com"
    }
)
app.include_router(router, prefix=API_PREFIX)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    create_default_admin()

@app.get("/")
def read_root(): 
    return {"status": "ok"}

@app.get("/NotFound")
def not_found_test():
    raise ResourceNotFoundError(name="Teste", message="O handler funcionou :D")

def create_exception_handler(
    status_code: int, initial_detail: str
) -> Callable[[Request, OrthoAiApiError], JSONResponse]:
    detail = {"message": initial_detail}

    async def exception_handler(_: Request, exc: OrthoAiApiError) -> JSONResponse:
        if exc.message:
            detail["message"] = exc.message

        if exc.name:
            detail["message"] = f"{detail['message']} [{exc.name}]"

        logger.error(exc)
        return JSONResponse(
            status_code=status_code, content={"detail": detail["message"]}
        )

    return exception_handler

app.add_exception_handler(
    exc_class_or_status_code=ResourceNotFoundError,
    handler=create_exception_handler(
        status.HTTP_404_NOT_FOUND, "Resource does not exist."
    )
)