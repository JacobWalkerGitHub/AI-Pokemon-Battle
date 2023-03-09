import csv

# Opens pokemon list and gathers data
try:
    f = open('pokemon-data.csv', 'r')
except IOError:
    print('cannot open it')
lines = csv.DictReader(f)
pname = []
ptype = []
php = []
pattack = []
pdefense = []
pmoves = []

for line in lines:
    pname.append(line['Name'])
    ptype.append(line['Type'])
    php.append(line['HP'])
    pattack.append(line['Attack'])
    pdefense.append(line['Defense'])
    pmoves.append(line['Moves'])
f.close() # closes pokemon list

# Opens moves list and gathers data
try:
    m = open('moves-data.csv', 'r')
except IOError:
    print('cannot open it')
rows = csv.DictReader(m)
mname = []
mtype = []
pp = []
power = []

for row in rows:
    mname.append(row['Name'])
    mtype.append(row['Type'])
    power.append(row['Power'])
m.close() # closed move lists





