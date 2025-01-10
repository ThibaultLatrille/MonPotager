 [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
 
 Mon Potager est une application permettant de simuler son potager en insérant les diverses espèces de fruits et légumes,
 et de savoir si les interactions seront favorables ou défavorables. Mon Potager permet également d'obtenir facilement des informations 
sur la façon dont un parasite peut être éliminé par des plants compagnes.

Le tableur en ligne qui initialise la base de données est ouvert aux suggestions, rendez-vous à :
 - [La base de données des espèces](https://docs.google.com/spreadsheets/d/1Wp_fomhElzCspAxgarp1BstonU0HGA_tNB_U2uNskw0/edit?usp=sharing#gid=537765681)
 - [La base de données des interactions](https://docs.google.com/spreadsheets/d/1Wp_fomhElzCspAxgarp1BstonU0HGA_tNB_U2uNskw0/edit?usp=sharing#gid=0537765681)

L'application est actuellement accessible sur [https://thibaultlatrille.github.io/MonPotager/](https://thibaultlatrille.github.io/MonPotager/).
L'application telle que déployée sur github n'a pas de back-end, et donc il n'est pas possible de rajouter de nouvelles espèces ou interactions à la base de données qui est donc statique, mais avec le code source disponible il est tout à fait possible de déployer sur heroku ou autre afin d'avoir sa propre base de données qui peut être mise à jour à la volée.

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
At this step, you may have to chose between either a blue or a red pill :pill:.

With the blue pill, simply build the docker container and run the server inside the docker container.

Or chose the red pill and install the requirements (Python3, PostgreSQL, _etc_).

Blue pill is prefered is you want minimal conflict with your local system and just run the server.
Red pill method is prefered if you plan to extensively use the application and tinker with the code.
The two pills are mutually not exclusive, no overdose had ever been observed (though no statistical study had been performed).

### 1.a. Blue pill - Docker
A installation of Docker is required, see https://docs.docker.com/install/.

In Ubuntu (>17.10) with snap pre-installed, one can simply install docker with: 
```
sudo snap install docker
```
Once installed, build and run the docker container with:
```
sh ./docker_build_run.sh 
```
Once this is done, MonPotager is up and running at [http://0.0.0.0:8000](http://0.0.0.0:8000)

To note, the local folder MonPotager is kept synced within the docker container, meaning file changes are propagated inside the docker container (and vice-versa).

### 1.b. Red pill - Installation on debian
Install the dependencies:
```
sudo apt install -qq -y python3 python3-dev python3-pip postgresql postgresql-client postgresql-contrib libpq-dev
```
Install python3 packages
```
pip3 install --user -r requirements.txt
```
Create role and database in PostgreSQL
```
sudo -u postgres psql --command "CREATE USER monpotager_user WITH CREATEDB PASSWORD 'password';"
sudo -u postgres psql --command "CREATE DATABASE monpotager_db OWNER monpotager_user;"
```
Define environnment variables.
These lines can an also be added to your _~/.bashrc_ if your want them to be loaded at startup.
```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://monpotager_user:password@localhost/monpotager_db"
export SEED_PATH="/seed_path_reset_all_db"
export SECRET_KEY_BASE="af686cd78d5d56cd7af6"
```
Migrate database and seed
```
python3 manage.py db upgrade
python3 -c 'import app; app.reset_db()'
```
Run server
```
python3 app.py
```
Once this is done, MonPotager is up and running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 2. Add features or debug in the python scripts
You made modifications this README.md, or you added new features.
You wish this work benefits to all (futur) users of MonPotager?
Please, feel free to open a [pull-request](https://github.com/ThibaultLatrille/MonPotager/pulls)

## License
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Voir [LICENSE.md](https://github.com/ThibaultLatrille/MonPotager/blob/master/LICENSE.md) pour plus d'informations.
