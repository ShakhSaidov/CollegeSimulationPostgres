import psycopg2
import random
import openpyxl

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

# ||||||||||||||||||||||||||||||||||||
# NON-STATIC DATA
# ||||||||||||||||||||||||||||||||||||


def initializeNonStatic():
    conn = psycopg2.connect(
        host="localhost",
        database="Simulation",
        user="postgres",
        password="postgre$320")

    addStudentJobs(conn)

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


def addStudentJobs(connection):
    cur = connection.cursor()
    connection.autocommit = True

    cur.execute("SELECT lnumber from student_profile")
    studentsList = cur.fetchall()
    studentsList = [x[0] for x in studentsList]

    cur.execute("SELECT jobname, deptname from jobs")
    jobsList = cur.fetchall()
    jobsList = [x[0] for x in jobsList]

    cur.execute("SELECT deptname from jobs")
    jobDeptNameList = cur.fetchall()
    jobDeptNameList = [x[0] for x in jobDeptNameList]

    studentWithJobsAmount = random.randint(0, len(studentsList) / 2)
    count = 1

    while (count < studentWithJobsAmount):
        currentStudent = studentsList[count]
        randomJob = random.randint(0, len(jobsList))

        currentJob = jobsList[randomJob-1]
        currentJobDeptName = jobDeptNameList[randomJob-1]

        query = """INSERT INTO student_job VALUES (%s,%s,%s)"""
        insertValues = (currentStudent, currentJob, currentJobDeptName)
        cur.execute(query, insertValues)

        count += 1


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

def makeStudentsTakeCourses(semester,year,conn):
    cur = conn.cursor()

    gettingStudentIds = "Select Major, lNumber FROM student_profile"

    cur.execute(gettingStudentIds)
    #print("Selecting rows from mobile table using cursor.fetchall")
    infos = cur.fetchall()

    for info in infos:
        # #print(info)
        major = info[0]
        id = info[1]
        studentCourses = "Select sectNum FROM student_courses WHERE lNumber="+str(id)
        cur.execute(studentCourses)
        sections = cur.fetchall()
        # if len(sections) > 0:
        #     print(sections[len(sections)-1][0])

        if len(sections) == 0:
            if major == "CS":
                csClasses = "Select courseSect FROM course_profile WHERE courseCRN=1001"
                cur.execute(csClasses)
                sections = cur.fetchall()
                max = len(sections)
                pickSection = random.randint(0,max-1)
                sectionNumber = sections[pickSection][0]
                fstCourse = sectionNumber
                # #print(fstCourse)
                csClasses = "Select courseSect FROM course_profile WHERE courseCRN=1002"
                cur.execute(csClasses)
                sections = cur.fetchall()
                max = len(sections)
                pickSection = random.randint(0,max-1)
                sectionNumber = sections[pickSection][0]
                sndCourse = sectionNumber
                # #print(sndCourse)
                insertCourse1 = "INSERT INTO student_courses Values("+str(id)+",'"+semester+"',"+str(year)+",1001,"+str(fstCourse)+")"
                insertCourse2 = "INSERT INTO student_courses Values("+str(id)+",'"+semester+"',"+str(year)+",1002,"+str(sndCourse)+")"
                print(insertCourse1)
                print(insertCourse2)
                cur.execute(insertCourse1)
                conn.commit()
                cur.execute(insertCourse2)
                conn.commit()
            if major == "ECON":
                csClasses = "Select courseSect FROM course_profile WHERE courseCRN=2001"
                cur.execute(csClasses)
                sections = cur.fetchall()
                max = len(sections)
                pickSection = random.randint(0,max-1)
                sectionNumber = sections[pickSection][0]
                fstCourse = sectionNumber
                #print(fstCourse)
                csClasses = "Select courseSect FROM course_profile WHERE courseCRN=2002"
                cur.execute(csClasses)
                sections = cur.fetchall()
                max = len(sections)
                pickSection = random.randint(0,max-1)
                sectionNumber = sections[pickSection][0]
                sndCourse = sectionNumber
                #print(sndCourse)
                insertCourse1 = "INSERT INTO student_courses Values("+str(id)+",'"+semester+"',"+str(year)+",2001,"+str(fstCourse)+")"
                insertCourse2 = "INSERT INTO student_courses Values("+str(id)+",'"+semester+"',"+str(year)+",2002,"+str(sndCourse)+")"
                print(insertCourse1)
                print(insertCourse2)
                cur.execute(insertCourse1)
                conn.commit()
                cur.execute(insertCourse2)
                conn.commit()
            if major == "MATH":
                csClasses = "Select courseSect FROM course_profile WHERE courseCRN=3001"
                cur.execute(csClasses)
                sections = cur.fetchall()
                max = len(sections)
                pickSection = random.randint(0,max-1)
                sectionNumber = sections[pickSection][0]
                fstCourse = sectionNumber
                #print(fstCourse)
                csClasses = "Select courseSect FROM course_profile WHERE courseCRN=3002"
                cur.execute(csClasses)
                sections = cur.fetchall()
                max = len(sections)
                pickSection = random.randint(0,max-1)
                sectionNumber = sections[pickSection][0]
                sndCourse = sectionNumber
                #print(sndCourse)
                insertCourse1 = "INSERT INTO student_courses Values("+str(id)+",'"+semester+"',"+str(year)+",3001,"+str(fstCourse)+")"
                insertCourse2 = "INSERT INTO student_courses Values("+str(id)+",'"+semester+"',"+str(year)+",3002,"+str(sndCourse)+")"
                print(insertCourse1)
                print(insertCourse2)
                cur.execute(insertCourse1)
                conn.commit()
                cur.execute(insertCourse2)
                conn.commit()
        else:
            lastSection = sections[len(sections)-1][0]
            last_digit = int(repr(lastSection)[-2])
            isOne = int(repr(lastSection)[-3])
            if last_digit+2 > 6 and isOne == 1:
                print("the student have graduated")
            else:
                csClasses = "Select courseCRN FROM student_courses WHERE sectNum="+str(lastSection)
                cur.execute(csClasses)
                courses = cur.fetchall()
                course = courses[0][0]
                course1 = course+1
                course2 = course+2
                csClasses = "Select courseSect FROM course_profile WHERE courseCRN="+str(course1)
                cur.execute(csClasses)
                sections = cur.fetchall()
                max = len(sections)
                pickSection = random.randint(0,max-1)
                sectionNumber = sections[pickSection][0]
                fstCourse = sectionNumber
                #print(fstCourse)
                csClasses = "Select courseSect FROM course_profile WHERE courseCRN="+str(course2)
                cur.execute(csClasses)
                sections = cur.fetchall()
                max = len(sections)
                pickSection = random.randint(0,max-1)
                sectionNumber = sections[pickSection][0]
                sndCourse = sectionNumber
                # print("here:"+str(sndCourse))
                insertCourse1 = "INSERT INTO student_courses Values("+str(id)+",'"+semester+"',"+str(year)+","+str(course1)+","+str(fstCourse)+")"
                insertCourse2 = "INSERT INTO student_courses Values("+str(id)+",'"+semester+"',"+str(year)+","+str(course2)+","+str(sndCourse)+")"
                print(insertCourse1)
                print(insertCourse2)
                cur.execute(insertCourse1)
                conn.commit()
                cur.execute(insertCourse2)
                conn.commit()

