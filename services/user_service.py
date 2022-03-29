from datetime import datetime, timedelta
from typing import Optional, Union
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from pydantic.types import UUID

from database import Session
from database.models.session import Session as AuthSession
from database.models.user import User
from dto.user_dto import CreateUserDto, GetUserDto, GetUserToken


def create_user_service(db: Session, user_dto: CreateUserDto):
    repeat_user = db.query(User) \
        .filter(User.login == user_dto.login) \
        .first()

    if repeat_user != None:
        return None

    user = User()
    user.login = user_dto.login
    user.hashed_password = user_dto.password

    db.add(user)
    return user


def get_user_by_id(db: Session, user_id: UUID):
    find_user = db.query(User).filter(User.id == user_id).first()
    if find_user:
        get_user_dto = GetUserDto.from_orm(find_user)
        return get_user_dto
    else:
        return False


def delete_user_by_id(db: Session, user_id: UUID):
    find_user = db.query(User).filter(User.id == user_id).first()
    if find_user:
        db.delete(find_user)
        return True
    else:
        return False


def get_user_by_login(db: Session, login: str):
    found_user = db.query(User).filter(User.login == login.lower()).first()
    return found_user


class UserToken():
    session_id: UUID
    access_token: str
    refresh_token: UUID


class UserNotFound(Exception):
    pass


class WrongPassword(Exception):
    pass

