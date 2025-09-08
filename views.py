from flask import render_template, request, redirect, url_for, flash
from models import db, todo # Also import your database model here

def init_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')