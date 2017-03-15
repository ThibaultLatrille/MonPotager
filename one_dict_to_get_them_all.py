import os
#set directory where all files for dictionaries are
os.chdir("/Users/thibaultlorin/Desktop/ecolostyle/Michel/potageome/")

#import useful dict
from dico_appartenance import appartenance
from dico_interaction_plantes import interaction_plante
from dico_plantes_categories import plantes, categories




#Le résultat final qu'on veut

#Carotte\légume|favorise|Poireau\légume
#Carotte\légume|favorise|Poireau\légume
#Carotte\légume|favorise|Poireau\légume
#Carotte\légume|favorise|Poireau\légume
#Carotte\légume|favorise|Poireau\légume
#Carotte\légume|favorise|Poireau\légume
#Carotte\légume|favorise|Poireau\légume


#principe du code
#pour chaque interaction dans le dico interaction_plantes
#	récupérer le premier terme
#	récupérer le nom de l espèce dans le dictionnaire plantes 
#	récupérer son type dans appartenance et la catégorie dans categories
#	écrire "nom|type"
#	idem pour le deuxième terme
#	pour le troisième:
#		si 1: favorise
#		si -1: défavorise
#		si 2: attire
#		si -2: est nuisible à
#		si -3: repousse


f = open('interactions_comprehensibles.txt', 'w')

#verify that in the dictionary the order is good with the nuisible being in second

for i in range (0,len(interaction_plante)):
    if interaction_plante[i][2] == 1:
        f.write(plantes[interaction_plante[i][0]]+"\\"+categories[appartenance[interaction_plante[i][0]]]+"|favorise|"+plantes[interaction_plante[i][1]]+"\\"+categories[appartenance[interaction_plante[i][1]]]+"\n")
    elif interaction_plante[i][2] == -1:
        f.write(plantes[interaction_plante[i][0]]+"\\"+categories[appartenance[interaction_plante[i][0]]]+"|défavorise|"+plantes[interaction_plante[i][1]]+"\\"+categories[appartenance[interaction_plante[i][1]]]+"\n")
    if interaction_plante[i][2] == -2:
        f.write(plantes[interaction_plante[i][1]]+"\\"+categories[appartenance[interaction_plante[i][1]]]+"|nuit à|"+plantes[interaction_plante[i][0]]+"\\"+categories[appartenance[interaction_plante[i][0]]]+"\n")
    if interaction_plante[i][2] == 2:
        f.write(plantes[interaction_plante[i][1]]+"\\"+categories[appartenance[interaction_plante[i][1]]]+"|attire|"+plantes[interaction_plante[i][0]]+"\\"+categories[appartenance[interaction_plante[i][0]]]+"\n")
    if interaction_plante[i][2] == -3:
        f.write(plantes[interaction_plante[i][0]]+"\\"+categories[appartenance[interaction_plante[i][0]]]+"|repousse|"+plantes[interaction_plante[i][1]]+"\\"+categories[appartenance[interaction_plante[i][1]]]+"\n")
    

f.close()
