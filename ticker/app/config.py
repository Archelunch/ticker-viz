from dataclasses import dataclass


@dataclass
class Config:
    instrument_count: int = 100
    initial_price: int = 0
    update_interval: int = 1  # in seconds
    timezone: str = 'Europe/Moscow'
