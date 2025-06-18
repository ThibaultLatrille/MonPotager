from app import *

# The source will be merged into the target
species_to_merge = [
    ("achillée", "achillée millefeuille"),
    ("céleri", "céleris"),
    ("céleri branche", "céleris"),
    ("céleri-rave", "céleris"),
    ("cerise", "cerisier"),
    ("fraise", "fraisier"),
    ("framboise", "framboisier"),
    ("groseille", "groseillier"),
    ("haricot", "haricots"),
    ("haricot vert", "haricots"),
    ("haricot à ecosser et demi-secs", "haricots"),
    ("haricot de guar", "haricots"),
    ("laurier-sauce", "laurier sauce"),
    ("poire", "poirier"),
    ("poires d'automne", "poirier"),
    ("poires d'ete autres", "poirier"),
    ("poires d'hiver", "poirier"),
    ("poires jules guyot", "poirier"),
    ("poires william's", "poirier"),
    ("pomme", "pommier"),
    ("pomme golden", "pommier"),
    ("pomme granny smith", "pommier"),
    ("pomme de table autres", "pommier"),
    ("prune", "prunier"),
    ("prunes autres", "prunier"),
    ("pêche", "pêcher"),
    ("féverole", "fève fèverole")
]

# Species to remove
species_to_remove = [
    "agrumes",
    "arbres fruitiers"
]

def main():
    with app.app_context():
        print("Dropping existing database...")
        drop_db()

        # Populate database with initial data
        populate_db("static/database/paut_formatted_especes.csv",
                    "static/database/paut_formatted_associations.csv")
        print(f"The db contains n={Specie.query.count()} and m={Interaction.query.count()} from paut formatted.")

        # Add additional data
        populate_db("static/database/especes_v2.csv",
                    "static/database/associations.csv")
        print(f"The db contains n={Specie.query.count()} and m={Interaction.query.count()} after merge.")

        # Merge similar species
        print("\nMerging similar species...")
        for source, target in species_to_merge:
            merge_species(source, target)

        # Remove unwanted species
        print("\nRemoving unwanted species...")
        for species_name in species_to_remove:
            remove_species(species_name)

        # Prune database
        print(f"The db contains n={Specie.query.count()} and m={Interaction.query.count()} before pruning.")
        prune_db()
        print(f"The db contains n={Specie.query.count()} and m={Interaction.query.count()} after pruning.")
        update_ncbi_wiki()
        # Save final data to CSV
        save_db_as_csv("static/database/merged_especes.csv",
                       "static/database/merged_associations.csv")


if __name__ == "__main__":
    main()
