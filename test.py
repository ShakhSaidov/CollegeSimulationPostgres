import psycopg2


def initialize():
    conn = psycopg2.connect(
        host="localhost",
        database="Simulation",
        user="postgres",
        password="postgre$320")

    addLibrariesTest(conn)

    conn.close()


def addLibrariesTest(connection):
    cur = connection.cursor()

    cur.execute("""
        CREATE TABLE test(
        Library_ID integer PRIMARY KEY,
        Library_Name text,
        St_Address_Name text,
        St_Address_Number integer
    )
    """)

    with open('Data/LibrariesTest.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'test', sep=',')

    connection.commit()
