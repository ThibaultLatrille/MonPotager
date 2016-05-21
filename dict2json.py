# -*- coding: utf-8 -*-


from dico_appartenance import appartenance
from dico_interaction_plantes import interaction_plante
from dico_plantes_categories import plantes
from dico_plantes_categories import categorie



json = open("potageome.json","w")

json.write("{\n")
json.write(' "nodes":[\n')
json.write('    {"name":"Null","group":1},\n')

#nodes for json file
for key, values in appartenance.items():
	#print(key)
	#print(values)
	json.write(('\t{"name":"'+plantes[key]+'","group":'+str(values)+'},\n'))
	#print(plantes[key] + " est un/une " + categorie[values])


json.write('  ],\n')
json.write('  "links":[\n')
    


interaction_categorie = []
for plante_1, plante_2, bla in interaction_plante:
    interaction_categorie.append((appartenance[plante_1], appartenance[plante_2], bla ))


#links for html file
for plante_1, plante_2, bla in interaction_plante:
	json.write('\t{"source":'+str(plante_1)+',"target":'+str(plante_2)+',"value":'+str(bla)+'},\n')


json.write('  ]\n')
json.write('}')