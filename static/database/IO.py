def lecture_data(fichierCsv):
	''' Fonction permettant de lire le fichier espece.csv et de retourner un dictionnaire avec comme valeur et comme valeur les noms communs français'''
	liste_nom_commun=list()
	with open(fichierCsv, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			liste_nom_commun.append(row[2])
	del liste_nom_commun[0]
	
	dico_nom_commun=dict()
	for i in liste_nom_commun:
		dico_nom_commun[i]=i
	return(dico_nom_commun)
	
def generate_data(dico,fichier):
	''' Fonction qui permet de créer un fichier csv et de le remplir des valeurs contenus dans un dictionnaire incluant le nom commun français; le lien wikipedia;
	le rang taxomique, le nom latin et le taxID
	'''
	with open(fichier, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(['nom_commun']+ ['lien wikipedia']+['taxonomie']+['nom latin']+['TaxID'])
		for value in dico.values():
			spamwriter.writerow([value[0]]+[value[1]]+[value[2]]+[value[3]]+[value[4]])
			
def ecriture_data(dico):
	