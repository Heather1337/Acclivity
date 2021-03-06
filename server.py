from flask import (Flask, render_template, request, flash, session,
                   redirect,jsonify)
from model import connect_to_db, db, User
import crud
from jinja2 import StrictUndefined
import secrets
import os

app = Flask(__name__)


@app.route('/', defaults={'input_path': ''}) #if this matches the URL
@app.route('/<path:input_path>') #or if this does
def show_homepage(input_path):
    """SHOW APPLICATION HOMEPAGE."""
    return render_template('base.html')


# * ======================================== STOCK ROUTES ==================================================
@app.route('/api/get-all-stocks', methods=["POST"])
def get_all_stocks():
    '''GET ALL STOCKS'''

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    user_id = data['user_id']
    # ****************************** #

    all_stocks = crud.get_all_stocks(user_id)
    return jsonify(all_stocks)

    
# * ======================================== USER STOCK ROUTES =============================================
@app.route('/api/get-user-stocks', methods=["POST"])
def get_user_nominations():
    '''GET USER STOCKS'''

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    user_id = data['user_id']
    # ****************************** #

    user_stocks = crud.get_user_nominations(user_id)
    return jsonify(user_stocks)


@app.route('/api/set-user-stocks', methods=["POST"])
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


@app.route('/api/set_user_stock', methods=["POST"])
def remove_user_stock():
    '''REMOVE STOCK FROM USER'''

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    user_id = data['user_id']
    stock_id = data['stock_id']
    # ****************************** #

    #  REMOVE STOCK
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
        new_user = crud.create_user(fname,lname,email,password)
        return jsonify('account created')



@app.route('/api/login', methods=["POST"])
def login_user():
    '''VERIFY USER AND LOGIN'''

    #  GET DATA
    # ****************************** #
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = crud.get_user_by_email(email)
    # ****************************** #

    is_user = crud.validate_user(password,email)

    if is_user:
        return jsonify({'fname' : user['fname'], 'id':user['user_id'], 'submission_status':user['submission_status'] })

    else:
        return jsonify('info does not match')

if __name__ == '__main__':
    connect_to_db(app)
    app.run()
