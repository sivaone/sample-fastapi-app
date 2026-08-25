from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.core.exceptions import LibraryException
from app.core.exception_handlers import library_exception_handler
from app.api.v1.api import api_router

# Import models to ensure they are registered with SQLModel.metadata
from app.models.user import User
from app.models.book import Book


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    create_db_and_tables()
    yield


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.add_exception_handler(LibraryException, library_exception_handler)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the Local Library API"}
