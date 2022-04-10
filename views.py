from flask import render_template, Blueprint, abort, request
from models import Instrument, InstrumentPrices

bp = Blueprint('views', __name__, template_folder='templates')


@bp.get("/")
def root():

    """Return list of instruments"""

    instruments = Instrument.query.all()
    return render_template('index.html', instruments=instruments)


@bp.get("/<int:instrument_id>")
def detail(instrument_id: int):

    """Return detail page of the instrument"""

    instrument = Instrument.query.get(instrument_id)
    if not instrument:
        abort(404)

    return render_template('detail.html', instrument=instrument)


@bp.get("/prices/<int:instrument_id>")
def prices(instrument_id: int):

    """
    Return prices for the instrument

    you can set last_price_id get parameter and method
    return prices starts from last_price_id
    """

    instrument = Instrument.query.get(instrument_id)
    if not instrument:
        abort(404)

    last_price_id = request.args.get('last_price_id', 0)
    if type(last_price_id) != int and not last_price_id.isdigit():
        abort(404)

    prices_req = InstrumentPrices.query.filter(
        InstrumentPrices.instrument_id == instrument.id
    ).filter(InstrumentPrices.id > last_price_id).all()

    prices_result = []
    for price in prices_req:
        prices_result.append({
            'id': price.id,
            'date': price.date.isoformat(),
            'price': price.price
        })

    return {'prices': prices_result}


@bp.errorhandler(404)
def page_not_found(_):
    return render_template('404.html', title='404'), 404
