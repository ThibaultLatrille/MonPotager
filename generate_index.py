import csv
from models import Specie, Interaction
from toolbox import *
import jinja2
from jsmin import jsmin
import sass
import os


def generate_js(file_name):
    species_cat = dict()
    species_wiki = dict()
    species_ncbi = dict()
    months = dict()

    appartenance = dict()
    name_to_index = dict()
    for enum_id, sp in enumerate(Specie.query.all()):
        species_cat[sp.name] = sp.category
        species_wiki[sp.name] = sp.wiki
        species_ncbi[sp.name] = sp.NCBI
        months[sp.name] = []
        name_to_index[sp.name] = enum_id
        appartenance[name_to_index[sp.name]] = reverse_cat[sp.category]

    associations_plant = set()
    for assoc in Interaction.query.all():
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


if __name__ == '__main__':
    render_index()
