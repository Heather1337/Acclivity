"""CRUD operations."""
from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import db, User, connect_to_db, UserStock, Stock
import datetime
import random
import logging


# ======================================== DASHBOARD ROUTES =============================================
def get_profile_risk(user_id):

    stock_tuples = get_user_stocks(user_id)

    payout_ratio = 0

    for stock in stock_tuples:
        payout_ratio += float(stock.payout_ratio)

    if payout_ratio < 35:
        return ('very low')
    if payout_ratio > 35 and payout_ratio < 55:
        return ('average')
    if payout_ratio > 55:
        return ('high')


def get_user_industries(user_id):

    sector_list = []
    stock_tuples = get_user_stocks(user_id)
    for stock in stock_tuples:
        stock_info = get_stock_info(stock.stock_id)
        if stock_info['sector'] not in sector_list:
            sector_list.append(stock_info['sector'])
    print(sector_list)
    return sector_list


def get_user_payouts(user_id):

    quarterlyPayout = 0
    monthlyPayout = 0
    otherPayout = 0
    AnnualPayout = 0
    spent = 0

    stock_tuples = get_user_stocks(user_id)
    for payout in stock_tuples:
        dividend_amount = float(payout.dividend_yield) * \
            float(payout.stock_price)
        if payout.payout_schedule == '12':
            monthlyPayout += dividend_amount
        elif payout.payout_schedule == '4':
            quarterlyPayout += dividend_amount
        elif payout.payout_schedule == '1':
            AnnualPayout += dividend_amount
        else:
            otherPayout += dividend_amount

        AnnualPayout += monthlyPayout * 12
        AnnualPayout += quarterlyPayout * 4

        spent += float(payout.stock_price)

    return [quarterlyPayout, monthlyPayout, otherPayout, AnnualPayout]


# ======================================== STOCK ROUTES =============================================
def get_all_stocks():
    '''GET SPECIFIC NOMINATION'''

    stocksquery = Stock.query.all()
    stocks = []
    if len(stocksquery):
        stocks = stocksquery

    return stocks


# ======================================== USER STOCK ROUTES =============================================

def get_stock_info(stock_id):

    stock = Stock.query.filter(Stock.stock_id == stock_id).first()

    stock_object = {
            'stock_id':stock.stock_id,
            'symbol':stock.symbol,
            'company_name':stock.company_name,
            'sector':stock.sector,
            'dividend_yield':stock.dividend_yield,
            'dividend_amount':stock.dividend_amount,
            'payout_schedule':stock. payout_schedule,
            'payout_ratio':stock.payout_ratio,
            'stock_price':stock.stock_price
    }

    return(stock_object)




def get_user_stocks(user_id):
    '''RETURN USER'S NOMINATIONS'''

    # stock_tuples = db.session.query(Stock).select_from(Stock).join(
    #     UserStock, Stock.stock_id == UserStock.stock_id).filter(UserStock.user_id == user_id).all()
    user_stocks = UserStock.query.filter(UserStock.user_id == user_id).all()

<<<<<<< HEAD
    for stock in stock_tuples:
        stock_object = {
            'stock_id': stock.stock_id,
            'dividend_yield': stock.dividend_yield,
            'dividend_amount': stock.dividend_amount,
            'payout_schedule': stock. payout_schedule,
            'payout_ratio': stock.payout_ratio,
            'stock_price': stock.stock_price
        }
        stock_object_list.append(stock_object)
    # print(stock_tuples)
    return (stock_object_list)
=======
    return (user_stocks)
>>>>>>> 9aa534ace4501e26b3edaa341fc15d50bb6796d1


def remove_user_stock(user_id, stock_id):
    '''REMOVE NOMINATION'''

    stock = UserStock.query.filter(
        UserStock.user_id == user_id, UserStock.stock_id == stock_id).first()

    db.session.delete(stock)
    db.session.commit()


def add_user_stock(user_id, stock_id):
    '''ADD NOMINATION'''

    now = datetime.datetime.now()
    new_user_stock = UserStock(user_id=user_id,
                               stock_id=stock_id,
                               date_added=now,
                               date_modified=now)
    db.session.add(new_user_stock)
    db.session.commit()

# ======================================== CREATE | LOGIN ROUTES =============================================


def get_user_by_email(email):
    '''RETURN USER BY EMAIL'''

    result = User.query.filter(User.email == email).first()
    user = {'email': result.email,
            'fname': result.fname,
            'lname': result.lname,
            'password': result.password,
            'user_id': result.user_id}
    print('GET USER BY EMAIL *****************************************************************************', user)
    return user


def does_user_exist(email):
    ''' CHECK IF USER EXISTS'''

    result = User.query.filter(User.email == email).first()

    if result is not None:
        return ('user exists')
    else:
        return('user does not exist')


def validate_user(password, email):
    """CHECK FOR VALID PASSWORD AT LOGIN"""

    user = User.query.filter(User.password == password,
                             User.email == email).first()
    print('Validate user *****************************************************************************', user)
    return user


def create_user(fname, lname, email, password):
    '''CREATE NEW USER'''

    now = datetime.datetime.now()
    new_user = User(fname=fname, lname=lname, email=email, password=password,
                    date_added=now, date_modified=now)

    db.session.add(new_user)
    db.session.commit()

    user = {'email': new_user.email,
            'fname': new_user.fname,
            'lname': new_user.lname,
            'password': new_user.password,
            'user_id': new_user.user_id}
    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
