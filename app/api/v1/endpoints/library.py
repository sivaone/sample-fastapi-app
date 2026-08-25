from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.book import BookRead
from app.services.library_service import LibraryService

router = APIRouter()


@router.post("/reserve/{book_id}/user/{user_id}", response_model=BookRead)
def reserve_book(book_id: int, user_id: int, session: Session = Depends(get_session)):
    service = LibraryService(session)
    return service.reserve_book(book_id, user_id)


@router.post("/checkout/{book_id}/user/{user_id}", response_model=BookRead)
def checkout_book(book_id: int, user_id: int, session: Session = Depends(get_session)):
    service = LibraryService(session)
    return service.checkout_book(book_id, user_id)


@router.post("/return/{book_id}", response_model=BookRead)
def return_book(book_id: int, session: Session = Depends(get_session)):
    service = LibraryService(session)
    return service.return_book(book_id)
