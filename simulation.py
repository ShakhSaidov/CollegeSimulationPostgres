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
addition = 50

#Populating global college campus data that will not change throughout the simulation
DataGenerator.populateGlobalData(conn)

"""
DataGenerator.initializeSemesterStart("Fall", 2026, addition, conn)
DataGenerator.initializeSemesterEnd("Fall", 2026, conn)
DataGenerator.initializeSemesterStart("Spring", 2026, addition+100, conn)
DataGenerator.initializeSemesterEnd("Spring", 2026, conn)
"""

#Simulation loop, 10 years from 2022-2032
for year in range (2022,2032):
    for semester in season:
        print("Current Time: " + semester + ", " + str(year))
        
        DataGenerator.initializeSemesterStart(semester, year, addition, conn)
        DataGenerator.initializeSemesterEnd(semester, year, conn)

        addition += 50

# Closing the connection to the Database
cur.close()
conn.close()


