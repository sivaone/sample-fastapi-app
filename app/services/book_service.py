from sqlmodel import Session

from app.core.exceptions import BookNotFoundError, DuplicateISBNError
from app.models.book import Book, BookCreate, BookUpdate
from app.repositories.book_repository import BookRepository


class BookService:
    def __init__(self, session: Session):
        self.repository = BookRepository(session)

    def create_book(self, book_in: BookCreate) -> Book:
        if self.repository.get_by_isbn(book_in.isbn):
            raise DuplicateISBNError(f"Book with ISBN {book_in.isbn} already exists")
        book = Book.model_validate(book_in)
        return self.repository.create(book)

    def get_book(self, book_id: int) -> Book:
        book = self.repository.get(book_id)
        if not book:
            raise BookNotFoundError(f"Book with id {book_id} not found")
        return book

    def get_all_books(self, skip: int = 0, limit: int = 100) -> list[Book]:
        return self.repository.get_multi(skip=skip, limit=limit)

    def update_book(self, book_id: int, book_in: BookUpdate) -> Book:
        book = self.get_book(book_id)
        update_data = book_in.model_dump(exclude_unset=True)
        return self.repository.update(book, update_data)

    def delete_book(self, book_id: int) -> bool:
        if not self.repository.delete(book_id):
            raise BookNotFoundError(f"Book with id {book_id} not found")
        return True
