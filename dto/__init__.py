from pydantic import BaseModel
from humps import camelize


class CommonPydanticConfig:
    orm_mode = True
    alias_generator = camelize
    allow_population_by_field_name = True
    arbitrary_types_allowed = True


class BaseDto(BaseModel):
    class Config(CommonPydanticConfig):
        pass
