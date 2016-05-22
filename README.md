*UN POINT SUR LES FICHIERS*

- dico_plantes_categories.py : identifiants des espèces et des catégories
- dico_appartenance.py : liste des espèces et la catégorie à laquelle elles appartiennent
- dico_interaction_plantes.py : liste avec les identifiants des espèces et le type d'interactions :
	1 : interaction favorable entre les plantes (exemple : (a,b,1) : a est favorable à b )
	-1 : interaction défavorable entre les plantes
	2 : la plante attire l'auxiliaire
	-2 : la plante/l'auxiliaire repousse le nuisible


- dict2json.py : fichier python qui permet d'obtenir un fichier json à partir des dictionnaires contenus dans les fichiers précédents.
USAGE : 
cd /path/to/potageome/
python dict2json.py   #génère le fichier potageome.json

- potageome.html : le fichier qui permet d'afficher le graphe



