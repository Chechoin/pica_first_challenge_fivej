from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.errors import ServerErrorMiddleware

from app.config.logger import logger
from app.utils.exception_handler import custom_exception_handler

from . import models
from .config.database import engine
from .routers import auth, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Añadir el middleware de manejo de errores
app.add_middleware(ServerErrorMiddleware, handler=custom_exception_handler)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up the application")
    yield
    logger.info("Shutting down the application")


app.include_router(user.router)
app.include_router(auth.router)
