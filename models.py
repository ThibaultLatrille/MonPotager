from app import db
from toolbox import *


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
