"""CRUD operations."""
from flask import Flask, render_template, request, flash, session, redirect ,jsonify
from model import db, User,connect_to_db, UserStock, Stock
import datetime
import random
import logging


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
