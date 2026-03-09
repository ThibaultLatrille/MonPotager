import re
import polars as pl
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import *


# Function to load reference names from paut_references.csv
def load_reference_names():
    # Read paut_references.csv using polars
    df = pl.read_csv('static/database/paut_references.csv', encoding='utf-8')

    print("Loading reference names from paut_references.csv...")
    print(f"Columns in paut_references.csv: {df.columns}")

    # Create a dictionary mapping reference IDs to reference names
    reference_map = {}
    for row in df.to_dicts():
        # The column names are different than expected
        # 'Pages internet' contains the ID
        # '' (empty string) contains the reference name
        ref_id = row.get('Pages internet', '')
        ref_name = row.get('', '')

        # Skip header rows and empty rows
        if ref_id and ref_name and ref_id != 'id' and ref_id != 'Ouvrages' and ref_id != 'Outlis et applications':
            # Convert 'à faire' to numeric ID if possible, otherwise skip
            if ref_id == 'à faire' or '(' in ref_id:
                continue

            try:
                # Try to convert to integer to ensure it's a valid ID
                int(ref_id)
                reference_map[str(ref_id)] = f"\'{ref_name}\'"
            except ValueError:
                # Skip if not a valid numeric ID
                continue
    return reference_map


# Dictionary to map interaction types
interaction_mapping = {
    '+': 'pos',
    '-': 'neg'
}

# Dictionary to map categories
category_mapping = {
    'Vegetable': 'Légume',
    'Fruit': 'Fruit',
    'Medicinal, Aromatic Plants, Flowers & Others': 'Arômate',
    'Vegetables': 'Légume',
    'Fruits': 'Fruit',
    'Shrubs & Berries': 'Fruit',
    'Trees (woody perennials)': 'Arbres',
    'Cereals': 'Céréale'
}


def clean_name(name):
    # Remove text between parentheses and clean up the name
    name = re.sub(r'\([^)]*\)', '', name)
    # Remove special characters and extra spaces
    name = re.sub(r'[&…]', ' ', name)
    # Strip whitespace and capitalize
    # Remove any double spaces in the name
    name = re.sub(r'\s+', ' ', name)
    # Replace "Petits pois" with "pois"
    if 'petits pois' in name.lower():
        name = name.lower().replace('petits pois', 'pois')
    if "chou brocoli" in name.lower():
        name = name.lower().replace('chou brocoli', 'brocoli')
    return name.strip().capitalize()


def clean_species_data():
    # Read paut_especes.csv using polars
    df = pl.read_csv('static/database/paut_especes.csv', encoding='utf-8')

    # Process each row
    for row in df.to_dicts():
        # Get French name and clean it
        french_name = str(row.get('Crop_fr', '')).strip()
        if french_name == 'None':
            print(f"Skipping row due to empty French name: {row}")
            continue

        latin_name = str(row.get('Latin_name', '')).strip()
        if not latin_name:
            latin_name = "nom  latin  non  trouvé"

        # Map the category
        crop_type_rp = str(row.get('Crop_type_RP', '')).strip()
        crop_type_pennington = str(row.get('Crop_type_Pennington_2009', '')).strip()
        raw_category = crop_type_rp or crop_type_pennington
        category = category_mapping.get(raw_category, 'Légume')  # Default to 'Légume' if no mapping found

        # Create a normalized name for associations (lowercase)
        common_name = clean_name(french_name).lower()
        taxonomy = row.get('Crop_family', '').strip()
        add_or_update_specie(common_name=common_name, category=category, taxonomy=taxonomy,
                             latin_name=latin_name, name=common_name)


def clean_associations_data():
    # Read paut_associations.csv using polars
    df = pl.read_csv('static/database/paut_associations.csv', encoding='utf-8')
    # Group by crop1, crop2, and source to remove duplicates
    # Aggregate to keep the majority type (pos/neg)
    unique_associations = df.group_by(['crop1', 'crop2', 'source']).agg(
        pl.col('type').mode().first().alias('type'),
        pl.col('Sens').mode().first().alias('Sens'),
        pl.col('Reason').mode().first().alias('Reason')
    ).sort(['crop1', 'crop2'])
    print(f"Original associations count: {len(df)}")
    print(f"Unique associations count after collapsing: {len(unique_associations)}")
    # Load reference names
    reference_map = load_reference_names()

    # Process each row
    for row in unique_associations.to_dicts():
        source_raw = row.get('crop1', '').strip()
        target_raw = row.get('crop2', '').strip()
        interaction_type = str(row.get('type', '')).strip()

        # Skip if any of the required fields is empty
        if not source_raw or not target_raw or not interaction_type:
            print(f"Skipping row due to empty fields: {row}")
            continue

        # Clean and map source and target names
        source = clean_name(source_raw).lower()
        target = clean_name(target_raw).lower()

        interaction = interaction_mapping[interaction_type]

        # Get the source number and look up the reference name
        source_num = str(row.get('source', '')).strip()
        reference_name = reference_map.get(source_num, f"une autre source ({source_num})")
        reference = f"{interaction_forward[interaction]} d'après {reference_name}"

        direction = str(row.get('sens', '')).strip()
        if direction == '':
            add_or_update_interaction(source=source, target=target, interaction=interaction,
                                      references=reference)
            add_or_update_interaction(source=target, target=source, interaction=interaction,
                                      references=reference)
        elif direction[0] == '1' and direction[-1] == '2':
            add_or_update_interaction(source=source, target=target, interaction=interaction,
                                      references=reference)
        elif direction[0] == '2' and direction[-1] == '1':
            add_or_update_interaction(source=target, target=source, interaction=interaction,
                                      references=reference)


def main():
    with app.app_context():
        print("Dropping existing database...")
        drop_db()
        clean_species_data()
        print(f"The database contains {Specie.query.count()} species.")
        clean_associations_data()
        print(f"The database contains {Interaction.query.count()} associations.")

        negative_interactions = Interaction.query.filter(Interaction.weight <= 0).count()
        print(f"The database contains {negative_interactions} interactions with 0 or negative weight.")
        prune_associations()
        print(f"The database contains {Interaction.query.count()} associations after pruning.")
        save_db_as_csv("static/database/paut_formatted_especes.csv",
                       "static/database/paut_formatted_associations.csv")


if __name__ == "__main__":
    main()
