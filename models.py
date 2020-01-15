from app import db


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


class Specie(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    common_name = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), nullable=False)
    wiki = db.Column(db.String())
    taxonomy = db.Column(db.String())
    latin_name = db.Column(db.String())
    TaxID = db.Column(db.Integer())
    NCBI = db.Column(db.String())

    def __init__(self, common_name, category, wiki, taxonomy, latin_name, TaxID, NCBI, name):
        self.name = name
        self.common_name = common_name
        self.category = category
        self.wiki = wiki
        self.taxonomy = taxonomy
        self.latin_name = latin_name
        self.TaxID = TaxID
        self.NCBI = NCBI

    def is_valid(self):
        return self.category in categories.values()

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'common_name': self.common_name,
            'category': self.category,
            'wiki': self.wiki,
            'taxonomy': self.taxonomy,
            'latin_name': self.latin_name,
            'TaxID': self.TaxID,
            'NCBI': self.NCBI,
            'name': self.name
        }


class Interaction(db.Model):
    __tablename__ = 'interactions'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(), nullable=False)
    target = db.Column(db.String(), nullable=False)
    interaction = db.Column(db.String(), nullable=False)
    references = db.Column(db.String())

    def __init__(self, source, target, interaction, references):
        self.source = source
        self.target = target
        self.interaction = interaction
        self.references = references

    def is_valid(self):
        specie_source = Specie.query.filter_by(name=self.source).first()
        if specie_source is None:
            print_w("Source " + self.source + "' n'est pas dans le dictionnaire des espèces.")
            return False

        target_specie = Specie.query.filter_by(name=self.target).first()
        if target_specie is None:
            print_w("Cible " + self.source + "' n'est pas dans le dictionnaire des espèces.")
            return False

        if self.source == self.target:
            print_w("La source ({0}) et la cible sont les mêmes espèces ({1})".format(self.source, self.target))
            return False

        if self.interaction not in reverse_interactions.keys():
            print_w("Interaction '{0}' n'existe pas, seulement {1} sont possible".format(
                self.interaction, "|".join(reverse_interactions.keys())))
            return False

        inter = reverse_interactions[self.interaction]
        cat_target = target_specie.category
        if ((cat_target in cat_animals) and abs(inter) != 2) or ((cat_target in cat_plants) and abs(inter) != 1):
            print_w("Cible est '{0}', l'interaction {1} ne peut pas s'appliquer".format(cat_target, interaction_forward[
                self.interaction]))
            return False

        inter_db = Interaction.query.filter_by(source=self.source, target=self.target).first()
        if inter_db is None:
            return True
        else:
            print_w("L'interaction de {0} vers {1} existe déjà".format(self.source, self.target))
            return False

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'source': self.source,
            'target': self.target,
            'interaction': self.interaction,
            'references': self.references
        }
