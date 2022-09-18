import sqlite3

conn = sqlite3.connect('Naruto.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS Naruto (
    Personaje TEXT PRIMARY KEY,
    NinjaRenegado REAL NOT NULL,
    Ninja REAL NOT NULL,
    Konoha REAL NOT NULL,
    OtraAldea REAL NOT NULL,
    Clan REAL NOT NULL,
    NoClan REAL NOT NULL,
    Hombre REAL NOT NULL,
    Mujer REAL NOT NULL,
    Vivo REAL NOT NULL,
    Muerto REAL NOT NULL) """)

# Quitarle los ''' del inicio y del final en caso de que no exista la database, la primera vez que haya
# corrido el código vuelva a colocar las ''' para evitar errores.
'''c.execute("INSERT INTO Naruto VALUES ('Naruto', 0, 1, 1, 0, 1, 0, 1, 0, 1, 0)")
c.execute("INSERT INTO Naruto VALUES ('Sasuke', 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)")
c.execute("INSERT INTO Naruto VALUES ('Itachi', 1, 0, 1, 0, 1, 0, 1, 0, 0, 1)")
c.execute("INSERT INTO Naruto VALUES ('Anko', 1, 0, 1, 0, 0, 1, 0, 1, 1, 0)")
c.execute("INSERT INTO Naruto VALUES ('Tayuya', 1, 0, 1, 0, 0, 1, 0, 1, 0, 1)")
c.execute("INSERT INTO Naruto VALUES ('Orochimaru', 1, 0, 1, 0, 0, 1, 1, 0, 1, 0)")
c.execute("INSERT INTO Naruto VALUES ('Kabuto', 1, 0, 1, 0, 0, 1, 1, 0, 0, 1)")
c.execute("INSERT INTO Naruto VALUES ('Kisame', 1, 0, 0, 1, 1, 0, 1, 0, 0, 1)")
c.execute("INSERT INTO Naruto VALUES ('Konan', 1, 0, 0, 1, 0, 1, 0, 1, 0, 1)")
c.execute("INSERT INTO Naruto VALUES ('Nagato', 1, 0, 0, 1, 0, 1, 1, 0, 0, 1)")
c.execute("INSERT INTO Naruto VALUES ('Hinata', 0, 1, 1, 0, 1, 0, 0, 1, 1, 0)")
conn.commit()
print('--- Se ha creado la base de datos ---')'''

c.execute("SELECT * FROM Naruto")
Naruto = c.fetchall()

database = []

for row in Naruto:
    database.append({'personaje': row[0], 'ninja_renegado': bool(row[1]), 'ninja': bool(row[2]), 'konoha': bool(row[3]), 'otra_aldea': bool(
        row[4]), 'clan': bool(row[5]), 'no_clan': bool(row[6]), 'hombre': bool(row[7]), 'mujer': bool(row[8]), 'vivo': bool(row[9]), 'muerto': bool(row[10])},)

print('\n')
print('-------------------------------------- Bienvenid@ a Adivina Quién versión Naruto --------------------------------------\n')

with open('naruto.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())

print('\n')
print('\t\t\t\t--- Forma de jugar ---')
print('\t\t\t\tColoca la siguiente letra de acuerdo a tu decisión:')
print('\t\t\t\tY ----> Sí')
print('\t\t\t\tN ----> No\n\n\n')


def option(answer, property):
    if answer == "Y":
        nswr = True
    else:
        nswr = False

    to_remove = []
    for i in database:
        if i[property] != nswr:
            to_remove.append(i)

    for j in to_remove:
        database.remove(j)

# La variable nswr nos va a ayudar con el bool dentro de la base de datos


# Pregunta 1
nswr = input('¿Tu personaje es un ninja renegado?\n')
nswr = nswr.upper()
option(nswr, 'ninja_renegado')
if nswr == 'Y':
    nswr_1 = 1
else:
    nswr_1 = 0

# Pregunta 2
nswr = input('¿Tu personaje es un ninja?\n')
nswr = nswr.upper()
option(nswr, 'ninja')
if nswr == 'Y':
    nswr_2 = 1
else:
    nswr_2 = 0

# Pregunta 3
nswr = input('¿Tu personaje es de Konoha?\n')
nswr = nswr.upper()
option(nswr, 'konoha')
if nswr == 'Y':
    nswr_3 = 1
else:
    nswr_3 = 0

# Pregunta 4
nswr = input('¿Tu personaje es de otra aldea\n')
nswr = nswr.upper()
option(nswr, 'otra_aldea')
if nswr == 'Y':
    nswr_4 = 1
else:
    nswr_4 = 0

nswr = input('¿Tu pertenece a un clan?\n')
nswr = nswr.upper()
option(nswr, 'clan')
if nswr == 'Y':
    nswr_5 = 1
else:
    nswr_5 = 0

nswr = input('¿Tu personaje no pertenece a un clan?\n')
nswr = nswr.upper()
option(nswr, 'no_clan')
if nswr == 'Y':
    nswr_6 = 1
else:
    nswr_6 = 0

nswr = input('¿Tu personaje es hombre?\n')
nswr = nswr.upper()
option(nswr, 'hombre')
if nswr == 'Y':
    nswr_7 = 1
else:
    nswr_7 = 0

nswr = input('¿Tu personaje es mujer?\n')
nswr = nswr.upper()
option(nswr, 'mujer')
if nswr == 'Y':
    nswr_8 = 1
else:
    nswr_8 = 0

nswr = input('¿Tu personaje está vivo?\n')
nswr = nswr.upper()
option(nswr, 'vivo')
if nswr == 'Y':
    nswr_9 = 1
else:
    nswr_9 = 0

nswr = input('¿Tu personaje está muerto?\n')
nswr = nswr.upper()
option(nswr, 'muerto')
if nswr == 'Y':
    nswr_10 = 1
else:
    nswr_10 = 0

if len(database) == 1:
    print('El personaje que pensabas es: ' + database[0]['personaje'])
else:
    print('No supe qué personaje pensabas. :(\n')
    nswr_11 = input('Dime, ¿cuál era el personaje que tenías en mente?\n')
    c.execute('INSERT INTO Naruto VALUES (?,?,?,?,?,?,?,?,?,?,?)', (nswr_11, nswr_1,
              nswr_2, nswr_3, nswr_4, nswr_5, nswr_6, nswr_7, nswr_8, nswr_9, nswr_10))
    conn.commit()

conn.close()
