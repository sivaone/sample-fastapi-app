from typing import List
from sqlmodel import Session
from app.models.user import User, UserCreate
from app.repositories.user_repository import UserRepository
from app.core.exceptions import UserNotFoundError, DuplicateEmailError


class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def create_user(self, user_in: UserCreate) -> User:
        if self.repository.get_by_email(user_in.email):
            raise DuplicateEmailError(f"User with email {user_in.email} already exists")
        user = User.model_validate(user_in)
        return self.repository.create(user)

    def get_user(self, user_id: int) -> User:
        user = self.repository.get(user_id)
        if not user:
            raise UserNotFoundError(f"User with id {user_id} not found")
        return user

    def get_all_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.repository.get_multi(skip=skip, limit=limit)

    def delete_user(self, user_id: int) -> bool:
        if not self.repository.delete(user_id):
            raise UserNotFoundError(f"User with id {user_id} not found")
        return True
