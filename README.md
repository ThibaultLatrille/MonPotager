 [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
 
 Mon Potager est une application permettant de simuler son potager en insérant les diverses espèces de fruits et légumes,
 et de savoir si les interactions seront favorables ou défavorables. Mon Potager permet également d'obtenir facilement des informations 
sur la façon dont un parasite peut être éliminé par des plants compagnes.
L'application est actuellement accessible sur [http://monpotagerorg.herokuapp.com/](http://monpotagerorg.herokuapp.com/).

Le tableur en ligne qui initialise la base de données est ouvert aux suggestions, rendez-vous à :
 - [La base de données des espèces](https://docs.google.com/spreadsheets/d/1Wp_fomhElzCspAxgarp1BstonU0HGA_tNB_U2uNskw0/edit?usp=sharing#gid=537765681)
 - [La base de données des interactions](https://docs.google.com/spreadsheets/d/1Wp_fomhElzCspAxgarp1BstonU0HGA_tNB_U2uNskw0/edit?usp=sharing#gid=0537765681)


# For developers 

This repository gives the instructions to run the application on your local computer and start coding.
The instructions are meant for Linux/Unix/MacOS operating systems.
However a docker container is provided and a WindowsOS installation (not tested by the author) should in principle work too, at your own peril.

If problems and/or questions are encountered, feel free to [open issues](https://github.com/ThibaultLatrille/MonPotager/issues).

## 0. Local copy
Clone the repository and cd to the dir.
```
git clone https://github.com/ThibaultLatrille/MonPotager
cd MonPotager
```

## 1. Installation

Install the dependencies:
```
sudo apt install -qq -y python3 python3-dev python3-pip postgresql postgresql-client postgresql-contrib libpq-dev
```
Install python3 packages
```
pip3 install --user -r requirements.txt
```
Run server
```
python3 app.py
```
Once this is done, MonPotager is up and running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
To seed the database with the default data go to url [http://127.0.0.1:5000/seed](http://127.0.0.1:5000/seed), this will run the function `seed_db()` in `app.py` which will insert the data from into the database.

## 2. Add features or debug in the python scripts
You made modifications this README.md, or you added new features.
You wish this work benefits to all (futur) users of MonPotager?
Please, feel free to open a [pull-request](https://github.com/ThibaultLatrille/MonPotager/pulls)

## License
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Voir [LICENSE.md](https://github.com/ThibaultLatrille/MonPotager/blob/master/LICENSE.md) pour plus d'informations.
