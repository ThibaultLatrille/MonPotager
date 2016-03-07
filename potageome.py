# -*- coding: utf-8 -*-


plantes = {1: "Carotte", 2: "Poireau", 3:"Ail", 4:"Haricot", 5:"Panais", 6:"Tomate", 7:"Pois", 8:"Poivron", 9:"Mâche", 10:"Concombre", 11:"Aneth", 12:"Pomme de terre", 13:"Oignon", 14:"Chou-fleur", 15:"Chou-rave", 16:"Chou rouge", 17:"Céleri", 18:"Betterave", 19:"Radis", 20:"Laitue", 21:"Radis", 22:"Courgette", 23:"Fenouil", #legumes
24:"Fraisier", #fruits
 25:"Aneth", 26:"Persil", 27:"Sarriette", 28:"Ciboulette", 29:"Cerfeuil", 30:"Basilic",  31:"Moutarde", 32:"Menthe", 33:"Mélisse citronnelle",#aromates
 34:"Tanaisie", 35:"Trèfle blanc", 36:"Bourrache", 37:"Soucis", 38:"Oeillets d'Inde",#fleurs
 39:"Limaces", 40:"Altises", 41:"Pucerons", 42:"Nématodes", 43:"Cochenilles", 44:"Mildiou", #nuisibles
 45:"Coccinelles", 46:"Carabe doré", 47:"Perce-oreille"} #auxiliaires


#à classer : piéride, mouche de la carotte et de l'oignon

categorie = {1: "Légume", 2: "Fruit", 3:"Arômate", 4:"Fleur", 5:"Nuisible", 6:"Auxiliaire", 7:"Céréale"}

appartenance = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1,
24:2, 
25:3, 26:3, 27:3, 28:3, 29:3, 30:3, 31:3, 32:3, 33:3,
34:4, 35:4, 36:4, 37:4, 38:4,
39:5, 40:5, 41:5, 42:5, 43:5, 44:5,
45:6, 47:6, 48:6}


#nodes for html file
for key, values in appartenance.items():
	#print(key)
	#print(values)
	print('{"name":"'+plantes[key]+'","group":'+str(values)+'}')
	#print(plantes[key] + " est un/une " + categorie[values])




interaction_categorie = []
for plante_1, plante_2, bla in interaction_plante:
    interaction_categorie.append((appartenance[plante_1], appartenance[plante_2], bla ))


#links for html file
for plante_1, plante_2, bla in interaction_plante:
	print('{"source":'+str(plante_1)+',"target":'+str(plante_2)+',"value":'+str(bla)+'}')




Il contient exactement tout, il suffit de remplacer la ligne 
".style("stroke-width", function(d) { return Math.sqrt(d.value); });"
par 
".style("fill", function(d) { return color(d.value); }) "
pour qu'il colorie les arrêtes de couleur différentes !!!!!

Et les données en entrée sont parfaites pour nous, ca va être de la tarte !!!

Après une fois qu'on aura mit ça sur pied, on s'occupera de mettre les noms et de rendre ca design, mais chaque chose en son temps ;-)
 

Voilou, du coup ton expérience de pro me conseille de commencer par laquelle du coup ? Et est-ce que la matrice comme je pense la faire irait ou pas ? En particulier je sais pas trop comment distinguer les cases de différents types ^^

 

Cimer brow !

Je t'en prie, ça m'a prit un peu de temps de répondre, mais je sais que le résultat va être trop stylé. D'ailleurs la chercheuse dans mon bureau attend de voir ton résultat avec impatience. N'hésites pas à me demander.
Je sais que la façon que je te propose est pas pratique pour la rédaction au départ, mais crois moi plus tard quand tu seras dans le code, ou quand tu voudra changer les noms, fusionner ou ajouter des catégories ou des plantes, tu fera des bisous au toi du passé qui avait pris le temps de bien penser au design des datas.
 