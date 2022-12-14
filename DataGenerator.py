import psycopg2

def initialize():
    conn = psycopg2.connect(
        host="localhost",
        database="Simulation",
        user="postgres",
        password="postgre$320")

    addClubs(conn)
    addCourseAtt(conn)
    addCourseInfo(conn)
    addCoursePrereq(conn)
    addDepartments(conn)
    addHallInfo(conn)
    addHallInfo(conn)
    addJobs(conn)
    addLibraries(conn)
    addLibraryItems(conn)
    addMajor(conn)
    addMajorAttReq(conn)
    addMajorCourseReq(conn)
    addResLifeStaff(conn)
    addStaffProfile(conn)
    addStudentProfile(conn)

    conn.close()

# populating clubs table
def addClubs(connection):
    cur = connection.cursor()

    with open('Data/Clubs.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'clubs', sep=',')

    connection.commit()

# populating course attributes table
def addCourseAtt(connection):
    cur = connection.cursor()

    with open('Data/CourseAtt.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'courseAtt', sep=',')

    connection.commit()

# populating course information table
def addCourseInfo(connection):
    cur = connection.cursor()

    with open('Data/CourseInfo.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'courseInfo', sep=',')

    connection.commit()

# populating course prerequisites table
def addCoursePrereq(connection):
    cur = connection.cursor()

    with open('Data/CoursePrereq.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'coursePrereq', sep=',')

    connection.commit()

# populating departments table
def addDepartments(connection):
    cur = connection.cursor()

    with open('Data/Departments.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'departments', sep=',')

    connection.commit()

# populating residence hall information table
def addHallInfo(connection):
    cur = connection.cursor()

    with open('Data/HallInfo.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'hallInfo', sep=',')

    connection.commit()

# populating residence hall rooms table
def addHallRoom(connection):
    cur = connection.cursor()

    with open('Data/HallRoom.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'hallRoom', sep=',')

    connection.commit()

# populating jobs table
def addJobs(connection):
    cur = connection.cursor()

    with open('Data/Jobs.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'jobs', sep=',')

    connection.commit()

# populating libraries table
def addLibraries(connection):
    cur = connection.cursor()

    with open('Data/Libraries.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'libraries', sep=',')

    connection.commit()

# populating library items table
def addLibraryItems(connection):
    cur = connection.cursor()

    with open('Data/LibraryItems.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'libraryItems', sep=',')

    connection.commit()

# populating major table
def addMajor(connection):
    cur = connection.cursor()

    with open('Data/Major.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'major', sep=',')

    connection.commit()

# populating major attribute requirement table
def addMajorAttReq(connection):
    cur = connection.cursor()

    with open('Data/MajorAttReq.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'majorAttReq', sep=',')

    connection.commit()

# populating major course requirement table
def addMajorCourseReq(connection):
    cur = connection.cursor()

    with open('Data/MajorCourseReq.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'majorCourseReq', sep=',')

    connection.commit()

# populating residence life staff table
def addResLifeStaff(connection):
    cur = connection.cursor()

    with open('Data/ResLifeStaff.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'resLifeStaff', sep=',')

    connection.commit()

# populating staff profile table
def addStaffProfile(connection):
    cur = connection.cursor()

    with open('Data/StaffProfile.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'staffProfile', sep=',')

    connection.commit()

# populating student profile table
def addStudentProfile(connection):
    cur = connection.cursor()

    with open('Data/StudentProfile.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'studentProfile', sep=',')

    connection.commit()