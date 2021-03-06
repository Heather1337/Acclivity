from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()



class Stock(db.Model):
    """A user."""

    __tablename__ = 'users'

    stock_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    symbol = db.Column(db.String,
                        nullable=False,
                        unique=False)
    sector = db.Column(db.String,
                        nullable=False,
                        unique=False)
    dividend_yield = db.Column(db.String,
                        nullable=False,
                        unique=False)
    dividend_amount = db.Column(db.String,
                        nullable=False,
                        unique=False)
    payout_schedule= db.Column(db.String,
                        nullable=False)
    payout_ratio= db.Column(db.String,
                        nullable=False)
    stock_price = db.Column(db.String,
                        nullable=False)
    date_added = db.Column(db.DateTime,nullable=False)
    date_modified = db.Column(db.DateTime,nullable=False)


    def __repr__(self):
        return (f'<Stock symbol={self.symbol} dividend_amount={self.dividend_amount} dividend_yield={self.dividend_yield}  '
                f'payout_ratio={self.payout_ratio} payout_schedule={self.payout_schedule } stock_price={self.stock_price} '
                f'sector={self.sector} date_added={self.date_added} date_modified={self.date_modified}>')



def connect_to_db(flask_app, db_uri='postgresql:///shoppies', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

# *****************************************************************************


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    print("Connected to DB.")