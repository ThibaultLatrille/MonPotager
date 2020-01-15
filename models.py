from app import db


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
    __table_args__ = (db.UniqueConstraint('source', 'target', name='source_target'),)

    def __init__(self, source, target, interaction, references):
        self.source = source
        self.target = target
        self.interaction = interaction
        self.references = references

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
