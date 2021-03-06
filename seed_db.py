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


stock_data = 'data/Acclivity.csv'


# ************************************************************************************
new_user = User(fname='User',
                lname='user',
                email='user@gmail.com',
                password='user')
db.session.add(new_user)
db.session.commit()

stocks = {}

with open(stock_data, 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        symbol = row['Ticker Symbol'].strip()
        if symbol not in stocks:
            stocks[symbol] = {
                "symbol": symbol,
                "dividend_amount": row["Dividend Amount"].strip(),
                "payout_schedule": row["Payout Schedule"].strip(),
                "stock_price": row["Stock Price"].strip()
            }

with open('data/symbols.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        symbol = row['Ticker'].strip()
        if symbol in stocks:
            stocks[symbol]["company_name"] = row["Company Name"]
            stocks[symbol]["sector"] = row["Sector"]
            stocks[symbol]["payout_ratio"] = row["Dividend Payout Ratio"].strip()
            stocks[symbol]["dividend_yield"] = row["Dividend Yield"].strip()


for stock in stocks:
    print('stock', stocks[stock])
    ticker = Stock(symbol=stocks[stock]['symbol'], sector=stocks[stock]['sector'], company_name=stocks[stock]['company_name'], dividend_amount=stocks[stock]['dividend_amount'],
                   dividend_yield=stocks[stock]['dividend_yield'], payout_schedule=stocks[
        stock]['payout_schedule'], payout_ratio=stocks[stock]['payout_ratio'],
        stock_price=stocks[stock]['stock_price'])

    db.session.add(ticker)
    db.session.commit()


# ***************************************************************************
