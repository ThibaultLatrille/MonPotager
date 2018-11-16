# -*- coding: utf-8 -*-


def reverse_dict(dico):
    return {value: key for key, value in dico.items()}


def generate_js():
    categories = {1: "Légume", 2: "Fruit", 3: "Arômate", 4: "Fleur", 5: "Nuisible", 6: "Auxiliaire", 7: "Céréale",
                  8: "Arbres"}
    reverse_cat = reverse_dict(categories)

    txt_associations = {"favorise": 1, "défavorise": -1, "nuit à": -1, "attire": 2, "repousse": -2}
    interactions = open("interactions.txt", "r")
    interactions_plante = set()
    appartenance = {}
    plantes = {}
    count = 0
    for line in interactions.readlines():
        specie_1, interaction, specie_2 = line.strip("\n").split('|')
        name_1, cat_1 = specie_1.split('\\')
        name_2, cat_2 = specie_2.split('\\')
        if not name_1 in plantes:
            plantes[name_1] = count
            count += 1
        if not name_2 in plantes:
            plantes[name_2] = count
            count += 1
        appartenance[plantes[name_1]] = reverse_cat[cat_1]
        appartenance[plantes[name_2]] = reverse_cat[cat_2]
        interactions_plante.add((plantes[name_1], plantes[name_2], txt_associations[interaction]))
    interactions.close()
    plantes = reverse_dict(plantes)

    associations = {-1: "neg", 1: "pos", -2: "rep", 2: "atr"}
    association_backward = {"neg": "défavorise", "pos": "favorise", "rep": "repousse", "atr": "attire"}
    association_forward = {"neg": "défavorisé par", "pos": "favorisé par", "rep": "repoussé par", "atr": "attiré par"}

    javascript = open("js/data.js", "w")
    javascript.write("var graph = {\n")
    # nodes for javascript file
    javascript.write('\t"nodes":[\n')
    javascript.write(",\n".join(['\t\t{{"name":"{0}","group":"{1}","value":{2}}}'.format(name, appartenance[plante_id], plante_id)
                                 for plante_id, name in plantes.items()]))
    javascript.write('\n\t],\n')
    # Forward list
    javascript.write('\t"forward":[\n')
    javascript.write(",\n".join(['\t\t[' + ','.join(
        ['{{"target":{0},"value":"{1}","group":{2}}}'.format(plante_2, associations[inter], appartenance[plante_2])
         for plante_1, plante_2, inter
         in interactions_plante if plante_1 == plante_id]) + ']' for plante_id, _ in plantes.items()]))
    javascript.write('\n\t],\n')
    # Backward list
    javascript.write('\t"backward":[\n')
    javascript.write(",\n".join(['\t\t[' + ','.join(
        ['{{"source":{0},"value":"{1}","group":{2}}}'.format(plante_1, associations[inter], appartenance[plante_1])
         for plante_1, plante_2, inter
         in interactions_plante if plante_2 == plante_id]) + ']' for plante_id, _ in plantes.items()]))
    javascript.write('\n\t]\n};')

    javascript.write("\nvar groups = {\n")
    javascript.write(",\n".join(['\t{0}:"{1}"'.format(key, value) for key, value in categories.items()]))
    javascript.write('\n};')

    javascript.write('\nvar associations = ["' + '","'.join(sorted(set(associations.values()))) + '"];')
    forward = ', '.join(['"{0}":"{1}"'.format(value, association_forward[value]) for value in sorted(set(associations.values()))])
    backward = ', '.join(['"{0}":"{1}"'.format(value, association_backward[value]) for value in sorted(set(associations.values()))])
    javascript.write('\nvar filter_name_dico = {"forward":{' + forward + '}, "backward":{' + backward + '}};')

    javascript.close()

    print("Javascript data file successfully written !")
    return plantes, appartenance
