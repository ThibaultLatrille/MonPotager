# -*- coding: utf-8 -*-

interaction_plante = [(1,2,1), #carotte-poireau
(1,3,1), #carotte-ail
(1,13,1), #carotte-oignon
(1,49,1), #carotte-échalote
(1,28,1), #carotte-ciboulette
(1,18,1), #carotte-betterave
(1,7,1), #carotte-pois
(1,19,1), #carotte-radis
(1,20,1), #carotte-laitue
(1,50,1), #carotte-roquette
(1,5,1), #carotte-panais
(1,6,1), #carotte-tomate
(1,4,1), #carotte-haricot
(1,50,1), #carotte-salsifis
(1,52,1), #carotte-piment
(1,53,1), #carotte-lin
(1,54,1), #carotte-romarin
(1,55,1), #carotte-sauge
(1,56,1), #carotte-absinthe
(1,57,1), #carotte-coriandre
(1,25,-1), #carotte-aneth
(1,58,-1), #carotte-maïs
(1,64,-1), #carotte-bette
(1,46,1), #carotte-carabe
(1,59,-1), #carotte cultivée-carotte sauvage
(59,60,1), #carotte sauvage-choux
(2,1,1), #poireau-carotte
(2,17,1), #poireau-céleri
(2,61,1), #poireau-asperge
(2,20,1), #poireau-laitue
(2,9,1), #poireau-mâche
(2,6,1), #poireau-tomate
(2,23,1), #poireau-fenouil
(2,62,1), #poireau-artichaut
(2,31,1), #poireau-moutarde
(2,63,1), #poireau-cresson
(2,64,-1), #poireau-bette
(2,18,-1), #poireau-betterave
(2,60,-1), #poireau-choux
(2,4,-1), #poireau-haricot
(2,26,-1), #poireau-persil
(2,7,-1), #poireau-pois
(2,24,1), #poireau-fraisier
(3,65,1), #ail-pêcher
(3,66,1), #ail-pommier
(3,67,1), #ail-poirier
(3,68,1), #ail-prunier
(3,69,1), #ail-chicorée
(3,70,1), #ail-pissenlit
(3,71,1), #ail-topinambour
(3,6,1), #ail-tomate
(3,24,1), #ail-fraisier
(3,72,1), #ail-framboisier
(3,73,1), #ail-rosier
(3,60,-1), #ail-chou
(3,12,-1), #ail-pomme de terre
(3,4,-1), #ail-haricot
(3,7,-1), #ail-pois
(3,37,-1), #ail-souci
(3,62,-1), #ail-artichaut
(3,61,-1), #ail-asperge
(4,58,1), #haricot-maïs
(4,74,1), #haricot-potiron
(4,60,1), #haricot-choux
(4,75,1), #haricot-melon
(4,76,1), #haricot-pastèque
(4,1,1), #haricot-carotte
(4,17,1), #haricot-céleri
(4,77,1), #haricot-concombre
(4,12,1), #haricot-pomme de terre
(4,78,1), #haricot-épinard
(4,20,1), #haricot-laitue
(4,36,1), #haricot-bourrache
(4,79,1), #haricot-capucine
(4,80,1), #haricot-sarriette annuelle
(4,81,1), #haricot-tournesol
(4,56,1), #haricot-absinthe
(4,2,-1), #haricot-poireau
(4,3,-1), #haricot-ail
(4,49,-1), #haricot-échalote
(4,28,-1), #haricot-ciboulette
(4,13,-1), #haricot-oignon
(4,23,-1), #haricot-fenouil
(4,7,-1), #haricot-pois
(4,22,-1), #haricot-courgette
(4,82,-1), #haricot-kiwi
(5,19,1), #panais-radis
(5,18,1), #panais-betterave
(5,15,1), #panais-chou rave
(5,13,1), #panais-oignon
(5,20,-1), #panais-laitue
(6,83,1), #tomate-rosier d'inde
(6,84,1), #tomate-oeillets d'Inde
(6,85,1), #tomate-cosmos
(6,86,1), #tomate-camomille allemande
(6,60,1), #tomate-choux
(6,87,1), #tomate-géranium
(6,88,1), #tomate-inule visqueuse
(6,76,1), #tomate-pastèque
(6,10,1), #tomate-concombre
(6,73,1), #tomate-rosier
(6,1,1), #tomate-carotte
(6,78,1), #tomate-épinard
(6,4,1), #tomate-haricot
(6,13,1), #tomate-oignon
(6,26,1), #tomate-persil
(6,2,1), #tomate-poireau
(6,20,1), #tomate-laitue
(6,12,-1), #tomate-pomme de terre
(6,81,-1), #tomate-tournesol
(6,44,-1), #tomate-mildiou
(6,18,-1), #tomate-betterave
(6,23,-1), #tomate-fenouil
(6,24,-1), #tomate-fraisier
(89,42,-1), #ricin-nématodes
(89,90,-1), #ricin-doryphores
(7,89,1), #pois-ricin
(7,12,1), #pois-pomme de terre
(7,57,1), #pois-coriandre
(7,13,-1), #pois-oignon
(7,3,-1), #pois-ail
(7,49,-1), #pois-échalote
(7,2,-1), #pois-poireau
(7,26,-1), #pois-persil
(8,6,1), #poivron-tomate
(8,1,1), #poivron-carotte
(8,60,1), #poivron-choux
(9,91,-1), #mâche-amarante
(9,82,-1), #mâche-kiwi
(9,60,-1), #mâche-choux
(9,2,1), #mâche-poireau
(9,13,1), #mâche-oignon
(9,24,1), #mâche-fraisier
(9,35,1), #mâche-trèfle
(9,74,1), #mâche-potiron
(10,6,1), #tomate-concombre
(12,82,1), #pomme de terre-kiwi
(12,61,1), #pomme de terre-asperge
(12,86,1), #pomme de terre-camomille allemande
(86,45,1), #camomille allemande-coccinelles
(86,42,-1), #camomille allemande-nématodes
(12,79,1), #pomme de terre-capucine
(12,17,1), #pomme de terre-céleri
(12,92,1), #pomme de terre-chanvre
(12,60,1), #pomme de terre-choux
(12,93,1), #pomme de terre-ciboulette chinoise
(12,57,1), #pomme de terre-coriandre
(12,77,1), #pomme de terre-fève
(12,94,1), #pomme de terre-féverole
(12,4,1), #pomme de terre-haricot
(12,95,1), #pomme de terre-morelle de balbis
(12,7,1), #pomme de terre-pois
(12,21,1), #pomme de terre-radis
(12,37,1), #pomme de terre-souci
(95,90,-1), #morelle de balbis-doryphores
(95,42,-1), #morelle de balbis-nématodes
(21,63,1), #radis-cresson
(21,96,1), #radis-genêt
(21,29,1), #radis-cerfeuil
(21,5,1), #radis-panais
(21,1,1), #radis-carotte
(21,7,1), #radis-pois
(21,10,1), #radis-concombre
(21,11,1), #radis-cornichon
(21,78,1), #radis-épinard
(21,4,1), #radis-haricot
(21,17,1), #radis-céleri-rave
(21,12,1), #radis-pomme de terre
(21,6,1), #radis-tomate
(21,13,1), #radis-oignon
(21,28,-1), #radis-ciboulette
(21,60,-1), #radis-choux
(13,1,1), #oignon-carotte
(13,20,1), #oignon-laitue
(13,9,1), #oignon-mâche
(13,21,1), #oignon-radis
(13,35,1), #oignon-trèfle
(13,4,-1), #oignon-haricot
(13,7,-1), #oignon-pois
(13,82,-1), #oignon-kiwi
(13,41,-2), #oignon-pucerons
(13,13,-1), #oignon-oignon       ATTENTION, AUTOINTERACTION
(60,,-1), #choux-chicorée
(60,,-1), #choux-fraisier
(60,,-1), #choux-poireau
(60,,-1), #choux-radis
(60,,-1), #choux-maïs
(60,,-1), #choux-mâche
(60,,-1), #choux-fenouil
(60,,-1), #choux-cresson
(60,,-1), #choux-courgette
(60,,-1), #choux-origan
(60,,-1), #choux-piment
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #
# (,,), #


plantes = {
 #legumes
 1:"Carotte",
 2:"Poireau",
 3:"Ail",
 4:"Haricot",
 5:"Panais",
 6:"Tomate",
 7:"Pois",
 8:"Poivron",
 9:"Mâche",
 10:"Concombre",
 11:"Cornichon",
 12:"Pomme de terre",
 13:"Oignon",
 60:"Choux",
 14:"Chou-fleur",
 15:"Chou-rave",
 16:"Chou-rouge",
 17:"Céleri",
 18:"Betterave",
 19:"Radis",
 20:"Laitue",
 21:"Radis",
 22:"Courgette",
 23:"Fenouil",
 49:"Echalote",
 50:"Roquette",
 51:"Salsifis",
 58:"Maïs",
 61:"Asperge",
 62:"Artichaut",
 63:"Cresson",
 64:"Bette",
 69:"Chicorée",
 71:"Topinambour",
 74:"Potiron",
 77:"Fève",
 78:"Epinard",
 94:"Féverole",
 #fruits
 24:"Fraisier",
 65:"Pêcher",
 66:"Pommier",
 67:"Poirier",
 68:"Prunier",
 72:"Framboisier",
 75:"Melon",
 76:"Pastèque",
 82:"Kiwi",
 #aromates
 25:"Aneth",
 26:"Persil",
 27:"Sarriette",
 28:"Ciboulette",
 29:"Cerfeuil",
 30:"Basilic",
 31:"Moutarde",
 32:"Menthe",
 33:"Mélisse citronnelle",
 52:"Piment",
 54:"Romarin",
 55:"Sauge",
 56:"Absinthe",
 57:"Coriandre",
 80:"Sarriette",
 93:"Ciboulette chinoise",
 #fleurs
 34:"Tanaisie",
 35:"Trèfle blanc",
 36:"Bourrache",
 37:"Soucis",
 38:"Oeillets d'Inde",
 48:"Achillée millefeuille",
 59:"Carotte sauvage",
 70:"Pissenlit",
 73:"Rosier",
 79:"Capucine",
 81:"Tournesol",
 83:"Rosier d'Inde",
 84:"Oeillets d'Inde",
 85:"Cosmos",
 86:"Camomille allemande",
 87:"Géranium",
 88:"Inule visqueuse",
 89:"Ricin",
 91:"Amarante",
 92:"Chanvre",
 95:"Morelle de Balbis",
 96:"Genêt",
 #nuisibles
 39:"Limaces",
 40:"Altises",
 41:"Pucerons",
 42:"Nématodes",
 43:"Cochenilles",
 44:"Mildiou",
 90:"Doryphores",
 #auxiliaires
 45:"Coccinelles",
 46:"Carabe doré",
 47:"Perce-oreille",
 #céréales
 53:"Lin"} 



appartenance = {
 #legumes
 1: 1,
 2: 1,
 3: 1,
 4: 1,
 5: 1,
 6: 1,
 7: 1,
 8: 1,
 9: 1,
 10: 1,
 11: 1,
 12: 1,
 13: 1,
 60:1,
 14: 1,
 15: 1,
 16: 1,
 17: 1,
 18: 1,
 19: 1,
 20: 1,
 21: 1,
 22: 1,
 23: 1,
 49:1,
 50:1,
 51:1,
 58:1,
 61:1,
 62:1,
 63:1,
 64:1,
 69:1,
 71:1,
 74:1,
 77:1,
 78:1,
 94:1,
 #fruits
 24:2,
 65:2,
 66:2,
 67:2,
 68:2,
 72:2,
 75:2,
 76:2,
 82:2,
 #aromates
 25:3,
 26:3,
 27:3,
 28:3,
 29:3,
 30:3,
 31:3,
 32:3,
 33:3,
 52:3,
 54:3,
 55:3,
 56:3,
 57:3,
 80:3,
 93:3,
 #fleurs
 34:4,
 35:4,
 36:4,
 37:4,
 38:4,
 48:4,
 59:4,
 70:4,
 73:4,
 79:4,
 81:4,
 83:4,
 84:4,
 85:4,
 86:4,
 87:4,
 88:4,
 89:4,
 91:4,
 92:4,
 95:4,
 96:4,
 #nuisibles
 39:5,
 40:5,
 41:5,
 42:5,
 43:5,
 44:5,
 90:5,
 #auxiliaires
 45:6,
 46:6,
 47:6,
 #céréales
 53:7}


categorie = {1: "Légume", 2: "Fruit", 3:"Arômate", 4:"Fleur", 5:"Nuisible", 6:"Auxiliaire", 7:"Céréale"}


#nodes for html file
for key, values in appartenance.items():
	#print(key)
	#print(values)
	print('{"name":"'+plantes[key]+'","group":'+str(values)+'},')
	#print(plantes[key] + " est un/une " + categorie[values])



interaction_categorie = []
for plante_1, plante_2, bla in interaction_plante:
    interaction_categorie.append((appartenance[plante_1], appartenance[plante_2], bla ))


#links for html file
for plante_1, plante_2, bla in interaction_plante:
	print('{"source":'+str(plante_1)+',"target":'+str(plante_2)+',"value":'+str(bla)+'},')

