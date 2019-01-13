 [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
 
 Mon Potager est une application permettant de simuler son potager en
 insérant les diverses espèces de fruits et légumes,
 et de savoir si les interactions seront favorables ou défavorables.
 
Mon Potager permet également d'obtenir facilement des informations 
sur la façon dont un parasite peut être éliminé par des plants compagnes.

L'application est actuellement accessible sur [https://monpotager.org](https://monpotager.org)

## Pour améliorer la base de données de MonPotager

Si la base de données (tableur en ligne ouverte aux suggestions) vous semble incomplète ou erronée, rendez-vous à :
 - [La base de donnes des espèces](https://docs.google.com/spreadsheets/d/1Wp_fomhElzCspAxgarp1BstonU0HGA_tNB_U2uNskw0/edit?usp=sharing#gid=537765681)
 - [La base de donnes des interactions](https://docs.google.com/spreadsheets/d/1Wp_fomhElzCspAxgarp1BstonU0HGA_tNB_U2uNskw0/edit?usp=sharing#gid=0537765681)

## Pour développer MonPotager en local (linux version)

### Installer les dépendances

```
$ git clone https://github.com/ThibaultLatrille/MonPotager
$ cd MonPotager
$ pip3 install --user -r requirements.txt
```

### Générer le fichier index.html 
 
```
$ python3 MonPotager.py
```

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Voir [LICENSE.md](https://github.com/ThibaultLatrille/MonPotager/blob/master/LICENSE.md) pour plus d'informations.