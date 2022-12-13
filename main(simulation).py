import psycopg2
#import DataGenerator

# Connect to DB
conn = psycopg2.connect(
    host="localhost",
    database="Simulation",
    user="postgres",
    password="postgre$320")

cur = conn.cursor()

# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)

# close the communication with the PostgreSQL
cur.close()

conn.close()

'''

def yearStart():
    cur.execute(DataGenerator.addStudents())
    cur.execute(DataGenerator.addClasses())
    ...


def yearMiddle():
    cur.execute(DataGenerator.assignGrades())
    cur.execute(DataGenerator.changeHalls())
    ...


def yearEnd():
    cur.execute(DataGenerator.levelUpStudents())
    cur.execute(DataGenerator.assignGrades())
    ...

# initialization()
season = ["Fall","Spring"]

for year in range (2015,2020):
    for semester in season:
        print("It is "+semester+", "+str(year))
        yearStart()
        yearMiddle()
        yearEnd()

# Capture the final state of the DB and put in the report

'''

