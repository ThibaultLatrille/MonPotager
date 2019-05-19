import csv, psycopg2, hashlib, json

import sys
sys.path.append('..')
import config

pg = None
cursor = None
try:
    pg = psycopg2.connect("dbname='"+config.DB_NAME+"' user='"+config.DB_USER+"' host='"+config.DB_HOST+"' password='"+config.DB_PASSWORD+"'")
    cursor = pg.cursor()
except:
    print("I am unable to connect to the database")
    exit(0)

def get_calendar_binary_string(months):
    calendar=bytearray(48)
    for i in range(11):
        if months[i]=='S': calendar[11-i+12*3]=1
        if months[i]=='G': calendar[11-i+12*2]=1
        if months[i]=='H': calendar[11-i+12  ]=1
        if months[i]=='T': calendar[11-i     ]=1
    return calendar

species=dict()

#import species
with open('especes.csv', newline='', encoding='utf-8') as file:
    next(file) #skip first line (contains column headers)
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        id=None
        category=None
        tmp=row[1].strip()
        if tmp == 'Légume':     category='V'
        if tmp == 'Arômate':    category='H'
        if tmp == 'Auxiliaire': category='A'
        if tmp == 'Fleur':      category='O'
        if tmp == 'Fruit':      category='F'
        if tmp == 'Nuisible':   category='P'
        if tmp == 'Céréale':    category='C'
        if tmp == 'Arbres':      category='T'
        c=get_calendar_binary_string(row[5:])
        #print(row[0],'\t',row[1],'\t',category,'\t',c)
        cursor.execute("INSERT INTO specie (category, calendar) VALUES(%s, %s::bytea) RETURNING id", (category, get_calendar_binary_string(row[5:])))
        id=id_of_new_row = cursor.fetchone()[0]
        species[row[0]]=id
        #import names in french and latin
        french=row[2].title()
        cursor.execute("INSERT INTO name (plant,lang,name) VALUES(%s,'fre',%s)", (id, french))
        latin =row[3].title()
        if latin:
            cursor.execute("INSERT INTO name (plant,lang,name) VALUES(%s,'lat',%s)", (id, latin))
        cursor.execute("INSERT INTO media (hash, url, type) VALUES(%s,%s, 'R')", (hashlib.sha256(str.encode(row[4])).digest(), row[4]))
        pg.commit()

#import interactions between plants, insects and pests
with open('associations.csv', newline='', encoding='utf-8') as file:
    next(file) #skip first line (contains column headers)
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        t=True if row[1].strip()=='favorise' or row[1].strip()=='repousse' else False
        cursor.execute("INSERT INTO interaction (beneficial,specie1,specie2, sources) VALUES(%s, %s, %s, %s)", (t, species[row[0]], species[row[2]], json.dumps(row[3].strip() + ', ' + row[5].strip())))
        pg.commit()
