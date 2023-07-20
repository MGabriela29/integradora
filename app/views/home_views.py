from flask import render_template, redirect, url_for, Blueprint

home_views = Blueprint('home', __name__)
ayudante_views = Blueprint('ayudante', __name__)

@home_views.route('/')
def index():
    return render_template('index.html')

@home_views.route('/administrador')
def administrador():
    return render_template('Administrador/index.html')

@ayudante_views.route('/ayudante')
def ayudante():
    return render_template('Ayudante/index.html')