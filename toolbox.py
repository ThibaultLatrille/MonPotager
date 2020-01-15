def reverse_dict(dico):
    return {value: key for key, value in dico.items()}


WARNING = '\033[93m'
FAIL = '\033[91m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'

color = {
    0: "#0F0F0F", 1: "#1776b6", 2: "#ff7f0e", 3: "#9564bf", 4: "#f7b6d2", 5: "#d62728", 6: "#24a221", 7: "#ffe778",
    8: "#8d5649"
}

categories = {1: "Légume", 2: "Fruit", 3: "Arômate", 4: "Fleur", 5: "Nuisible", 6: "Auxiliaire", 7: "Céréale",
              8: "Arbres"}

cat_animals = {"Nuisible", "Auxiliaire"}
cat_plants = set(categories.values()) - cat_animals
cat_pests = {"Nuisible"}
reverse_cat = reverse_dict(categories)

description_interactions = {"favorise": 1, "défavorise": -1, "attire": 2, "repousse": -2}
interactions = {-1: "neg", 1: "pos", -2: "rep", 2: "atr"}
reverse_interactions = reverse_dict(interactions)
interaction_forward = {"neg": "Défavorise", "pos": "Favorise", "rep": "Repousse", "atr": "Attire"}
interaction_backward = {"neg": "Défavorisé par", "pos": "Favorisé par", "rep": "Repoussé par", "atr": "Attiré par"}


def print_w(txt):
    print(WARNING + txt + ENDC)


def print_fail_assoc(source, inter, target, line):
    print(FAIL + "Association '{0}' '{1}' '{2}' n'est pas prise en compte (ligne {3}).".format(source, inter,
                                                                                               target, line) + ENDC)
