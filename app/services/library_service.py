from sqlmodel import Session
from app.models.book import Book, BookStatus
from app.repositories.book_repository import BookRepository
from app.repositories.user_repository import UserRepository
from app.core.exceptions import (
    BookNotFoundError,
    UserNotFoundError,
    BookNotAvailableError,
    BookAlreadyCheckedOutError,
)


class LibraryService:
    def __init__(self, session: Session):
        self.book_repo = BookRepository(session)
        self.user_repo = UserRepository(session)

    def reserve_book(self, book_id: int, user_id: int) -> Book:
        book = self.book_repo.get(book_id)
        if not book:
            raise BookNotFoundError(f"Book {book_id} not found")

        user = self.user_repo.get(user_id)
        if not user:
            raise UserNotFoundError(f"User {user_id} not found")

        if book.status != BookStatus.AVAILABLE:
            raise BookNotAvailableError(
                f"Book {book_id} is not available for reservation"
            )

        return self.book_repo.update(
            book, {"status": BookStatus.RESERVED, "owner_id": user_id}
        )

    def checkout_book(self, book_id: int, user_id: int) -> Book:
        book = self.book_repo.get(book_id)
        if not book:
            raise BookNotFoundError(f"Book {book_id} not found")

        user = self.user_repo.get(user_id)
        if not user:
            raise UserNotFoundError(f"User {user_id} not found")

        if book.status == BookStatus.CHECKED_OUT:
            raise BookAlreadyCheckedOutError(f"Book {book_id} is already checked out")

        # Can checkout if AVAILABLE or RESERVED to this user
        if book.status == BookStatus.RESERVED and book.owner_id != user_id:
            raise BookNotAvailableError(f"Book {book_id} is reserved by another user")

        return self.book_repo.update(
            book, {"status": BookStatus.CHECKED_OUT, "owner_id": user_id}
        )

    def return_book(self, book_id: int) -> Book:
        book = self.book_repo.get(book_id)
        if not book:
            raise BookNotFoundError(f"Book {book_id} not found")

        return self.book_repo.update(
            book, {"status": BookStatus.AVAILABLE, "owner_id": None}
        )
