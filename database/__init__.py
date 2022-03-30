from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from config import envs

engine = create_engine(
    f'postgresql+psycopg2://{envs.DB_USER}:{envs.DB_PASSWORD}@{envs.DB_HOST}/{envs.DB_NAME}', echo=False)

# if not database_exists(engine.url):
#     from sqlalchemy_utils import create_database
#
#     create_database(engine.url)

Base = declarative_base()

from database.models.user import User
from database.models.session import Session
from database.models.todo import Todo

Base.metadata.create_all(bind=engine)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
