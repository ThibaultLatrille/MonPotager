*UN POINT SUR LES FICHIERS*

- dico_plantes_categories.py : identifiants des espèces et des catégories
- dico_appartenance.py : liste des espèces et la catégorie à laquelle elles appartiennent
- dico_interaction_plantes.py : liste avec les identifiants des espèces et le type d'interactions :
	1 : interaction favorable entre les plantes (exemple : (a,b,1) : a est favorable à b )
	-1 : interaction défavorable entre les plantes
	2 : la plante attire l'auxiliaire
	-2 : la plante/l'auxiliaire repousse le nuisible

- MonPotager.py : fichier python qui permet de remplir MonPotager_template.html en utilisant les données contenus dans les dictionnnaires :

### Installer les dependances

```
$ git clone https://github.com/ThibaultLatrille/MonPotager
$ pip3 install --user libsass jinja2 jsmin
```

### Generer le fichier MonPotager.html 
 
```
$ cd MonPotager
$ python3 MonPotager.py
```

### To do
    - Pour les nuisibles, comment attirer les auxilliaire qui les repousses (filtre)
    - Smooth Zoom (et bouttons +/-)
    - Sauvegarder dans les cookies