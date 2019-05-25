from flask import render_template
from . import app

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/<int:post_id>-<string:name>.html')
def item_page():
    return 'Plant'

@app.route('/interactions-entre-plantes-legumes-fruits-arbres-fleurs-aromates-maladies-auxiliaires.html')
def interactions():
    return render_template('interactions.html')

@app.route('/a-propos.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
