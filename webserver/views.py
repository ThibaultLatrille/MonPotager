from flask import render_template
from . import app

@app.route('/')
def home_page():
    print('Home')
    return 'Accueil /'
