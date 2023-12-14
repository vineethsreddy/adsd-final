import sqlite3

connection = sqlite3.connect("student_course_db.db")

cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS courses")
    cursor.execute("DROP TABLE IF EXISTS students")
except Exception as e:
    print(f"Error dropping tables: {e}")

# Create the 'courses' table
try:
    cursor.execute("CREATE TABLE courses (CourseID INTEGER PRIMARY KEY, CourseName TEXT, Department TEXT, Credits INTEGER)")
except Exception as e:
    print(f"Error creating 'courses' table: {e}")

# Create the 'students' table
try:
    cursor.execute("CREATE TABLE students (StudentID INTEGER PRIMARY KEY, StudentName TEXT, CourseID INTEGER, FOREIGN KEY (CourseID) REFERENCES courses(CourseID))")
except Exception as e:
    print(f"Error creating 'students' table: {e}")

# Insert sample data into 'courses' table
courses_data = [('Computer Science Basics', 'Computer Science', 3),
                ('Microeconomics', 'Economics', 4),
                ('English Literature', 'English', 3),
                ('Calculus I', 'Mathematics', 4),
                ('General Psychology', 'Psychology', 3)]

for course_data in courses_data:
    try:
        cursor.execute("INSERT INTO courses (CourseName, Department, Credits) VALUES (?, ?, ?)", course_data)
    except Exception as e:
        print(f"Error inserting data into 'courses' table: {e}")

# Insert sample data into 'students' table
students_data = [('John Doe', 1),
                 ('Jane Smith', 2),
                 ('Bob Johnson', 1),
                 ('Alice Williams', 3),
                 ('Charlie Brown', 4)]

for student_data in students_data:
    try:
        cursor.execute("INSERT INTO students (StudentName, CourseID) VALUES (?, ?)", student_data)
    except Exception as e:
        print(f"Error inserting data into 'students' table: {e}")

connection.commit()
connection.close()
print("done.")
