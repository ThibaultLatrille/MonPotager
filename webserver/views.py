from flask import render_template
from . import app, cache

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/plant/<int:id>-<string:name>.html')
@app.route('/plante/<int:id>-<string:name>.html')
@cache.cached(timeout=86400)
def plant(id, name):
    print("Plante")
    return render_template('plant.html')

@app.route('/disease/<int:id>-<string:name>.html')
@app.route('/maladie/<int:id>-<string:name>.html')
@cache.cached(timeout=86400)
def maladie(id, name):
    print("Maladie")
    return("Maladie")
    #return render_template('desease.html')

@app.route('/nuisible/<int:id>-<string:name>.html')
@app.route('/pest/<int:id>-<string:name>.html')
@cache.cached(timeout=86400)
def pest(id, name):
    print("Nuisible")
    return("nuisible")
    #return render_template('pest.html')

@app.route('/auxiliaire/<int:id>-<string:name>.html')
@app.route('/helper/<int:id>-<string:name>.html')
@cache.cached(timeout=86400)
def helper(id, name):
    print("Auxiliaire")
    return("auxiliaire")
    #return render_template('helper.html')

@app.route('/interactions-entre-plantes-legumes-fruits-arbres-fleurs-aromates-maladies-auxiliaires.html')
def interactions():
    return render_template('interactions.html')

@app.route('/a-propos.html')
@app.route('/about.html')
@cache.cached(timeout=86400)
def about():
    return render_template('about.html')
