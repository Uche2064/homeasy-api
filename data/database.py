from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config.config import Settings

settings = Settings()

SQLALCHEMY_CONNEXION_STRING = f"""postgresql://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"""

engine = create_engine(SQLALCHEMY_CONNEXION_STRING)

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()