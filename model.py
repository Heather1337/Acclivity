from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# *****************************************************************************


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String,
                      nullable=False,
                      unique=False)
    lname = db.Column(db.String,
                      nullable=False,
                      unique=False)
    email = db.Column(db.String,
                      nullable=False,
                      unique=True)
    password = db.Column(db.String,
                         nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)
    date_modified = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return (f'<User user_id={self.user_id} fname ={self.fname} lname={self.lname} '
                f'email={self.email} password={self.password}'
                f' date_added={self.date_added} date_modified={self.date_modified}>')


class UserStock(db.Model):
    ''' User's stocks'''

    __tablename__ = 'userstocks'

    userstock_id = db.Column(db.Integer,
                             autoincrement=True,
                             primary_key=True)
    user_id = db.Column(db.Integer,
                        nullable=False,
                        unique=False)
    stock_id = db.Column(db.Integer,
                         nullable=False,
                         unique=False)
    date_added = db.Column(db.DateTime, nullable=False)
    date_modified = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return (f'<User userstock_id={self.userstock_id} user_id={self.user_id} stock_id={self.stock_id} '
                f' date_added={self.date_added} date_modified={self.date_modified}>')


class Stock(db.Model):
    """A Stock."""

    __tablename__ = 'stocks'

    stock_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    symbol = db.Column(db.String,
                       nullable=False,
                       unique=False)
    company_name = db.Column(db.String,
                       nullable=False,
                       unique=False)
    sector = db.Column(db.String,
                       nullable=True,
                       unique=False)
    dividend_yield = db.Column(db.String,
                               nullable=True,
                               unique=False)
    dividend_amount = db.Column(db.String,
                                nullable=True,
                                unique=False)
    payout_schedule = db.Column(db.String,
                                nullable=True)
    payout_ratio = db.Column(db.String,
                             nullable=True)
    stock_price = db.Column(db.String,
                            nullable=True)
    date_added = db.Column(db.DateTime, nullable=False)
    date_modified = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return (f'<Stock symbol={self.symbol} Company Name={self.company_name} dividend_amount={self.dividend_amount} dividend_yield={self.dividend_yield}  '
                f'payout_ratio={self.payout_ratio} payout_schedule={self.payout_schedule } stock_price={self.stock_price} '
                f'sector={self.sector} date_added={self.date_added} date_modified={self.date_modified}>')


def connect_to_db(flask_app, db_uri='postgresql:///acclivity', echo=True):
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
