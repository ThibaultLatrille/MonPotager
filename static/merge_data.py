from app import *


def main():
    with app.app_context():
        print("Dropping existing database...")
        drop_db()
        populate_db("static/database/paut_formatted_especes.csv",
                    "static/database/paut_formatted_associations.csv")
        print(f"The db contains n={Specie.query.count()} and m={Interaction.query.count()} from paut formatted.")
        populate_db("static/database/especes_v2.csv",
                    "static/database/associations.csv")
        print(f"The db contains n={Specie.query.count()} and m={Interaction.query.count()} after merge.")
        prune_db()
        print(f"The db contains n={Specie.query.count()} and m={Interaction.query.count()} after pruning.")
        save_db_as_csv("static/database/merged_especes.csv",
                       "static/database/merged_associations.csv")


if __name__ == "__main__":
    main()
