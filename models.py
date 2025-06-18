import csv
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

def clean_string(s: str) -> str:
    return ' '.join(s.strip().split()) if s else ""

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
            taxId = None
        self.name = clean_string(name)
        self.common_name = clean_string(common_name)
        self.category = clean_string(category)
        self.wiki = clean_string(wiki)
        self.taxonomy = clean_string(taxonomy)
        self.latin_name = clean_string(latin_name)
        self.TaxID = taxId
        self.NCBI = clean_string(NCBI)

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

def most_complete(s1: str, s2: str) -> str:
    if s1 == s2:
        return s1
    if len(s1) > len(s2):
        return s1
    return clean_string(s2)

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
                existing_specie.common_name = most_complete(existing_specie.common_name, common_name)
                existing_specie.category = most_complete(existing_specie.category, category)
                existing_specie.wiki = most_complete(existing_specie.wiki, wiki)
                existing_specie.taxonomy = most_complete(existing_specie.taxonomy, taxonomy)
                existing_specie.latin_name = most_complete(existing_specie.latin_name, latin_name)
                existing_specie.TaxID = TaxID if TaxID else existing_specie.TaxID
                existing_specie.NCBI = most_complete(existing_specie.NCBI, NCBI)
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
        if other.references in self.references:
            raise ValidationError(f"Les références de l'interaction {self.source} -> {self.target} sont déjà présentes : {self.references}")
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
        s = f"Interaction de {self.source} vers {self.target} : {interaction_forward[self.interaction].lower()} ({self.weight})\n"
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


def prune_species():
    # Remove species with no associations
    print("Pruning species...")
    species_with_associations = {assoc.source for assoc in db.session.query(Interaction).all()} | \
                                {assoc.target for assoc in db.session.query(Interaction).all()}
    all_species = db.session.query(Specie).all()
    for specie in all_species:
        if specie.name not in species_with_associations:
            db.session.delete(specie)
    db.session.commit()


def prune_associations():
    print("Pruning associations...")
    # Remove the associations with weight = 0, invert interaction with negative weight
    for assoc in db.session.query(Interaction).all():
        if assoc.weight == 0:
            db.session.delete(assoc)
        elif assoc.weight < 0:
            assoc.interaction = interactions[-reverse_interactions[assoc.interaction]]
            assoc.weight = -assoc.weight
            db.session.add(assoc)
    db.session.commit()


def prune_db():
    prune_associations()
    prune_species()


def drop_db():
    db.drop_all()
    db.create_all()
    db.session.query(Interaction).delete()
    db.session.commit()
    db.session.query(Specie).delete()
    db.session.commit()


def populate_db(especes_file, associations_file):
    print("Populating database...")
    with open(especes_file, 'r', newline='', encoding='utf-8') as csvfile:
        speciesreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(speciesreader)
        for line in speciesreader:
            add_or_update_specie(name=line[7], common_name=line[0], category=line[1],
                                 latin_name=line[4], wiki=line[2], taxonomy=line[3],
                                 TaxID=line[5], NCBI=line[6])

    with open(associations_file, 'r', newline='', encoding='utf-8') as csvfile:
        associationsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(associationsreader)
        for source, assoc, target, references, weight, _ in associationsreader:
            add_or_update_interaction(source=source, target=target,
                                      interaction=interactions[description_interactions[assoc]],
                                      references=references, weight=float(weight) if weight else 1.0)


def remove_species(species_name):
    print(f"Removing species '{species_name}'...")
    species = Specie.query.filter_by(name=species_name).first()
    if not species:
        print(f"Species '{species_name}' not found.")
        return False

    # Remove all interactions where species_name is the source
    for interaction in Interaction.query.filter_by(source=species_name).all():
        db.session.delete(interaction)

    # Remove all interactions where species_name is the target
    for interaction in Interaction.query.filter_by(target=species_name).all():
        db.session.delete(interaction)

    # Delete the species
    db.session.delete(species)
    try:
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(f"Error removing species: {e}")
        return False


def merge_species(source_name, target_name):
    print(f"Merging species '{source_name}' into '{target_name}'...")

    # Check if both species exist
    source_species = Specie.query.filter_by(name=source_name).first()
    target_species = Specie.query.filter_by(name=target_name).first()

    if not source_species or not target_species:
        print(f"Source species '{source_name}' or target species '{target_name}' not found.")
        return False

    # Update all interactions where source_name is the source
    source_interactions = Interaction.query.filter_by(source=source_name).all()
    for interaction in source_interactions:
        add_or_update_interaction(source=target_name, target=interaction.target, interaction=interaction.interaction,
                                  references=interaction.references, weight=interaction.weight)

    # Update all interactions where source_name is the target
    target_interactions = Interaction.query.filter_by(target=source_name).all()
    for interaction in target_interactions:
        add_or_update_interaction(source=interaction.source, target=target_name, interaction=interaction.interaction,
                                  references=interaction.references, weight=interaction.weight)
    db.session.commit()
    # Delete the source species
    return remove_species(source_name)


def save_db_as_csv(especes_file, associations_file):
    print("Saving database to CSV files...")
    with open(especes_file, 'w', newline='', encoding='utf-8') as csvfile:
        specieswriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        specieswriter.writerow(
            ['common_name', 'category', 'wiki', 'taxonomy', 'latin_name', 'TaxID', 'NCBI', 'name'])
        for sp in db.session.query(Specie).order_by(Specie.common_name).all():
            specieswriter.writerow(
                [sp.common_name, sp.category, sp.wiki, sp.taxonomy, sp.latin_name, sp.TaxID, sp.NCBI, sp.name])

    with open(associations_file, 'w', newline='', encoding='utf-8') as csvfile:
        associationswriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        associationswriter.writerow(
            ['espèce source', 'interaction', 'espèce cible', 'source', 'poids', "commentaire"])
        for assoc in db.session.query(Interaction).order_by(Interaction.source, Interaction.target,
                                                            Interaction.interaction).all():
            i = interaction_forward[assoc.interaction].lower()
            associationswriter.writerow([assoc.source, i, assoc.target, assoc.references, assoc.weight, ""])
