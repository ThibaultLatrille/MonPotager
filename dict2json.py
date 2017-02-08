# -*- coding: utf-8 -*-

from dico_appartenance import appartenance
from dico_interaction_plantes import interaction_plante
from dico_plantes_categories import plantes
from dico_plantes_categories import categories

javascript = open("data.js", "w")

javascript.write("var graph = {\n")
# nodes for javascript file
javascript.write('\t"nodes":[\n')
javascript.write(",\n".join(['\t\t{"name":"'+plantes[key]+'","group":'+str(values)+'}' for key, values in appartenance.items()]))
javascript.write('\n\t],\n')
# links for html file
javascript.write('\t"links":[\n')
javascript.write(",\n".join(['\t\t{"source":'+str(plante_1)+',"target":'+str(plante_2)+',"value":'+str(inter)+'}' for plante_1, plante_2, inter in interaction_plante]))
javascript.write('\n\t]\n};')

javascript.write("\nvar groups = {\n")
javascript.write(",\n".join(['\t'+str(key)+':"'+str(values)+'"' for key, values in categories.items()]))
javascript.write('\n};')

javascript.close()

print("Javascript data file successfully written !")
