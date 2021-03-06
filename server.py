from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db, User
import crud
from jinja2 import StrictUndefined
import secrets
import os

app = Flask(__name__)


@app.route('/', defaults={'input_path': ''})  # if this matches the URL
@app.route('/<path:input_path>')  # or if this does
def show_homepage(input_path):
    """SHOW APPLICATION HOMEPAGE."""
    return render_template('index.html')

# * ======================================== DASHBOARD ROUTES ==================================================


@app.route('/api/get-profile-info', methods=["POST"])
def get_portfolio_info():
    '''GET ALL STOCKS'''

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    user_id = data['user_id']
    # ****************************** #

    risk = crud.get_profile_risk(user_id)
    industry_list = crud.get_user_industries(user_id)

    portfolio = {'PortfolioRisk': risk,
                 'Industries': industry_list}

    return jsonify(portfolio)


@app.route('/api/get-all-payouts', methods=["POST"])
def get_all_payouts():
    '''GET ALL STOCKS'''
    print('CALLING PAYOUTS &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    #  GET DATA
    # ****************************** #
    data = request.get_json()
    user_id = data['user_id']
    # ****************************** #
    payouts = crud.get_user_payouts(user_id)
    print('DONE &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', payouts)
    return jsonify(payouts)


# * ======================================== STOCK ROUTES ==================================================
@app.route('/api/get-all-stocks', methods=["GET"])
def get_all_stocks():
    '''GET ALL STOCKS'''

    #  GET DATA
    # ****************************** #
    # data = request.get_json()
    # user_id = data['user_id']
    # ****************************** #
    all_stocks = crud.get_all_stocks()
    stocks = []

    for s in all_stocks:
        # logic to swap schedule for a string saying how often
        interval = "Other"
        if s.payout_schedule == "0":
            interval = "None in 2020"
        elif s.payout_schedule == "1":
            interval = "Annually"
        elif s.payout_schedule == "2":
            interval = "Semi-annually"
        elif s.payout_schedule == "4":
            interval = "Quarterly"

        stocks.append({"symbol": s.symbol,
                       "dividend_amount": s.dividend_amount,
                       "dividend_yield": s.dividend_yield,
                       "payout_ratio": s.payout_ratio,
                       "payout_schedule": interval,
                       "stock_price": s.stock_price,
                       "company_name": s.company_name,
                       "sector": s.sector,
                       "id": s.stock_id
                       })

    return jsonify(stocks)


# * ======================================== USER STOCK ROUTES =============================================
@app.route('/api/get-user-stocks', methods=["POST"])
def get_user_stocks():
    '''GET USER STOCKS'''

    # ****************************** #
    data = request.get_json()
    user_id = data['user_id']
    # ****************************** #
    stock_count = {}
    user_stocks = crud.get_user_stocks(user_id)
    for stock in user_stocks:
        if stock.stock_id not in stock_count:
            stock_count[stock.stock_id] = 1
        else:
            stock_count[stock.stock_id] += 1
    return jsonify(stock_count)


@app.route('/api/add-user-stock', methods=["POST"])
def add_user_stock():
    '''TOGGLE MOVIE NOMINATION STATUS'''

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    user_id = data['user_id']
    stock_id = data['stock_id']
    # ****************************** #

    #  REMOVE NOMINATION
    stock_add = crud.add_user_stock(user_id, stock_id)
    return jsonify('stock added')


@app.route('/api/remove_user_stock', methods=["POST"])
def remove_user_stock():
    '''REMOVE STOCK FROM USER'''

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    user_id = data['user_id']
    stock_id = data['stock_id']
    # ****************************** #

    stock_remove = crud.remove_user_stock(user_id, stock_id)
    return jsonify('stock_removed')
# *============================================= USER ACCOUNT ROUTES =============================================


@app.route('/api/signup', methods=["POST"])
def sign_up():
    """ADD NEW USER TO DB AND GO TO HOMEPAGE"""

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    fname = data['fname']
    lname = data['lname']
    email = data['email']
    password = data['password']
    # ****************************** #

    existing_user = crud.does_user_exist(email)
    if existing_user == 'user exists':
        return jsonify('user exits')
    else:
        new_user = crud.create_user(fname, lname, email, password)
        return jsonify('account created')


@app.route('/api/login', methods=["POST"])
def login_user():
    '''VERIFY USER AND LOGIN'''

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    # print('THISI IS DATA #########################################################################################', data)
    email = data['email']
    password = data['password']
    # ****************************** #

    is_user = crud.validate_user(password, email)

    if is_user:
        user = crud.get_user_by_email(email)
        return jsonify({'fname': user['fname'], 'id': user['user_id']})

    else:
        # print('IS NOT USER')
        return jsonify('info does not match')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
