import csv, psycopg2, hashlib

pg = None
try:
    pg = psycopg2.connect("dbname='monpotager' user='postgres' host='localhost' password='mysecretpassword'")
except:
    print("I am unable to connect to the database")
    exit(0)

def get_calendar_binary_string(months):
    calendar=0
    for i in range(11):
        if months[i]=='S': calendar|=2**(11-i+12*3)
        if months[i]=='G': calendar|=2**(11-i+12*2)
        if months[i]=='H': calendar|=2**(11-i+12  )
        if months[i]=='T': calendar|=2**(11-i     )
    return calendar

species=dict()

#import species
with open('especes.csv', newline='') as file:
    next(file)
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        id=None
        category=None
        if row[1] == 'Légume':     category='V'
        if row[1] == 'Arômate':    category='H'
        if row[1] == 'Auxiliaire': category='A'
        if row[1] == 'Fleur':      category='O'
        if row[1] == 'Fruit':      category='F'
        if row[1] == 'Nuisible':   category='P'
        if row[1] == 'Céréale':    category='C'
        c=get_calendar_binary_string(row[5:])
        print(row[0],'\t',c,'\t',format(c,'b'))
        sql="INSERT INTO specie (category, calendar) VALUES('%s', %s) RETURNING id" % (category, get_calendar_binary_string(row[5:]))
        #cursor.execute(sql)
        #id=id_of_new_row = cursor.fetchone()[0]
        species[row[0]]=id
        #import names in french and latin
        french=row[2].title()
        sql="INSERT INTO name (plant,lang,name) VALUES(%s,'fre','%s')" % (id, french)
        latin =row[3].title()
        print(sql)
        sql="INSERT INTO media (hash, url, type) VALUES('%s','%s', 'R')" % (hashlib.sha256(str.encode(row[4])).digest(), row[4])
        #cursor.execute(sql)
        #pg.commit()

#import interactions between plants, insects and pests
with open('associations.csv', newline='') as file:
    next(file)
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        t=True if row[1]=='favorise' or row[1]=='repousse' else False
        sql="INSERT INTO interaction (beneficial,specie1,specie2, sources) VALUES(%s, %s, %s, '%s')" % (t, species[row[0]], species[row[2]], row[3].strip() + ', ' + row[5])
        #cursor.execute(sql)
        #pg.commit()
