from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.book import BookRead, BookCreate, BookUpdate
from app.services.book_service import BookService

router = APIRouter()


@router.post("/", response_model=BookRead)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    service = BookService(session)
    return service.create_book(book)


@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: int, session: Session = Depends(get_session)):
    service = BookService(session)
    return service.get_book(book_id)


@router.get("/", response_model=List[BookRead])
def read_books(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    service = BookService(session)
    return service.get_all_books(skip=skip, limit=limit)


@router.patch("/{book_id}", response_model=BookRead)
def update_book(
    book_id: int, book: BookUpdate, session: Session = Depends(get_session)
):
    service = BookService(session)
    return service.update_book(book_id, book)


@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    service = BookService(session)
    service.delete_book(book_id)
    return {"status": "success"}
