import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Instrument(db.Model):
    __tablename__ = 'instruments'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    prices = relationship("InstrumentPrices", backref="instrument")


class InstrumentPrices(db.Model):
    __tablename__ = 'instrument_prices'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    instrument_id = db.Column(db.Integer, ForeignKey('instruments.id', ondelete='CASCADE'), nullable=False, index=True)
    date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now())
    price = db.Column(db.Integer, nullable=False)
