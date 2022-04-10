import time
from datetime import datetime
from random import random

from sqlalchemy import func

from app import db
from models import InstrumentPrices


def generate_movement() -> int:
    movement = -1 if random() < 0.5 else 1
    return movement


def update_prises() -> None:

    """Update prices for all instruments every second"""

    max_date = db.session.query(func.max(InstrumentPrices.date).label('max_date')).first()
    instrument_prices = InstrumentPrices.query.filter(InstrumentPrices.date == max_date['max_date']).all()

    current_date = datetime.now()
    new_instrument_prices = []
    for instrument_price in instrument_prices:
        new_instrument_prices.append(
            InstrumentPrices(
                instrument_id=instrument_price.instrument_id,
                date=current_date,
                price=instrument_price.price + generate_movement(),
            )
        )

    db.session.add_all(new_instrument_prices)
    db.session.commit()


if __name__ == '__main__':
    start_time = time.time()
    while True:
        update_prises()
        time.sleep(1 - ((time.time() - start_time) % 1))
