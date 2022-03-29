from typing import Optional
from pydantic.fields import Field
from model_dotenv import EnvironModel


class Envs(EnvironModel):
    TITLE_APP: str
    DESCRIPTION_APP: Optional[str]
    HOST: str = Field(default='127.0.0.1')
    PORT: int = Field(default=8000)

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str


envs = Envs()



