# Description

# Installation
Sous Linux (Debian / Ubuntu) :

```console
$ sudo -s
$ apt-get update
$ apt-get install install postgresql postgresql-contrib postgis
```

# Roadmap
* :heavy_check_mark: Choisir le système de base de données :arrow_forward: **PostgreSQL**
* :heavy_check_mark: Créer la base de données pour la gestion des plantes et des interactions
* :heavy_check_mark: Permettre la modification des données pour les utilisateurs identifiés. Inclure un système de validations
* :white_square_button: Organiser les connaissances acquises sur les jardins afin de valider ou d’invalider les interactions contenus dans la base de données / organiser des expérimentations d’associations de cultures dans les jardins
* :white_square_button: Permettre la création et la modification d'un potager avec gestion spatiale de celui-ci (y compris verticale)
* :heavy_check_mark: Importer **especes.csv** et **associations.csv** dans la base de données (se placer dans ce dossier et executer `python import.py`)
