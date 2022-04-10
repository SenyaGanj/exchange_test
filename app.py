from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_prefixed_env()
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from views import bp
app.register_blueprint(bp)


from models import Instrument, InstrumentPrices


@app.cli.command()
def generatedb():

    """Initialize instruments and prices."""

    new_instruments = []
    for i in range(0, 100):
        new_instruments.append(
            Instrument(
                name=f'Instrument {i + 1}'
            )
        )

    db.session.add_all(new_instruments)
    db.session.commit()

    new_prices = []
    for instrument in Instrument.query.all():
        new_prices.append(
            InstrumentPrices(
                instrument_id=instrument.id,
                price=0
            )
        )

    db.session.add_all(new_prices)
    db.session.commit()
