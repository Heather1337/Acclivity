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
        payout_ratio += stock.payout_ratio

    if payout_ratio < 35:
        return ('very low')
    if payout_ratio > 35 and payout_ratio < 55:
        return ('average')
    if payout_ratio > 55:
        return ('high')


def get_user_industries(user_id):

    stock_tuples = get_user_stocks(user_id)

    print('obv not done')


def get_user_payouts(user_id):

    quarterlyPayout = 0
    monthlyPayout = 0
    otherPayout = 0
    AnnualPayout = 0
    spent = 0

    stock_tuples = get_user_stocks(user_id)
    for payout in stock_tuples:
        dividend_amount = payout.dividend_yield * payout.stock_price
        if payout.schedule == 'monthly':
            monthlyPayout += dividend_amount
        if payout.schedule == 'quarterly':
            quarterlyPayout += dividend_amount
        if payout.schedule == 'annually':
            AnnualPayout += dividend_amount
        if payout.schedule == 'other':
            otherPayout += dividend_amount

        AnnualPayout += monthlyPayout * 12
        AnnualPayout += quarterlyPayout * 4

        spent += payout.stock_price

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

def get_user_stocks(user_id):
    '''RETURN USER'S NOMINATIONS'''

    stock_tuples = db.session.query(Stock).select_from(Stock).join(
        UserStock, Stock.stock_id == UserStock.stock_id).filter(UserStock.user_id == user_id).all()

    return stock_tuples


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
