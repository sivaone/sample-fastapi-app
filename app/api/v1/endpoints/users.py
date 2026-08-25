from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.user import UserRead, UserCreate
from app.services.user_service import UserService

router = APIRouter()


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    service = UserService(session)
    return service.create_user(user)


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session)):
    service = UserService(session)
    return service.get_user(user_id)


@router.get("/", response_model=List[UserRead])
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    service = UserService(session)
    return service.get_all_users(skip=skip, limit=limit)


@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    service = UserService(session)
    service.delete_user(user_id)
    return {"status": "success"}
