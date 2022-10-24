from db import crud, init_database
from apscheduler.schedulers.background import BlockingScheduler

from app.config import Config
from app.utils import generate_ticks

sched = BlockingScheduler()
conf = Config()


def init_instruments():
    """drop database and fill it with initial data"""

    init_database()
    zero_prices = [conf.initial_price for _ in range(
        conf.instrument_count)]

    ticks = generate_ticks(0, zero_prices)
    crud.add_ticks(ticks)  # insert into database


def update_instruments():
    old_ticks = crud.get_last_ticks(conf.instrument_count)
    old_prices = [tick.price for tick in old_ticks]
    instrument_names = [tick.instrument_name for tick in old_ticks]
    start_index = old_ticks[-1].id + 1

    ticks = generate_ticks(start_index, old_prices, instrument_names)
    crud.add_ticks(ticks)  # insert into database


init_instruments()

sched.add_job(update_instruments, 'interval',
              seconds=conf.update_interval, max_instances=1)
sched.start()
