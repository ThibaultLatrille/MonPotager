*UN POINT SUR LES FICHIERS*

- dico_plantes_categories.py : identifiants des espèces et des catégories
- dico_appartenance.py : liste des espèces et la catégorie à laquelle elles appartiennent
- dico_interaction_plantes.py : liste avec les identifiants des espèces et le type d'interactions :
	1 : interaction favorable entre les plantes (exemple : (a,b,1) : a est favorable à b )
	-1 : interaction défavorable entre les plantes
	2 : la plante attire l'auxiliaire
	-2 : la plante/l'auxiliaire repousse le nuisible

- potageome.py : fichier python qui permet de remplir potageome_template.html en utilisant les données contenus dans les dictionnnaires :

### Installer les dependances

```
$ git clone https://github.com/tlorin/potageome
$ pip3 install --user libsass jinja2 jsmin
```

### Generer le fichier potageome.html 
 
```
$ cd potageome
$ python3 potageome.py
```

### To do
    - Afficher dans le potager le nombre d'interactions et le nombre de nuisibles
    - Pour chaque plante, indiquer le nombre d'interactions (positive et negative) et comment ajouter des interactions positives
    - Pour les nuisibles, le nombre d'interactions negative et comment attirer les nuisibles qui les repousse
    - Pour les auxiliaires, le nombre d'interactions positives avec les plantes, le nombre de nuisibles qu'il vire, et comment les attirer.
    - Dans la liste, degradé vert et rouge