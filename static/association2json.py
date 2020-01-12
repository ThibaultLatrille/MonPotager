# -*- coding: utf-8 -*-
import csv

WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

color = {
    0: "#0F0F0F", 1: "#1776b6", 2: "#ff7f0e", 3: "#9564bf", 4: "#f7b6d2", 5: "#d62728", 6: "#24a221", 7: "#ffe778",
    8: "#8d5649"
}

categories = {1: "Légume", 2: "Fruit", 3: "Arômate", 4: "Fleur", 5: "Nuisible", 6: "Auxiliaire", 7: "Céréale",
              8: "Arbres"}


def reverse_dict(dico):
    return {value: key for key, value in dico.items()}


def print_w(txt):
    print(WARNING + txt + ENDC)


def print_fail_assoc(source, inter, target, line):
    print(FAIL + "Association '{0}' '{1}' '{2}' n'est pas prise en compte (ligne {3}).".format(source, inter,
                                                                                               target, line) + ENDC)


def generate_js(file_name):
    cat_animals = {"Nuisible", "Auxiliaire"}
    cat_plants = set(categories.values()) - cat_animals
    cat_pests = {"Nuisible"}
    reverse_cat = reverse_dict(categories)

    description_interactions = {"favorise": 1, "défavorise": -1, "attire": 2, "repousse": -2}
    interactions = {-1: "neg", 1: "pos", -2: "rep", 2: "atr"}
    interaction_forward = {"neg": "Défavorise", "pos": "Favorise", "rep": "Repousse", "atr": "Attire"}
    interaction_backward = {"neg": "Défavorisé par", "pos": "Favorisé par", "rep": "Repoussé par", "atr": "Attiré par"}

    species_cat = dict()
    species_name = dict()
    species_wiki = dict()
    species_ncbi = dict()
    months = dict()

    appartenance = dict()
    name_to_index = dict()
    count = 0
    nbr_errors = 0
    with open('static/database/especes_v2.csv', 'r') as csvfile:
        speciesreader = csv.reader(csvfile)
        next(speciesreader)
        for line in speciesreader:
            name=line[7]
            cat=line[1]
            disp_name=line[0]
            txt=line[4]
            wiki=line[2]
            ncbi=line[6]
            species_cat[name] = cat
            species_name[name] = name
            species_wiki[disp_name] = wiki
            species_ncbi[disp_name]=ncbi
            months[name.capitalize() ] = line[9:] #Donc la je met en majuscule la première lettre du nom car je comprends rien à la configuration de [key] et j'ai pas envie de chercher et surtout ca marche très bien comme ça :) En gros pour chercher dans le html le calendrier d'une plante on fera référence à son nom
            name_to_index[name]=count
            appartenance[name_to_index[name]]=reverse_cat[cat]
            count+=1
    associations_plant = set()

    with open('static/database/associations.csv', 'r') as csvfile:
        associationsreader = csv.reader(csvfile)
        next(associationsreader)
        for line, (specie_source, interaction, specie_target, source, rank, details) in enumerate(associationsreader):

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
                nbr_errors += 1
                print_w("Erreur: {0} ({3}) {1} {2} ({4}).".format(name_source, interaction, name_target,
                                                                  cat_source, cat_target))
                print_w("Remplacé par: {0} ({3}) {1} {2} ({4}).".format(name_source,
                                                                        interaction_forward[interactions[inter]],
                                                                        name_target, cat_source, cat_target))

            associations_plant.add((source, target, inter))

    if nbr_errors > 0:
        print_w("{0} erreurs corrigées au total".format(nbr_errors))
    index_to_name = reverse_dict(name_to_index)
    javascript = open(file_name, "w")
    javascript.write("var graph = {\n")
    # nodes for javascript file
    javascript.write('\t"nodes":[\n')
    javascript.write(
        ",\n".join(['\t\t{{"name":"{0}","group":{1},"value":{2},"wiki":"{3}","ncbi":"{4}"}}'.format(name, appartenance[index], index,species_wiki[name],species_ncbi[name])
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
    print (examples)
    return months, index_to_name, appartenance, examples, categories_list, \
           sorted([reverse_cat[cat] for cat in cat_plants]), \
           sorted([reverse_cat[cat] for cat in cat_animals]), \
           {"backward": interaction_backward, "forward": interaction_forward}
