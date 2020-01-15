import os
import sys
import csv
import jinja2
import sass
from jsmin import jsmin
from flask import Flask
from flask import render_template, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy

os.makedirs("templates", exist_ok=True)
sys.path.insert(1, "static/")

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from function_search_taxonomy import find_latin_name, find_tax_id
from models import *


def generate_js(file_name):
    species_cat = dict()
    species_wiki = dict()
    species_ncbi = dict()
    months = dict()

    appartenance = dict()
    name_to_index = dict()
    print(db.session.query(Specie).all())
    for enum_id, sp in enumerate(db.session.query(Specie).all()):
        species_cat[sp.name] = sp.category
        species_wiki[sp.name] = sp.wiki
        species_ncbi[sp.name] = sp.NCBI
        months[sp.name] = []
        name_to_index[sp.name] = enum_id
        appartenance[name_to_index[sp.name]] = reverse_cat[sp.category]

    associations_plant = set()
    print(db.session.query(Interaction).all())
    for assoc in db.session.query(Interaction).all():
        associations_plant.add(
            (name_to_index[assoc.source], name_to_index[assoc.target], reverse_interactions[assoc.interaction]))

    index_to_name = reverse_dict(name_to_index)
    print(os.getcwd())
    javascript = open(file_name, "w")
    javascript.write("var graph = {\n")
    # nodes for javascript file
    javascript.write('\t"nodes":[\n')
    javascript.write(
        ",\n".join(['\t\t{{"name":"{0}","group":{1},"value":{2},"wiki":"{3}","ncbi":"{4}"}}'.format(name,
                                                                                                    appartenance[index],
                                                                                                    index,
                                                                                                    species_wiki[name],
                                                                                                    species_ncbi[name])
                    for index, name in index_to_name.items()]))
    javascript.write('\n\t],\n')
    # Forward list
    javascript.write('\t"forward":[\n')
    javascript.write(",\n".join(['\t\t[' + ','.join(
        ['{{"target":{0},"value":"{1}","group":{2}}}'.format(target, interactions[inter], appartenance[target])
         for source, target, inter
         in associations_plant if source == index]) + ']' for index, _ in index_to_name.items()]))
    javascript.write('\n\t],\n')
    # Backward list
    javascript.write('\t"backward":[\n')
    javascript.write(",\n".join(['\t\t[' + ','.join(
        ['{{"source":{0},"value":"{1}","group":{2}}}'.format(source, interactions[inter], appartenance[source])
         for source, target, inter
         in associations_plant if target == index]) + ']' for index, _ in index_to_name.items()]))
    javascript.write('\n\t]\n};')

    javascript.write('\nvar names_liste = ["' + '","'.join(sorted(set(species_cat))) + '"];')

    javascript.write("\nvar groups = {\n")
    javascript.write(
        ",\n".join(['\t{0}:"{1}"'.format(cat_index, cat_name) for cat_index, cat_name in categories.items()]))
    javascript.write('\n};')

    javascript.write("\nvar color = {\n")
    javascript.write(
        ",\n".join(['\t{0}:"{1}"'.format(color_index, color_name) for color_index, color_name in color.items()]))
    javascript.write('\n};')

    javascript.write('\nvar cat_animals = [' + ','.join(sorted([str(reverse_cat[c]) for c in cat_animals])) + '];')
    javascript.write('\nvar cat_pests = [' + ','.join(sorted([str(reverse_cat[c]) for c in cat_pests])) + '];')
    javascript.write(
        '\nvar cat_helpers = [' + ','.join(sorted([str(reverse_cat[c]) for c in (cat_animals - cat_pests)])) + '];')
    javascript.write('\nvar cat_plants = [' + ','.join(sorted([str(reverse_cat[c]) for c in cat_plants])) + '];')

    javascript.write('\nvar interactions = ["' + '","'.join(sorted(set(interactions.values()))) + '"];')
    backward = ', '.join(
        ['"{0}":"{1}"'.format(value, interaction_backward[value].lower()) for value in
         sorted(set(interactions.values()))])
    forward = ', '.join(
        ['"{0}":"{1}"'.format(value, interaction_forward[value].lower()) for value in
         sorted(set(interactions.values()))])
    javascript.write('\nvar filter_name_dico = {"backward":{' + backward + '}, "forward":{' + forward + '}};')

    javascript.close()

    examples = []
    for index, name in index_to_name.items():
        name_associations = [l for l in associations_plant if l[0] == index]
        name_interactions = set([l[2] for l in name_associations])
        if len(name_interactions) == len(description_interactions):
            for interaction in sorted(name_interactions, key=lambda x: abs(x)):
                source, target, inter = [l for l in name_associations if (l[2] == interaction)][0]
                assert inter == interaction
                example = dict()
                example["name_source"] = index_to_name[source]
                example["color_source"] = color[appartenance[source]]
                example["name_target"] = index_to_name[target]
                example["color_target"] = color[appartenance[target]]
                example["link"] = interactions[inter]
                example["description"] = "{0} {1} {2}".format(example["name_source"],
                                                              interaction_forward[interactions[inter]].lower(),
                                                              example["name_target"].lower())
                examples.append(example)
            break

    categories_list = []
    for cat in [sorted(cat_plants), sorted(cat_animals)]:
        categories_list += [(k, color[reverse_cat[k]]) for k in cat]
    return months, index_to_name, appartenance, examples, categories_list, sorted(
        [reverse_cat[cat] for cat in cat_plants]), sorted([reverse_cat[cat] for cat in cat_animals]), {
               "backward": interaction_backward, "forward": interaction_forward}


def render_index():
    minifiy = True
    months, plants, appartenance, examples, categories, cat_plants, cat_animals, dict_interactions = generate_js(
        "static/js/data.js")

    minified = ""
    if minifiy:
        minified = "min."
        for js_path in ["static/js/MonPotager.js", "static/js/data.js"]:
            with open(js_path, 'r') as js_file:
                jsminified = jsmin(js_file.read())
                jsminified_file = open(js_path.replace('.js', ".min.js"), "w")
                jsminified_file.write(jsminified)
                jsminified_file.close()
                print(OKBLUE + "Minifying " + js_path + ENDC)
    else:
        print(OKBLUE + ".js and .css not minified, use -c option if you wish to compress files." + ENDC)

    css = open("static/css/MonPotager." + minified + "css", "w")
    css.write(
        sass.compile(filename='static/MonPotager.css.scss', output_style=('compressed' if minifiy else "nested")))
    css.close()

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
    template = env.get_template('static/MonPotager.html')

    first_letter = sorted(set([name[0].upper() for key, name in plants.items() if (appartenance[key] in cat_plants)]))
    sorted_appartenance = sorted(appartenance.items(), key=lambda pl: plants[pl[0]].lower())

    template.stream(months=months,
                    plants=plants,
                    examples=examples,
                    minified=minified,
                    cat_plants=cat_plants,
                    cat_animals=cat_animals,
                    categories=categories,
                    first_letter=first_letter,
                    interactions=dict_interactions,
                    appartenance=sorted_appartenance).dump('templates/index.html')
    print(OKGREEN + "Application generated.\nOpen the file {0}/templates/index.html to open the application.".format(
        os.getcwd()) + ENDC)


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
        db.session.add(inter)
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
