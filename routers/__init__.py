# Функиця выдающая сессию для
# подключения к базе данных

from database import Session


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
