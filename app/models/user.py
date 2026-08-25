from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.book import Book


class UserBase(SQLModel):
    name: str
    email: str = Field(unique=True, index=True)


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    books: List["Book"] = Relationship(back_populates="owner")


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
