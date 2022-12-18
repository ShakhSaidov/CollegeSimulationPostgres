import psycopg2
import DataGenerator
import TableCreator

#TableCreator.createTables()
#DataGenerator.initializeStatic()
DataGenerator.initializeNonStatic("Fall", 2026, 100)

"""
# Connect to DB
conn = psycopg2.connect(
    host="localhost",
    database="Simulation",
    user="postgres",
    password="postgre$320")

cur = conn.cursor()

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

season = ["Fall","Spring"]

addition = 0
for year in range (2019,2020):
    for semester in season:
        print("It is "+semester+", "+str(year))
        DataGenerator.initializeNonStatic(semester, year, addition)
        addition += 100

# Capture the final state of the DB and put in the report

# display the PostgreSQL database server version
#db_version = cur.fetchone()
#print(db_version)

# close the communication with the PostgreSQL
cur.close()

conn.close()

"""


