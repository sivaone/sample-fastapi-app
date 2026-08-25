from fastapi import APIRouter
from app.api.v1.endpoints import books, users, library

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(library.router, prefix="/library", tags=["library"])
