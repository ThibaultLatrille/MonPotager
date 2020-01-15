import wikipedia
from Bio import Entrez
import requests
from bs4 import BeautifulSoup


def find_latin_name(nom_fr):
    """
    Fonction permettant à partir d'un nom commun d'espèce en français de ressortir un dictionnaire avec pour clé le nom commun et comme valeurs:
    - le nom commun français
    - le lien wikipedia de ce nom commun
    - son rang taxonomique
    - le nom latin
    """

    global u
    dico_fr = dict()
    wikipedia.set_lang("fr")
    key = nom_fr
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

    requete = requests.get(url)
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")
    if soup.find("div", {"class": "center taxobox_classification"}) is None:
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
    if soup.find("p", {"class": "bloc"}) is None:
        taxon = "taxon non trouvé"
    else:
        taxon = soup.find("p", {"class": "bloc"}).text

    # création du dictionnaire de sortie
    dico_fr[key] = [key, url, taxon, nom_latin]
    return dico_fr


def find_tax_id(dico_fr):
    """
    Cette fonction prend en entré un dictionnaire ayant pour clé le nom commmun français et comme valeur:
    le nom commun français, le lien wikipedia, le rang taxonomique et le nom latin.

    Cette fonction rajoute  à la fin des valeurs le taxID qui a été trouvé en consultant l'API du NCBI.
    """
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
