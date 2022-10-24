from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Tick(Base):
    __tablename__ = 'tick'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    instrument_name = Column(String(9))
    updated_at = Column(DateTime(timezone=True))
