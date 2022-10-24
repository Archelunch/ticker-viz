import contextlib
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from .models import Base


DATABASE_URI = f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTG_H']}:{os.environ['POSTG_P']}/{os.environ['POSTGRES_DB']}"


@contextlib.contextmanager
def get_session():
    engine = create_engine(DATABASE_URI)
    session = Session(bind=engine)
    try:
        yield session
    except Exception:
        session.rollback()
    finally:
        session.close()


@contextlib.contextmanager
def get_conn():
    """for optimized query execution"""

    engine = create_engine(DATABASE_URI)
    conn = engine.connect()
    yield conn
    conn.close()


def init_database():
    engine = create_engine(DATABASE_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
