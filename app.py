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
    db.session.add(sp)
    db.session.commit()
    render_index()
    res = make_response(jsonify(taxonomic_dico[name]), 200)
    return res


@app.route('/association/new-entry', methods=["POST", "GET"])
def create_association():
    req = request.get_json()
    db.session.add(Interaction(
        source=req["espSource"],
        target=req["espCible"],
        interaction=interactions[description_interactions[req["espInteraction"]]],
        references=req["espReference"]
    ))
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
    db.drop_all()
    db.create_all()
    db.session.commit()

    species_cat = dict()
    species_name = dict()
    name_to_index = dict()
    associations_plant = set()
    count = 0

    with open('static/database/especes_v2.csv', 'r', newline='', encoding='utf-8') as csvfile:
        speciesreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(speciesreader)
        for line in speciesreader:
            disp_name = line[0]
            name = line[7]
            cat = line[1]
            species_cat[name] = cat
            species_name[name] = name
            name_to_index[name] = count
            count += 1
            taxId = 0
            try:
                taxId = int(line[5])
            except ValueError:
                pass
            db.session.add(Specie(
                name=name,
                common_name=disp_name,
                category=cat,
                wiki=line[2],
                taxonomy=line[3],
                latin_name=line[4],
                TaxID=taxId,
                NCBI=line[6],
            ))
            db.session.commit()

    with open('static/database/associations.csv', 'r', newline='', encoding='utf-8') as csvfile:
        associationsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(associationsreader)
        for line, (specie_source, interaction, specie_target, references, rank, details) in enumerate(
                associationsreader):

            drop = False
            for specie in [specie_source, specie_target]:
                if specie not in species_name:
                    print_w("'" + specie + "' n'est pas dans le dictionnaire des espèces.")
                    drop = True

            if drop:
                print_fail_assoc(specie_source, interaction, specie_target, line + 1)
                continue

            name_source, cat_source = species_name[specie_source], species_cat[specie_source]
            name_target, cat_target = species_name[specie_target], species_cat[specie_target]
            if name_source == name_target:
                print_w("La source ({0}) et la cible sont les mêmes espèces ({1})".format(name_source, name_target))
                print_fail_assoc(specie_source, interaction, specie_target, line + 1)
                continue

            source = name_to_index[name_source]
            target = name_to_index[name_target]
            if interaction not in description_interactions.keys():
                print_w("interaction '{0}' n'existe pas, seulement {1} sont possible".format(
                    interaction, "|".join(description_interactions.keys())))
                print_fail_assoc(specie_source, interaction, specie_target, line + 1)
                continue

            inter = description_interactions[interaction]

            same_association = [assoc for assoc in associations_plant if (assoc[0] == source and assoc[1] == target)]
            if len(same_association) > 0:
                for assoc in same_association:
                    if assoc[2] == inter:
                        print_w("Erreur: {0} {1} {2} car l'association existe déjà.".format(name_source,
                                                                                            interaction,
                                                                                            name_target))
                    else:
                        print_w(
                            "Erreur: {0} {1} {2} impossible car {3} déjà.".format(
                                name_source, interaction,
                                name_target, interaction_forward[interactions[assoc[2]]].lower()))
                print_fail_assoc(specie_source, interaction, specie_target, line + 1)
                continue

            if ((cat_target in cat_animals) and abs(inter) != 2) or ((cat_target in cat_plants) and abs(inter) != 1):
                if (cat_target in cat_animals) and abs(inter) != 2:
                    inter *= 2
                else:
                    inter /= 2
                print_w("Erreur: {0} ({3}) {1} {2} ({4}).".format(name_source, interaction, name_target,
                                                                  cat_source, cat_target))
                print_w("Remplacé par: {0} ({3}) {1} {2} ({4}).".format(name_source,
                                                                        interaction_forward[interactions[inter]],
                                                                        name_target, cat_source, cat_target))
            db.session.add(Interaction(
                source=name_source,
                target=name_target,
                interaction=interactions[inter],
                references=references
            ))
            db.session.commit()

    render_index()
    return render_template('index.html')


# run the application
if __name__ == "__main__":
    app.run(threaded=True)
