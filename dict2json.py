# -*- coding: utf-8 -*-

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

