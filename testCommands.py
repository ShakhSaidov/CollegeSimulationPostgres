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

    """CREATE TABLE clubMembers(
        lNumber         INT NOT NULL,
        clubID          INT NOT NULL,
        title           VARCHAR(1024) NOT NULL,
        PRIMARY KEY(lNumber)
    )"""
)
degreeCompletion = (
    """CREATE TABLE staffProfile(
        lNumber         INT NOT NULL,
        department      VARCHAR(1024) NOT NULL,
        fName           VARCHAR(1024) NOT NULL,
        mName           VARCHAR(1024) NOT NULL,
        lName           VARCHAR(1024) NOT NULL,
        dob             VARCHAR(1024) NOT NULL,
        email           VARCHAR(1024) NOT NULL,
        phoneNo         VARCHAR(1024) NOT NULL,
        emergencyNo     INT NOT NULL,
        PRIMARY KEY(lNumber)
    )""",

    """CREATE TABLE majorAttributeRequirement(
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

    """CREATE TABLE gradeReport(
        lNumber         INT NOT NULL,
        sectNum         INT NOT NULL,
        grade           VARCHAR(1024) NOT NULL,
        PRIMARY KEY(lNumber)
    )""",

    """CREATE TABLE courseProfile(
        courseCRN       INT NOT NULL,
        courseSect      INT NOT NULL,
        courseName      VARCHAR(1024) NOT NULL,
        courseCredit    INT NOT NULL,
        courseDept      VARCHAR(1024) NOT NULL,
        instructor      VARCHAR(1024) NOT NULL,
        location        VARCHAR(1024) NOT NULL,
        numStudents     INT NOT NULL,
        PRIMARY KEY(courseCRN)
    )""",

    """CREATE TABLE majorCourseRequirement(
        major           VARCHAR(1024) NOT NULL,
        reqCourseCRN    INT NOT NULL
    )""",

    """CREATE TABLE courseAtt(
        courseCRN       INT NOT NULL,
        courseAtt       INT NOT NULL
    )""",

    """CREATE TABLE prerequisit(
        courseCRN       INT NOT NULL,
        prereqCRN       INT NOT NULL
    )""",

    """CREATE TABLE studentCourses(
        lNumber         INT NOT NULL,
        semester        VARCHAR(1024) NOT NULL,
        year            INT NOT NULL,
        sectNum         INT NOT NULL,
        PRIMARY KEY(lNumber)
    )""",

    """CREATE TABLE major(
        majorName       VARCHAR(1024) NOT NULL,
        majorDept       VARCHAR(1024) NOT NULL,
        numCourseGrad   INT NOT NULL
    )""",

    """CREATE TABLE jobs(
        jobName         VARCHAR(1024) NOT NULL,
        deptName        VARCHAR(1024) NOT NULL,
        facultyName     VARCHAR(1024) NOT NULL,
        jobDescr        VARCHAR(1024) NOT NULL,
        comp            INT NOT NULL,
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

    """CREATE TABLE libraryItems(
        itemID          INT NOT NULL,
        itemType        VARCHAR(1024) NOT NULL,
        itemName        VARCHAR(1024) NOT NULL,
        libraryID       INT NOT NULL,
        PRIMARY KEY(itemID)
    )""",

    """CREATE TABLE libraryServices(
        serviceID       INT NOT NULL,
        lNumber         INT NOT NULL,
        serviceName     VARCHAR(1024) NOT NULL,
        libraryID       INT NOT NULL,
        PRIMARY KEY(serviceID)
    )""",

    """CREATE TABLE libraryLoans(
        itemID          INT NOT NULL,
        libraryID       INT NOT NULL,
        lNumber         INT NOT NULL,
        dateOut         VARCHAR(1024) NOT NULL,
        dateDue         VARCHAR(1024) NOT NULL,
        dateIn          VARCHAR(1024) NOT NULL,
        PRIMARY KEY(itemId)
    )"""
)
residenceHalls = (
    """CREATE TABLE hallInfo(
        hallName        VARCHAR(1024) NOT NULL,
        tier            INT NOT NULL,
        capacity        INT NOT NULL,
        coed            VARCHAR(1024) NOT NULL,
        addressName     VARCHAR(1024) NOT NULL,
        addressNum      INT NOT NULL,
        hallType        VARCHAR(1024) NOT NULL,
        accessibility   VARCHAR(1024) NOT NULL,
        laundry         INT NOT NULL,
        kitchen         INT NOT NULL,
        PRIMARY KEY(hallName)
    )""",

    """CREATE TABLE hallRoom(
        hallName        VARCHAR(1024) NOT NULL,
        roomNumber      INT NOT NULL,
        roomType        VARCHAR(1024) NOT NULL,
        ac              BOOLEAN NOT NULL,
        occupants       INT NOT NULL,
        PRIMARY KEY(hallName)
    )""",

    """CREATE TABLE resLifeStaff(
        hallName        VARCHAR(1024) NOT NULL,
        nameRA          VARCHAR(1024) NOT NULL,
        headRA          VARCHAR(1024) NOT NULL,
        PRIMARY KEY(hallName)
    )"""
)
students = (
    """CREATE TABLE studentProfile(
        lNumber         INT NOT NULL,
        fName           VARCHAR(1024) NOT NULL,
        mName           VARCHAR(1024) NOT NULL,
        lName           VARCHAR(1024) NOT NULL,
        dob             DATE NOT NULL,
        major           VARCHAR(1024) NOT NULL,
        email           VARCHAR(1024) NOT NULL,
        year            VARCHAR(1024) NOT NULL,
        phone           VARCHAR(1024) NOT NULL,
        emergencyNum    VARCHAR(1024) NOT NULL,
        PRIMARY KEY(lNumber)
    )""",

    """CREATE TABLE studentSemester(
        lNumber         INT NOT NULL,
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

    """CREATE TABLE studentJob(
        lNumber         INT NOT NULL,
        title           VARCHAR(1024) NOT NULL,
        sponsor         VARCHAR(1024) NOT NULL
    )""",

    """CREATE TABLE studentClub(
        lNumber         INT NOT NULL,
        clubID          INT NOT NULL,
        memTitle        VARCHAR(1024) NOT NULL
    )"""
)