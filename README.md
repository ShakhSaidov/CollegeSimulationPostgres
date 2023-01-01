# CollegeSimulationPostgres

The goal of this project is to design, maintain and simulate a database that mimics the data operations of a university. We achieved this by designing relations that represent university entities such as students, residence halls, degree completion, library services, and clubs. Data was generated randomly for these relations, and executed in a simulation that populated each relation in a realistic manner. An earlier report detailed the design of each relation, therefore, this report will only go over the implementation of the simulator program.
	
To run the simulation, install postgresql and python on your computer along with Python packages psycopg2, openpyxl, pandas. Then, create a user and password for postgresql database and connect to it. Below is an example of our connection:
	
	conn = psycopg2.connect( host="localhost", database="Simulation", user="postgres", password="postgre$320")

The main file that initiates the program is called “simulation.py”. To start the program, run python “simulation.py”.
	
Relations were separated into dynamic and static, as shown in Figure 1. Static relations (green) are populated before the simulation loop from the .csv files and represent university entities that do not change in the simulation such as residence halls and classes. To simulate the program, we generated 100 random student types using Mockaroo. Data from the .csv file are from data generated from Mockaroo and the programmer’s input. The simulation produces two residence halls, two majors, two libraries, and four clubs. The data for these entities are created randomly. Dynamic relations (yellow) depend on static relations and extraneous variables from the .csv file. Dynamic relations are populated with the simulation loop as they contain data that changes every semester.



simulation.py creates empty tables for all entities in the above lucid chart and connects to the database. The class populates global college campus data that will not change throughout the simulation. dataGenerator.py populates global college campus data and each table from the .csv files generated from Mockaroo and will not change throughout the simulation. The class will also add non-static data to the program. At the end of the simulation, the program will close the connection to the database. 
tableCreator.py creates tables with appropriate attributes and data types. To simulate the database, static relations are built before the simulation begins. Data population functions are called in a sequence that mimics a college’s data operation. Semesters are broken down into two periods, the stand and end of the semester. The simulation executes the functions below twenty times to simulate ten years of college:

    addStudentProfile(conn, addition)
Adds 50 randomly created students per semester into the database

    addStudentJobs(conn, addition)
Randomly assigns a student job

    addClubMembers(conn, addition)
Randomly makes a student join a random club

    addEvents(semester, year, conn)
Randomly creates a campus event with relevant information

    makeLibraryService(conn)
Randomly makes a student use a library service

    makeLibraryItemLoan(conn,year)
Randomly makes a student loan out a library item with all relevant information stored
At the end of the program:

    makeStudentsTakeCourses(semester, year, conn)
Randomly assigns every student 2 courses per semester, unless graduated

    giveStudentsGrades(conn)
Randomly assigns grades to each students’ courses for the current semester

    addStudentSemester(semester, year, conn)
Sums up all the relevant semester information of a student, with final term grades, meal plans, residence information

The simulation executes as intended and produces information from data operations of a university for ten years. At the end of the program, 13,000 course sections, 220 loans from the library, 1000 student jobs, and 32 events are assigned from the simulation. The program allows the user to extract data from the simulation, and identify information over the years of the simulation. Test functions in our project demonstrate the functionality of our program and represent data operations over ten years at a university. 
