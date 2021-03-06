"""CRUD operations."""
from flask import Flask, render_template, request, flash, session, redirect ,jsonify
from model import db, User,connect_to_db, UserStock, Stock
import datetime
import random
import logging


# ======================================== STOCK ROUTES =============================================

# ======================================== USER STOCK ROUTES =============================================

# ======================================== CREATE | LOGIN ROUTES =============================================


def get_user_by_email(email):
    '''RETURN USER BY EMAIL'''

    result = User.query.filter(User.email == email).first()
    user = {'email': result.email,
            'fname' : result.fname,
            'lname' : result.lname,
            'password' : result.password,
            'submission_status':result.submission_status,
            'user_id' : result.user_id}

    return user

def does_user_exist(email):
    ''' CHECK IF USER EXISTS'''

    result = User.query.filter(User.email == email).first()

    if result is not None:
        return ('user exists')
    else:
        return('user does not exist')


def validate_user(password,email):
    """CHECK FOR VALID PASSWORD AT LOGIN"""

    return User.query.filter(User.password == password, User.email == email).first()


def create_user(fname,lname,email,password):
    '''CREATE NEW USER'''

    now = datetime.datetime.now()
    new_user= User(fname=fname, lname=lname, email=email, password=password,submission_status='false',date_added=now, date_modified= now)

    db.session.add(new_user)
    db.session.commit()

    user = {'email': new_user.email,
            'fname' : new_user.fname,
            'lname' : new_user.lname,
            'password' : new_user.password,
            'submission_status':new_user.submission_status,
            'user_id' : new_user.user_id}
    return user



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
