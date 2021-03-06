"""Script to seed database."""

import os
# This is a module from Python’s standard library. It contains
# code related to working with your computer’s operating system.
import json
from random import choice, randint
from datetime import datetime
import csv

# import crud
from model import db, connect_to_db, User, UserStock, Stock
import server

os.system('dropdb acclivity')

os.system('createdb acclivity')

# After that, you connect to the database and call db.create_all:
connect_to_db(server.app)
db.create_all()



stock_data = 'data/acclivity.csv'


# ************************************************************************************
with open(stock_data, 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        stock = Stock(  symbol = row['Ticker Symbol'].strip(),
                        # sector = row['Sector'].strip(), Might need to add another seed function for this if we need to use both csv's
                        dividend_amount = row['Dividend Amount'].strip(),
                        dividend_yield  = row['Dividend Yield'].strip(),
                        payout_schedule = row['Payout Schedule'].strip(),
                        payout_ratio = row['Payout Ratio'].strip(),
                        date_added = '11-04-2020',
                        date_modified = '11-04-2020')

        db.session.add(stock)
        db.session.commit()

    new_user = User(fname = 'User',
                    lname ='user',
                    email = 'user@gmail.com',
                    password = 'user',
                    profile_img = 'https://www.pakstockexchange.com/stock3/profile_pictures/no-profile-picture.png',
                    date_added = '2020-11-21',
                    date_modified = '2020-11-21')
    db.session.add(new_user)
    db.session.commit()

    new_userstock = UserStock(user_id = 'user_id',
                    stock_id ='stock_id',
                    date_added = '2020-11-21',
                    date_modified = '2020-11-21')
    db.session.add(new_userstock)
    db.session.commit()

# ***************************************************************************
