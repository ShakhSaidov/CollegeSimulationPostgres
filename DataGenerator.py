import psycopg2

def initializeStatic():
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
    addHallRoom(conn)
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
        cur.copy_from(f, 'course_attributes', sep=',')

    connection.commit()

# populating course information table
def addCourseInfo(connection):
    cur = connection.cursor()

    with open('Data/CourseProfile.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'course_profile', sep=',')

    connection.commit()

# populating course prerequisites table
def addCoursePrereq(connection):
    cur = connection.cursor()

    with open('Data/CoursePrereq.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'course_prerequisites', sep=',')

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
        cur.copy_from(f, 'hall_info', sep=',')

    connection.commit()

# populating residence hall rooms table
def addHallRoom(connection):
    cur = connection.cursor()

    with open('Data/HallRoom.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'hall_room', sep=',')

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
        cur.copy_from(f, 'library_items', sep=',')

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
        cur.copy_from(f, 'major_attribute_requirement', sep=',')

    connection.commit()

# populating major course requirement table
def addMajorCourseReq(connection):
    cur = connection.cursor()

    with open('Data/MajorCourseReq.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'major_course_requirement', sep=',')

    connection.commit()

# populating residence life staff table
def addResLifeStaff(connection):
    cur = connection.cursor()

    with open('Data/ResLifeStaff.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'reslife_staff', sep=',')

    connection.commit()

# populating staff profile table
def addStaffProfile(connection):
    cur = connection.cursor()

    with open('Data/StaffProfile.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'staff_profile', sep=',')

    connection.commit()

# populating student profile table
def addStudentProfile(connection):
    cur = connection.cursor()

    with open('Data/StudentProfile.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'student_profile', sep=',')

    connection.commit()

#||||||||||||||||||||||||||||||||||||
# NON-STATIC DATA
#||||||||||||||||||||||||||||||||||||

def initializeNonStatic():
    conn = psycopg2.connect(
        host="localhost",
        database="Simulation",
        user="postgres",
        password="postgre$320")

    addStudentClub(conn)

    conn.close()


# populating student club
def addStudentClub(connection):
    # studentsIDList = list of students ID (L number) from students table
    # clubIDList = list of club Ids from clubs table
    # membershipNames = list of names from general CSV file
    # amount = random number < studentsList.length
    # count = 1
    
    # while (count < amount):
    #   currID = studentsIDList[count]
    #   randomClub = random club chosen from clubIDList
    #   randomMembershipTitle = random membership title chosen from membershipNames
    #   
    #   cur = connection.cursor()
    #   cur.execute(INSERT INTO StudentClub Values ________ )
    #   connection.commit()

    return 0

# populating student club
def addStudentJob(connection):
    # studentsIDList = list of students ID (L number) from students table
    # JobList = list of jobs and their sponsorDepName from jobs table
    # amount = random number < studentsList.length
    # count = 1
    
    # while (count < amount):
    #   currID = studentsIDList[count]
    #   randomJob = random job chosen from jobList
    #   randomSponsorDepName = random sponsor name based on randomJob above
    #   
    #   cur = connection.cursor()
    #   cur.execute(INSERT INTO StudentJob Values ________ )
    #   connection.commit()

    return 0

# populating student club
def addEvents(connection):
    # eventNames = list from column from General CSV file
    # locations = list from column from General CSV file
    # dates = list from column from General CSV file

    # randomAmount = random number of events to add
    # count = 1
    
    # while (count < randomAmount):
    #   eventID = make a new random ID
    #   randomName = random name chosen from eventNames
    #   randomLocation = chosen from locations
    #   randomDates = chosen from dates

    #   cur = connection.cursor()
    #   cur.execute(INSERT INTO Events Values ________ )
    #   connection.commit()

    return 0