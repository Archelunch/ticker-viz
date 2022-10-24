from typing import List

from db import get_session, get_conn
from db.models import Tick


def get_ticks(instrument_name: str, from_date, to_date) -> List[Tick]:
    with get_session() as session:
        ticks = session.query(Tick).filter(Tick.updated_at.between(
            from_date, to_date)).filter_by(instrument_name=instrument_name)
        return ticks


def get_last_ticks_by_name(instrument_name: str, count: int) -> List[Tick]:
    with get_session() as session:
        ticks = session.query(Tick).filter_by(
            instrument_name=instrument_name).order_by(Tick.id.desc()).limit(count)
        return ticks[::-1]


def get_last_ticks(count: int) -> List[Tick]:
    with get_session() as session:
        ticks = session.query(Tick).order_by(Tick.id.desc()).limit(count)
        return ticks[::-1]


def add_ticks(ticks: List):
    with get_conn() as conn:
        insert_obj = Tick.__table__.insert()
        conn.execute(
            insert_obj,
            ticks,
        )
