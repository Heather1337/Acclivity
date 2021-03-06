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

# * ======================================== USER STOCK ROUTES =============================================

# *============================================= USER ACCOUNT ROUTES =============================================


if __name__ == '__main__':
    connect_to_db(app)
    app.run()
