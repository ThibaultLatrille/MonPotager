from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ANSI escape sequences for colored output in terminal
WARNING = '\033[93m'
FAIL = '\033[91m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'


def reverse_dict(dico):
    return {value: key for key, value in dico.items()}


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
    s = f"Association '{source}' '{inter}' '{target}' n'est pas prise en compte (ligne {line})."
    print(FAIL + s + ENDC)


class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class AlreadyExistsError(Exception):
    def __init__(self, message):
        super().__init__(message)


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
        try:
            taxId = int(TaxID)
        except ValueError:
            taxId = 0
        self.name = name
        self.common_name = common_name
        self.category = category
        self.wiki = wiki
        self.taxonomy = taxonomy
        self.latin_name = latin_name
        self.TaxID = taxId
        self.NCBI = NCBI

    def is_valid(self):
        if len(self.name) < 3:
            raise ValidationError(f"le nom {self.name} est trop petit.")

        if self.category not in categories.values():
            raise ValidationError(f"la catégorie {self.category} n'existe.")

        specie = Specie.query.filter_by(name=self.name).first()
        if specie is not None:
            raise AlreadyExistsError(f"l'espèce {self.name} existe déjà dans la base de données.")

    def __repr__(self):
        s = "Espèce : {0} ({1})\n".format(self.common_name.capitalize(), self.category.lower())
        s += "Page wikipedia : {0}\n".format(self.wiki)
        s += "Taxonomie : {0}\n".format(self.taxonomy)
        s += "Nom latin : {0}\n".format(self.latin_name)
        s += "Page NCBI : {0}\n".format(self.NCBI)
        s += "TaxID : {0}".format(self.TaxID)
        return s

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'common_name': self.common_name,
            'category': self.category,
            'wiki': self.wiki,
            'taxonomy': self.taxonomy,
            'latin_name': self.latin_name,
            'TaxID': self.TaxID,
            'NCBI': self.NCBI
        }


def add_or_update_specie(name, common_name, category, latin_name, wiki="", taxonomy="", TaxID="", NCBI=""):
    """
    Add a new specie or update an existing one.
    """
    specie = Specie(name=name, common_name=common_name, category=category, wiki=wiki, taxonomy=taxonomy,
                    latin_name=latin_name, TaxID=TaxID, NCBI=NCBI)
    try:
        specie.is_valid()
        db.session.add(specie)
        db.session.commit()
        return specie
    except ValidationError as e:
        db.session.rollback()
        print(f"Validation error for specie {name}: {e}")
    except AlreadyExistsError as e:
        # If the specie already exists, update it instead
        existing_specie = Specie.query.filter_by(name=name).first()
        if existing_specie:
            try:
                existing_specie.common_name = common_name
                existing_specie.category = category
                existing_specie.wiki = wiki
                existing_specie.taxonomy = taxonomy
                existing_specie.latin_name = latin_name
                existing_specie.TaxID = TaxID
                existing_specie.NCBI = NCBI
                db.session.commit()
                return existing_specie
            except ValidationError as e:
                db.session.rollback()
                print(f"Validation error while updating specie {name}: {e}")
    except Exception as e:
        db.session.rollback()
        print(f"Error processing specie {name}: {e}")
    return None


class Interaction(db.Model):
    __tablename__ = 'interactions'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(), nullable=False)
    target = db.Column(db.String(), nullable=False)
    interaction = db.Column(db.String(), nullable=False)
    references = db.Column(db.String())
    weight = db.Column(db.Float, default=1.0)

    def __init__(self, source, target, interaction, references, weight=1.0):
        self.source = source
        self.target = target
        self.interaction = interaction
        self.references = references
        self.weight = weight

    def is_valid(self):
        specie_source = Specie.query.filter_by(name=self.source).first()
        if specie_source is None:
            raise ValidationError(f"l'espèce source '{self.source}' n'est pas dans le dictionnaire des espèces.")

        target_specie = Specie.query.filter_by(name=self.target).first()
        if target_specie is None:
            raise ValidationError(f"l'espèce cible '{self.target}' n'est pas dans le dictionnaire des espèces.")

        if self.source == self.target:
            s = f"l'espèce source ({self.source}) et la cible sont les mêmes espèces ({self.target})."
            raise ValidationError(s)

        if self.interaction not in reverse_interactions.keys():
            s = f"l'interaction '{self.interaction}' n'est pas reconnue, seulement {', '.join(reverse_interactions.keys())} sont possibles."
            raise ValidationError(s)

        inter = reverse_interactions[self.interaction]
        cat_target = target_specie.category
        if ((cat_target in cat_animals) and abs(inter) != 2) or ((cat_target in cat_plants) and abs(inter) != 1):
            s = f"l'espèce cible est '{cat_target}', l'interaction {interaction_forward[self.interaction]} ne peut pas s'appliquer."
            raise ValidationError(s)

        inter_db = Interaction.query.filter_by(source=self.source, target=self.target).first()
        if inter_db is not None:
            raise AlreadyExistsError(f"l'interaction de {self.source} vers {self.target} existe déjà.")

    def update(self, other):
        """
        Update the interaction with another one, merging references and summing weights.
        """
        if self.interaction == other.interaction:
            self.weight += other.weight
        elif (self.interaction != other.interaction) and (
                reverse_interactions[self.interaction] == -reverse_interactions[other.interaction]):
            self.weight -= other.weight
        else:
            s = f"Cannot update interaction {self.source} -> {self.target} with different types: " \
                f"{self.interaction} and {other.interaction}."
            raise ValidationError(s)
        self.references += f", {other.references}"

    def __repr__(self):
        s = f"Interaction de {self.source.capitalize()} vers {self.target} : {interaction_forward[self.interaction].lower()} ({self.weight})\n"
        s += f"Références : {self.references}"
        return s

    def serialize(self):
        return {
            'id': self.id,
            'source': self.source,
            'target': self.target,
            'interaction': self.interaction,
            'references': self.references,
            'weight': self.weight
        }


def add_or_update_interaction(source, target, interaction, references="", weight=1.0):
    """
    Add a new interaction or update an existing one.
    """
    inter = Interaction(source=source, target=target, interaction=interaction, references=references, weight=weight)
    try:
        inter.is_valid()
        db.session.add(inter)
        db.session.commit()
        return inter
    except ValidationError as e:
        db.session.rollback()
        print(f"Validation error for interaction {source}-{target}: {e}")
    except AlreadyExistsError as e:
        # If the interaction already exists, update it instead
        existing_inter = Interaction.query.filter_by(source=source, target=target).first()
        try:
            existing_inter.update(inter)
            db.session.commit()
            return existing_inter
        except ValidationError as e:
            db.session.rollback()
            print(f"Validation error while updating interaction {source}-{target}: {e}")
    except Exception as e:
        db.session.rollback()
        print(f"Error processing interaction {source}-{target}: {e}")
    return None
