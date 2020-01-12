import subprocess
from flask import Flask
from flask import render_template, jsonify, request, make_response
import sys

sys.path.insert(1, "static/")
from MonPotager import main
from function_search_taxonomy import findLatin_name, findTaxID

# creates a Flask application, named app
app = Flask(__name__)


@app.route("/species/new-entry", methods=["GET", "POST"])
def create_entry():
    req = request.get_json()
    file = open("static/database/especes_v2.csv", "a")
    s = "\""
    v = ","
    if req['scientiesp'] != "-":
        wikipedia = findLatin_name(req['scientiesp'])
        for value in wikipedia.values():
            value[0] = req['namaesp']
        taxonomic_dico = findTaxID(wikipedia)
        taxonomic_dico[req['scientiesp']].append(req['catesp'])
        file.write(
            s + taxonomic_dico[req['scientiesp']][0] + s + v + s + taxonomic_dico[req['scientiesp']][5] + s + v + s
            + taxonomic_dico[req['scientiesp']][1] + s + v + s + taxonomic_dico[req['scientiesp']][2]
            + s + v + s + taxonomic_dico[req['scientiesp']][3] + s + v + s + taxonomic_dico[req['scientiesp']][4]
            + s + v + s + " https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=" +
            taxonomic_dico[req['scientiesp']][4] + s + v + s + taxonomic_dico[req['scientiesp']][0] + '"' + '\n')
        file.close()
        createIndex()
        res = make_response(jsonify(taxonomic_dico[req['scientiesp']]), 200)
        return res
    else:
        scientific_name = findLatin_name(req['namaesp'])
        taxonomic_dico = findTaxID(scientific_name)
        taxonomic_dico[req['namaesp']].append(req['catesp'])
        file.write(s + taxonomic_dico[req['namaesp']][0] + s + v + s + taxonomic_dico[req['namaesp']][5] + s + v + s
                   + taxonomic_dico[req['namaesp']][1] + s + v + s + taxonomic_dico[req['namaesp']][2]
                   + s + v + s + taxonomic_dico[req['namaesp']][3] + s + v + s + taxonomic_dico[req['namaesp']][
                       4] + s + v + s
                   + " https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=" + taxonomic_dico[req['namaesp']][
                       4] + s + v + s + taxonomic_dico[req['namaesp']][0] + '"' + '\n')
        file.close()
        createIndex()
        res = make_response(jsonify(taxonomic_dico[req['namaesp']]), 200)
        return res


@app.route('/association/new-entry', methods=["POST", "GET"])
def create_association():
    req = request.get_json()
    print(req)
    file = open("static/database/associations.csv", "a")
    s = "\""
    v = ","
    file.write(
        s + req["espSource"] + s + v + s + req["espInteraction"] + s + v + s + req["espCible"] + s + v + v + v + "\n")
    file.close()
    createIndex()
    return req


@app.route("/")
def monpotager():
    return render_template('index.html')


def createIndex():
    main()
    subprocess.run(["mv", "index.html", "templates/"])


# run the application
if __name__ == "__main__":
    createIndex()
    app.run(debug=True)
