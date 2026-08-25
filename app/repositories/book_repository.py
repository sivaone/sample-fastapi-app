from typing import List, Optional
from sqlmodel import Session, select
from app.models.book import Book, BookStatus
from app.repositories.base_repository import BaseRepository


class BookRepository(BaseRepository[Book]):
    def __init__(self, session: Session):
        super().__init__(Book, session)

    def get_by_isbn(self, isbn: str) -> Optional[Book]:
        statement = select(Book).where(Book.isbn == isbn)
        return self.session.exec(statement).first()

    def get_available(self) -> List[Book]:
        statement = select(Book).where(Book.status == BookStatus.AVAILABLE)
        return self.session.exec(statement).all()
