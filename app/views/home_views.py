from flask import Blueprint, render_template

home_views = Blueprint('home',__name__)

@home_views.route('/')
def home():
    return render_template('index.html')
@home_views.route('/')
def homeAd():
    return render_template('Administrador/index.html')