import psycopg2

clubs = (
    """CREATE TABLE clubs(
        clubID          INT NOT NULL,
        clubName        VARCHAR(1024) NOT NULL,
        clubHead        VARCHAR(1024) NOT NULL,
        website         VARCHAR(1024) NOT NULL,
        email           VARCHAR(1024) NOT NULL,
        phone           VARCHAR(1024) NOT NULL,
        PRIMARY KEY(clubID)
    )""",

    """CREATE TABLE events(
        eventID         INT NOT NULL,
        eventName       VARCHAR(1024) NOT NULL,
        location        VARCHAR(1024) NOT NULL,
        date            VARCHAR(1024) NOT NULL,
        clubID          INT NOT NULL,
        PRIMARY KEY(eventID)
    )""",

    """CREATE TABLE club_members(
        lNumber         BIGINT NOT NULL,
        clubID          INT NOT NULL,
        memTitle        VARCHAR(1024) NOT NULL,
        PRIMARY KEY(lNumber, clubID)
    )"""
)
degreeCompletion = (
    """CREATE TABLE staff_profile(
        lNumber         BIGINT NOT NULL,
        department      VARCHAR(1024) NOT NULL,
        fName           VARCHAR(1024) NOT NULL,
        mName           VARCHAR(1024) NOT NULL,
        lName           VARCHAR(1024) NOT NULL,
        dob             VARCHAR(1024) NOT NULL,
        email           VARCHAR(1024) NOT NULL,
        phoneNo         VARCHAR(1024) NOT NULL,
        emergencyNo     VARCHAR(1024) NOT NULL,
        PRIMARY KEY(lNumber)
    )""",

    """CREATE TABLE major_attribute_requirement(
        major           VARCHAR(1024) NOT NULL,
        attrName        VARCHAR(1024) NOT NULL
    )""",

    """CREATE TABLE departments(
        name            VARCHAR(1024) NOT NULL,
        location        VARCHAR(1024) NOT NULL,
        head            VARCHAR(1024) NOT NULL,
        numStudents     INT NOT NULL,
        PRIMARY KEY(name)
    )""",

    """CREATE TABLE grade_report(
        lNumber         BIGINT NOT NULL,
        sectNum         INT NOT NULL,
        grade           VARCHAR(1024) NOT NULL,
        PRIMARY KEY(lNumber, sectNum)
    )""",

    """CREATE TABLE course_profile(
        courseCRN       INT NOT NULL,
        courseSect      INT NOT NULL,
        courseName      VARCHAR(1024) NOT NULL,
        courseCredit    INT NOT NULL,
        courseDept      VARCHAR(1024) NOT NULL,
        instructor      VARCHAR(1024) NOT NULL,
        location        VARCHAR(1024) NOT NULL,
        numStudents     INT NOT NULL,
        PRIMARY KEY(courseCRN, courseSect)
    )""",

    """CREATE TABLE major_course_requirement(
        major           VARCHAR(1024) NOT NULL,
        reqCourseCRN    INT NOT NULL
    )""",

    """CREATE TABLE course_attributes(
        courseCRN       INT NOT NULL,
        courseAtt       VARCHAR(1024) NOT NULL
    )""",

    """CREATE TABLE course_prerequisites(
        courseCRN       INT NOT NULL,
        prereqCRN       INT NOT NULL
    )""",

    """CREATE TABLE student_courses(
        lNumber         BIGINT NOT NULL,
        semester        VARCHAR(1024) NOT NULL,
        year            INT NOT NULL,
        courseCRN       INT NOT NULL,
        sectNum         INT NOT NULL,
        PRIMARY KEY(lNumber, courseCRN)
    )""",

    """CREATE TABLE major(
        majorName       VARCHAR(1024) NOT NULL,
        majorDept       VARCHAR(1024) NOT NULL,
        numCourseGrad   INT NOT NULL,
        PRIMARY KEY(majorName)
    )""",

    """CREATE TABLE jobs(
        jobName         VARCHAR(1024) NOT NULL,
        deptName        VARCHAR(1024) NOT NULL,
        facultyName     VARCHAR(1024) NOT NULL,
        jobDescr        VARCHAR(1024) NOT NULL,
        comp            DECIMAL NOT NULL,
        hours           INT NOT NULL,
        PRIMARY KEY(jobName)
    )"""
)
libraryServices = (
    """CREATE TABLE libraries(
        libraryID       INT NOT NULL,
        libraryName     VARCHAR(1024) NOT NULL,
        addressName     VARCHAR(1024) NOT NULL,
        addressNum      INT NOT NULL,
        PRIMARY KEY(libraryID)
    )""",

    """CREATE TABLE library_items(
        itemID          INT NOT NULL,
        itemType        VARCHAR(1024) NOT NULL,
        itemName        VARCHAR(1024) NOT NULL,
        libraryID       INT NOT NULL,
        PRIMARY KEY(itemID)
    )""",

    """CREATE TABLE library_services(
        serviceID       INT NOT NULL,
        lNumber         BIGINT NOT NULL,
        serviceName     VARCHAR(1024) NOT NULL,
        libraryID       INT NOT NULL,
        PRIMARY KEY(serviceID)
    )""",

    """CREATE TABLE library_loans(
        itemID          INT NOT NULL,
        libraryID       INT NOT NULL,
        lNumber         BIGINT NOT NULL,
        dateOut         VARCHAR(1024) NOT NULL,
        dateDue         VARCHAR(1024) NOT NULL,
        dateIn          VARCHAR(1024) NOT NULL,
        PRIMARY KEY(itemId)
    )"""
)
residenceHalls = (
    """CREATE TABLE hall_info(
        hallName        VARCHAR(1024) NOT NULL,
        tier            INT NOT NULL,
        capacity        INT NOT NULL,
        coed            VARCHAR(1024) NOT NULL,
        addressNum      INT NOT NULL,
        addressName     VARCHAR(1024) NOT NULL,
        hallType        VARCHAR(1024) NOT NULL,
        accessibility   VARCHAR(1024) NOT NULL,
        laundry         INT NOT NULL,
        kitchen         INT NOT NULL,
        PRIMARY KEY(hallName)
    )""",

    """CREATE TABLE hall_room(
        hallName        VARCHAR(1024) NOT NULL,
        roomNumber      INT NOT NULL,
        roomType        VARCHAR(1024) NOT NULL,
        ac              BOOLEAN NOT NULL,
        occupants       INT NOT NULL,
        PRIMARY KEY(hallName, roomNumber)
    )""",

    """CREATE TABLE reslife_staff(
        hallName        VARCHAR(1024) NOT NULL,
        nameRA          VARCHAR(1024) NOT NULL,
        headRA          VARCHAR(1024) NOT NULL,
        PRIMARY KEY(hallName, nameRA)
    )"""
)
students = (
    """CREATE TABLE student_profile(
        lNumber         BIGINT NOT NULL,
        department      VARCHAR(1024) NOT NULL,
        fName           VARCHAR(1024) NOT NULL,
        lName           VARCHAR(1024) NOT NULL,
        dob             DATE NOT NULL,
        major           VARCHAR(1024) NOT NULL,
        email           VARCHAR(1024) NOT NULL,
        year            VARCHAR(1024) NOT NULL,
        phone           VARCHAR(1024) NOT NULL,
        emergencyNum    VARCHAR(1024) NOT NULL,
        PRIMARY KEY(lNumber)
    )""",

    """CREATE TABLE student_semester(
        lNumber         BIGINT NOT NULL,
        semester        VARCHAR(1024) NOT NULL,
        year            INT NOT NULL,
        financial       VARCHAR(1024) NOT NULL,
        enrolStatus     VARCHAR(1024) NOT NULL,
        mealPlan        INT NOT NULL,
        termGPA         INT NOT NULL,
        resHall         VARCHAR(1024) NOT NULL,
        resHallNum      INT NOT NULL,
        roomNum         INT NOT NULL,
        addressName     VARCHAR(1024) NOT NULL,
        addressNum      INT NOT NULL,
        PRIMARY KEY(lNumber)
    )""",

    """CREATE TABLE student_job(
        lNumber         BIGINT NOT NULL,
        title           VARCHAR(1024) NOT NULL,
        sponsor         VARCHAR(1024) NOT NULL,
        PRIMARY KEY(lNumber, title)
    )"""
)

# creating all the tables needed
def createTables():
    createTable(clubs)
    createTable(degreeCompletion)
    createTable(libraryServices)
    createTable(residenceHalls)
    createTable(students)

# functoin that creates tables based on the bassed entity array
def createTable(entities):
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="Simulation",
            user="postgres",
            password="postgre$320")

        cur = conn.cursor()

        for entity in entities:
            cur.execute(entity)

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
