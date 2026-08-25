from typing import Optional, TYPE_CHECKING
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.user import User


class BookStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    CHECKED_OUT = "CHECKED_OUT"


class BookBase(SQLModel):
    title: str = Field(index=True)
    author: str = Field(index=True)
    isbn: str = Field(unique=True, index=True)
    status: BookStatus = Field(default=BookStatus.AVAILABLE)
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")


class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    owner: Optional["User"] = Relationship(back_populates="books")


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int


class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    status: Optional[BookStatus] = None
    owner_id: Optional[int] = None
