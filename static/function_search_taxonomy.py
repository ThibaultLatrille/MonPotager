# Package permettant d'utiliser l'API de wikipedia.
import wikipedia
# Package permettend d'utiliser l'API du NCBI.
from Bio import Entrez

# package permettant de lire et d'écrire dans un fichier csv.
import csv

# package de base pour lire les csv
import os
import csv

# package permettant de lire des page html et de les parser
import requests
from bs4 import BeautifulSoup


def findTaxonomyMany(dico_fr):
    ''' Fonction permettant à partir d'un dictionnaire ayant pour clé et valeur des noms commun français de retourner un dictionnaire avec pour clé les noms communs
    français et comme valeurs:
    -le nom commun français
    -le lien wikipedia
    -le rang taxonomique (trouvé sur wikipedia)
    -le nom latin (trouvé sur wikipedia)
    -le taxID (trouvé sur le site du NCBI)
    '''

    # partie recherchant le nom_latin et le rang taxonomique sur wikipedia.
    wikipedia.set_lang("fr")

    for key in dico_fr.keys():
        search = wikipedia.search(key)
        if search == list():
            continue
        search = search[0]
        wiki = wikipedia.WikipediaPage(search)
        url = wiki.url
        requete = requests.get(url)
        page = requete.content
        soup = BeautifulSoup(page, features="lxml")
        if soup.find("div", {"class": "center taxobox_classification"}) == None:
            nom_latin = "nom latin non trouvé"
        else:
            nom_latin = soup.find("div", {"class": "center taxobox_classification"}).text
        for count, i in enumerate(nom_latin):
            u = int()
            if count == 0:
                continue
            elif i == " ":
                continue
            elif i == "'":
                continue
            elif i == ".":
                continue
            elif i.upper() == i:
                u = count
                break
            else:
                u = 20
        nom_latin = nom_latin[:u]
        if soup.find("p", {"class": "bloc"}) == None:
            taxon = "taxon non trouvé"
        else:
            taxon = soup.find("p", {"class": "bloc"}).text
        dico_fr[key] = key, url, taxon, nom_latin

    # partie cherchant le taxID dans la base du NCBI à partir
    dico = dict()
    for key, value in dico_fr.items():
        value = list(value)
        Entrez.email = "theophile.tesseraud@gmail.com"  # Always tell NCBI who you are
        if value[3] == "nom latin non trouvé":
            value.append(" ")
            dico[key] = value
            continue
        handle = Entrez.esearch(db="taxonomy", term=value[3])
        record = Entrez.read(handle)
        if len(record["IdList"]) == 0:
            value.append(" ")
            dico[key] = value
            continue
        taxID = record["IdList"][0]
        taxID = str(taxID)
        value.append(taxID)
        dico[key] = value
    return dico


def findLatin_name(nom_fr):
    '''
    Fonction permettant à partir d'un nom commun d'espèce en français de ressortir un dictionnaire avec pour clé le nom commun et comme valeurs:
    - le nom commun français
    - le lien wikipedia de ce nom commun
    - son rang taxonomique
    - le nom latin
    '''

    dico_fr = dict()
    wikipedia.set_lang("fr")
    key = nom_fr
    # effectue une recherche sur wikipedia et récupère l'url de la page
    search = wikipedia.search(nom_fr)
    if search == list():
        taxon = "taxon non trouvé"
        nom_latin = "nom latin non trouvé"
        url = "https://fr.wikipedia.org/"
        dico_fr[key] = [key, url, taxon, nom_latin]
        return dico_fr

    search = search[0]
    wiki = wikipedia.WikipediaPage(search)
    url = wiki.url

    # récupère le nom latin et le rang taxonimuque en cherchant des balises sépcifiques de la page wikipedia via un parser.
    requete = requests.get(url)
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")
    if soup.find("div", {"class": "center taxobox_classification"}) == None:
        nom_latin = "nom latin non trouvé"
    else:
        nom_latin = soup.find("div", {"class": "center taxobox_classification"}).text
    for count, i in enumerate(nom_latin):
        u = int()
        if count == 0:
            continue
        elif i == " ":
            continue
        elif i == "'":
            continue
        elif i == ".":
            continue
        elif i.upper() == i:
            u = count
            break
        else:
            u = 20
    nom_latin = nom_latin[:u]
    if soup.find("p", {"class": "bloc"}) == None:
        taxon = "taxon non trouvé"
    else:
        taxon = soup.find("p", {"class": "bloc"}).text

    # création du dictionnaire de sortie
    dico_fr[key] = [key, url, taxon, nom_latin]
    return dico_fr


def findTaxID(dico_fr):
    '''
    Cette fonction prend en entré un dictionnaire ayant pour clé le nom commmun français et comme valeur:
    le nom commun français, le lien wikipedia, le rang taxonomique et le nom latin.

    Cette fonction rajoute  à la fin des valeurs le taxID qui a été trouvé en consultant l'API du NCBI.
    '''
    dico = dict()
    for key, value in dico_fr.items():
        value = list(value)
        Entrez.email = "theophile.tesseraud@gmail.com"  # Always tell NCBI who you are
        if value[3] == "nom latin non trouvé":
            value.append("")
            dico[key] = value
            return dico
        handle = Entrez.esearch(db="taxonomy", term=value[3])
        record = Entrez.read(handle)
        if len(record["IdList"]) == 0:
            value.append(" ")
            dico[key] = value
            return dico
        taxID = record["IdList"][0]
        taxID = str(taxID)
        value.append(taxID)
        dico[key] = value
    return dico
