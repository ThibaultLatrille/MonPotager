*UN POINT SUR LES FICHIERS*

- dico_plantes_categories.py : identifiants des espèces et des catégories
- dico_appartenance.py : liste des espèces et la catégorie à laquelle elles appartiennent
- dico_interaction_plantes.py : liste avec les identifiants des espèces et le type d'interactions :
	1 : interaction favorable entre les plantes (exemple : (a,b,1) : a est favorable à b )
	-1 : interaction défavorable entre les plantes
	2 : la plante attire l'auxiliaire
	-2 : la plante/l'auxiliaire repousse le nuisible


- dict2json.py : fichier python qui permet d'obtenir un fichier javascript à partir des dictionnaires contenus dans les fichiers précédents.
USAGE : 
cd /path/to/potageome/
python dict2json.py   #génère le fichier data.js

- potageome.py : fichier python qui permet de remplir le template potageome.html en utilisant les données contenus dans les dictionnnaires :
cd /path/to/potageome/
python potageome.py   #génère le fichier potageome_rendered.html

- potageome_rendered.html : le fichier qui permet d'afficher le graphe



