# -*- coding: utf-8 -*-

from dico_appartenance import appartenance
from dico_interaction_plantes import interaction_plante
from dico_plantes_categories import plantes, categories, associations, association_forward, association_backward
from exemple_association import list_defavorable, list_favorable


def generate_js():
    interactions_set = set(interaction_plante)
    interactions = [(i, j, v) for i, j, v in interactions_set if abs(v) == 3]
    interactions.extend([(j, i, v) for i, j, v in interactions_set if abs(v) != 3])

    javascript = open("data.js", "w")

    javascript.write("var graph = {\n")
    # nodes for javascript file
    javascript.write('\t"nodes":[\n')
    javascript.write(",\n".join(['\t\t{{"name":"{0}","group":"{1}","value":{2}}}'.format(plantes[key], value, plante_id)
                                 for plante_id, (key, value) in enumerate(appartenance.items())]))
    javascript.write('\n\t],\n')
    # Forward list
    javascript.write('\t"forward":[\n')
    javascript.write(",\n".join(['\t\t[' + ','.join(
        ['{{"target":{0},"value":"{1}","group":{2}}}'.format(plante_2, associations[inter], appartenance[plante_2])
         for plante_1, plante_2, inter
         in interactions if plante_1 == plante_id]) + ']' for plante_id, _ in plantes.items()]))
    javascript.write('\n\t],\n')
    # Backward list
    javascript.write('\t"backward":[\n')
    javascript.write(",\n".join(['\t\t[' + ','.join(
        ['{{"source":{0},"value":"{1}","group":{2}}}'.format(plante_1, associations[inter], appartenance[plante_1])
         for plante_1, plante_2, inter
         in interactions if plante_2 == plante_id]) + ']' for plante_id, _ in plantes.items()]))
    javascript.write('\n\t]\n};')

    javascript.write("\nvar groups = {\n")
    javascript.write(",\n".join(['\t{0}:"{1}"'.format(key, value) for key, value in categories.items()]))
    javascript.write('\n};')

    javascript.write("\nvar list_defavorable = [" + ",".join(map(str, list_defavorable)) + "];")
    javascript.write("\nvar list_favorable = [" + ",".join(map(str, list_favorable)) + "];")
    javascript.write('\nvar associations = ["' + '","'.join(set(associations.values())) + '"];')
    forward = ', '.join(['"{0}":"{1}"'.format(value, association_forward[value]) for value in set(associations.values())])
    backward = ', '.join(['"{0}":"{1}"'.format(value, association_backward[value]) for value in set(associations.values())])
    javascript.write('\nvar filter_name_dico = {"forward":{' + forward + '}, "backward":{' + backward + '}};')

    javascript.close()

    print("Javascript data file successfully written !")
