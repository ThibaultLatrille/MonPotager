from flask import Flask
from flask import render_template, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
import sys
import os

os.makedirs("templates", exist_ok=True)
sys.path.insert(1, "static/")

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from generate_index import *
from function_search_taxonomy import find_latin_name, find_tax_id


@app.route("/species/new-entry", methods=["GET", "POST"])
def create_entry():
    req = request.get_json()
    name = req['scientiesp'] if req['scientiesp'] != "-" else req['namaesp']
    wikipedia = find_latin_name(name)
    if req['scientiesp'] != "-":
        for value in wikipedia.values():
            value[0] = req['namaesp']

    taxonomic_dico = find_tax_id(wikipedia)
    sp = Specie(
        name=taxonomic_dico[name][0],
        common_name=taxonomic_dico[name][0],
        category=req['catesp'],
        wiki=taxonomic_dico[name][1],
        taxonomy=taxonomic_dico[name][2],
        latin_name=taxonomic_dico[name][3],
        TaxID=taxonomic_dico[name][4],
        NCBI="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=" + taxonomic_dico[name][4]
    )
    if sp.is_valid:
        db.session.add(sp)
        db.session.commit()
        render_index()
    res = make_response(jsonify(taxonomic_dico[name]), 200)
    return res


@app.route('/association/new-entry', methods=["POST", "GET"])
def create_association():
    req = request.get_json()
    inter = Interaction(
        source=req["espSource"],
        target=req["espCible"],
        interaction=interactions[description_interactions[req["espInteraction"]]],
        references=req["espReference"]
    )
    if inter.is_valid:
        db.session.add()
        db.session.commit()
    render_index()
    return req


@app.route("/")
def monpotager():
    if not os.path.isfile('templates/index.html'):
        render_index()
    return render_template('index.html')


@app.route("/render")
def re_render():
    render_index()
    return render_template('index.html')


@app.route(os.environ['SEED_PATH'])
def seed_db():
    db.session.query(Interaction).delete()
    db.session.commit()
    db.session.query(Specie).delete()
    db.session.commit()

    with open('static/database/especes_v2.csv', 'r', newline='', encoding='utf-8') as csvfile:
        speciesreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(speciesreader)
        for line in speciesreader:
            taxId = 0
            try:
                taxId = int(line[5])
            except ValueError:
                pass
            sp = Specie(
                name=line[7],
                common_name=line[0],
                category=line[1],
                wiki=line[2],
                taxonomy=line[3],
                latin_name=line[4],
                TaxID=taxId,
                NCBI=line[6],
            )
            if sp.is_valid:
                try:
                    db.session.add(sp)
                    db.session.commit()
                except Exception as e:
                    print(e)

    with open('static/database/associations.csv', 'r', newline='', encoding='utf-8') as csvfile:
        associationsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(associationsreader)
        for source, assoc, target, references, _, _ in associationsreader:
            inter = Interaction(source=source, target=target, interaction=interactions[description_interactions[assoc]],
                                references=references)
            if inter.is_valid():
                try:
                    db.session.add(inter)
                    db.session.commit()
                except Exception as e:
                    print(e)

    render_index()
    return render_template('index.html')


# run the application
if __name__ == "__main__":
    app.run(threaded=True)
