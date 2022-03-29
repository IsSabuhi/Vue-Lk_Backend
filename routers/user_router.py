from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED

from database import Session
from dto.user_dto import GetUserDto, CreateUserDto
from routers import get_db
from services.user_service import (
    create_user_service,
    get_user_by_id as get_user_by_id_service,
    delete_user_by_id as delete_user_by_id_service,
    UserNotFound, WrongPassword,
)

user_router = APIRouter(tags=['user'])


@user_router.post(
    '/user',
    summary='Добавить пользователя',
    responses={
        409: {
            "description": "Пользователь с таким логином уже существует",
        },
    },
    response_model=GetUserDto,
    operation_id='createUser',
    status_code=201
)
def create_user(create_user_dro: CreateUserDto, db: Session = Depends(get_db)):
    new_user = create_user_service(db=db, user_dto=create_user_dro)
    if new_user is None:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail='Пользователь с таким логином уже существует')
    db.commit()
    get_user_dto = GetUserDto.from_orm(new_user)

    return get_user_dto


@user_router.get(
    "/user/{id}",
    summary="Получить пользователя по ID",
    responses={
        404: {
            "description": "Пользователь не может быть найден, так как отсутсвует в базе данных.",
        }
    },
    response_model=GetUserDto,
    operation_id="getUserById"
)
def get_user_by_id(id: UUID, db: Session = Depends(get_db)):
    user = get_user_by_id_service(db, id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="Не удалось найти пользователя с данным ID")


@user_router.delete(
    "/user",
    summary="Удаление пользователя по ID",
    responses={
        404: {
            "description": "Пользователь не может быть удален, так как отсутсвует в базе данных.",
        },
    },
    operation_id="deleteUserById"
)
def delete_user_by_id(user_id: UUID, db: Session = Depends(get_db)):
    if delete_user_by_id_service(db, user_id):
        db.commit()
        return "Пользователь успешно удален"
    else:
        raise HTTPException(status_code=404, detail="Не удалось найти пользователя с данным ID")
