from datetime import datetime
import pytz
from random import random

from app.config import Config

conf = Config()


def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement


def generate_tick(id: int, instrument_name: str, updated_at=None, old_price=0) -> dict:
    """single tick generation"""

    if updated_at == None:
        updated_at = datetime.now(pytz.timezone(conf.timezone))

    tick = {'id': id, 'price': old_price+generate_movement(),
            'instrument_name': instrument_name, 'updated_at': updated_at}
    return tick


def generate_ticks(start_index=0, old_prices=[], instrument_names=[]) -> list:
    """tick's generation for every instrument"""

    dt = datetime.now(pytz.timezone(conf.timezone))
    instrument_count = len(old_prices)

    if instrument_names == []:
        instrument_names = [
            f"ticker_0{i}" if i < 10 else f"ticker_{i}" for i in range(instrument_count)]

    ticks = [generate_tick(start_index+i, instrument_names[i], dt, old_prices[i])
             for i in range(instrument_count)]
    return ticks
