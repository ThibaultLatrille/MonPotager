# -*- coding: utf-8 -*-


def reverse_dict(dico):
    return {value: key for key, value in dico.items()}


def generate_js(file_name):
    categories = {1: "Légume", 2: "Fruit", 3: "Arômate", 4: "Fleur", 5: "Nuisible", 6: "Auxiliaire", 7: "Céréale",
                  8: "Arbres"}
    cat_animals = {"Nuisible", "Auxiliaire"}
    cat_plantes = set(categories.values()) - cat_animals
    reverse_cat = reverse_dict(categories)

    txt_associations = {"favorise": 1, "défavorise": -1, "attire": 2, "repousse": -2}
    associations = {-1: "neg", 1: "pos", -2: "rep", 2: "atr"}
    association_backward = {"neg": "défavorise", "pos": "favorise", "rep": "repousse", "atr": "attire"}
    association_forward = {"neg": "défavorisé par", "pos": "favorisé par", "rep": "repoussé par", "atr": "attiré par"}

    interactions = open("interactions.txt", "r")
    interactions_plante = set()
    appartenance = dict()
    name_to_index = dict()
    count = 0
    nbr_errors = 0
    for line in interactions.readlines():
        specie_source, interaction, specie_target = line.strip("\n").split('|')
        name_source, cat_source = specie_source.split('\\')
        name_target, cat_target = specie_target.split('\\')
        if name_source not in name_to_index:
            name_to_index[name_source] = count
            count += 1
        if name_target not in name_to_index:
            name_to_index[name_target] = count
            count += 1
        appartenance[name_to_index[name_source]] = reverse_cat[cat_source]
        appartenance[name_to_index[name_target]] = reverse_cat[cat_target]

        source = name_to_index[name_source]
        target = name_to_index[name_target]
        assert interaction in txt_associations.keys(), "Interaction '{0}' n'existe pas, seulement {1} sont possible".format(
            interaction, "|".join(txt_associations.keys()))
        inter = txt_associations[interaction]

        if ((cat_target in cat_animals) and abs(inter) != 2) or ((cat_target in cat_plantes) and abs(inter) != 1):
            if (cat_target in cat_animals) and abs(inter) != 2:
                inter *= 2
            else:
                inter /= 2
            nbr_errors += 1
            print("Erreur: {0} ({3}) {1} {2} ({4})".format(name_source, interaction, name_target,
                                                           cat_source, cat_target))
            print("Remplacé par: {0} ({3}) {1} {2} ({4})".format(name_source,
                                                                 association_backward[associations[inter]],
                                                                 name_target, cat_source, cat_target))

        interactions_plante.add((source, target, inter))

    if nbr_errors > 0:
        print("{0} erreurs au total".format(nbr_errors))
    interactions.close()

    index_to_name = reverse_dict(name_to_index)

    javascript = open(file_name, "w")
    javascript.write("var graph = {\n")
    # nodes for javascript file
    javascript.write('\t"nodes":[\n')
    javascript.write(
        ",\n".join(['\t\t{{"name":"{0}","group":{1},"value":{2}}}'.format(name, appartenance[index], index)
                    for index, name in index_to_name.items()]))
    javascript.write('\n\t],\n')
    # Forward list
    javascript.write('\t"forward":[\n')
    javascript.write(",\n".join(['\t\t[' + ','.join(
        ['{{"target":{0},"value":"{1}","group":{2}}}'.format(target, associations[inter], appartenance[target])
         for source, target, inter
         in interactions_plante if source == index]) + ']' for index, _ in index_to_name.items()]))
    javascript.write('\n\t],\n')
    # Backward list
    javascript.write('\t"backward":[\n')
    javascript.write(",\n".join(['\t\t[' + ','.join(
        ['{{"source":{0},"value":"{1}","group":{2}}}'.format(source, associations[inter], appartenance[source])
         for source, target, inter
         in interactions_plante if target == index]) + ']' for index, _ in index_to_name.items()]))
    javascript.write('\n\t]\n};')

    javascript.write("\nvar groups = {\n")
    javascript.write(
        ",\n".join(['\t{0}:"{1}"'.format(cat_index, cat_name) for cat_index, cat_name in categories.items()]))
    javascript.write('\n};')

    javascript.write('\nvar cat_animals = [' + ','.join(sorted([str(reverse_cat[c]) for c in cat_animals])) + '];')
    javascript.write('\nvar cat_plantes = [' + ','.join(sorted([str(reverse_cat[c]) for c in cat_plantes])) + '];')

    javascript.write('\nvar associations = ["' + '","'.join(sorted(set(associations.values()))) + '"];')
    forward = ', '.join(
        ['"{0}":"{1}"'.format(value, association_forward[value]) for value in sorted(set(associations.values()))])
    backward = ', '.join(
        ['"{0}":"{1}"'.format(value, association_backward[value]) for value in sorted(set(associations.values()))])
    javascript.write('\nvar filter_name_dico = {"forward":{' + forward + '}, "backward":{' + backward + '}};')

    javascript.close()
    return index_to_name, appartenance