def giveStudentsGrades(conn):
    cur = conn.cursor()
    for info in infos:
        # print(info)
        major = info[0]
        id = info[1]
        studentCourses = "Select sectNum FROM student_courses WHERE lNumber="+str(id)
        cur.execute(studentCourses)
        sections = cur.fetchall()
        beforeLastCourse = sections[len(sections)-2][0]
        lastCourse = sections[len(sections)-1][0]

        grade1 = general("Grade")
        grade2 = general("Grade")

        insertGrade1 = "INSERT INTO grade_report Values("+str(id)+","+str(beforeLastCourse)+","+str(grade1)+")"
        insertGrade2 = "INSERT INTO grade_report Values("+str(id)+","+str(lastCourse)+","+str(grade2)+")"
        print(insertGrade1)
        print(insertGrade2)
        cur.execute(insertGrade1)
        conn.commit()
        cur.execute(insertGrade2)
        conn.commit()

def general(colName):
    path = "C://Users//User//Desktop//CS320//FinalProject//CollegeSimulationPostgres//Data//General.xlsx"

    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj["Sheet1"]  

    generalCols = {}
    col = 1
    row = 1
    while(sheet_obj.cell(column=col, row=1).value != None):
        name = sheet_obj.cell(column=col, row=1).value
        generalCols[name] = col
        col = col + 1 

    colist = ["A","B","C","D","E","F","G","H","I",]

    colNum = generalCols[colName]
    colIndex = colNum -1

    colLength = 0
    for cell in sheet_obj[colist[colIndex]]:
        if cell.value == None:
            break
        colLength = colLength + 1

    row = random.randint(2,colLength)
    value = sheet_obj.cell(column=colNum, row=row).value
    return value
