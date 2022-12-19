import psycopg2
import DataGenerator
import TableCreator

#first, creating empty tables for all the entities we will be working with
TableCreator.createTables()

# Connecting to the Database
conn = psycopg2.connect(
    host="localhost",
    database="Simulation",
    user="postgres",
    password="postgre$320")

cur = conn.cursor()

season = ["Fall","Spring"]
addition = 100

#Populating global college campus data that will not change throughout the simulation
DataGenerator.populateGlobalData(conn)

#Simulation loop, 10 years from 2026-2035
for year in range (2026,2035):
    for semester in season:
        print("Current Time: " + semester + ", " + str(year))
        
        DataGenerator.initializeSemesterStart(semester, 2026, addition, conn)
        DataGenerator.initializeSemesterEnd(semester, 2026, conn)

        addition += 100


# Closing the connection to the Database
cur.close()
conn.close()


