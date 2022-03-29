from pydantic import Field
from pydantic.types import UUID, constr

from dto import BaseDto


class BaseUserDto(BaseDto):
    login: constr(max_length=35, to_lower=True) = Field(
        description='Логин пользователя', example='Ivan')


class CreateUserDto(BaseUserDto):
    password: constr(min_length=8, max_length=35) = Field(
        description='Пароль пользователя', example='qwerty123')


class GetUserDto(BaseUserDto):
    id: UUID = Field(description='Идентификатор пользователя', example='1')


class GetUserToken(BaseDto):
    session_id: UUID = Field(description='Идентификатор сессии')
    refresh_token: UUID = Field(description='Токен для получения нового')
    access_token: str = Field(description='Токен доступа')
