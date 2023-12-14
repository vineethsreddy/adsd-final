import sqlite3

connection = sqlite3.connect("student_course_db.db")

def get_courses_and_students(course_id=None):
    cursor = connection.cursor()
    if course_id is None:
        rows = cursor.execute("SELECT students.StudentName, courses.CourseID, courses.CourseName, courses.Department, courses.Credits FROM courses LEFT JOIN students ON courses.CourseID = students.CourseID")
    else:
        rows = cursor.execute(f"SELECT students.StudentName, courses.CourseID, courses.CourseName, courses.Department, courses.Credits FROM courses LEFT JOIN students ON courses.CourseID = students.CourseID WHERE courses.CourseID={course_id}")
    rows = list(rows)
    rows = [{'StudentName': row[0], 'CourseID': row[1], 'CourseName': row[2], 'Department': row[3], 'Credits': row[4]} for row in rows]
    return rows

def add_course_and_student(student_name, course_name, department, credits):
    cursor = connection.cursor()
    
    # Add course
    cursor.execute(f"INSERT INTO courses (CourseName, Department, Credits) VALUES ('{course_name}', '{department}', {credits})")
    connection.commit()

    # Get the last inserted CourseID
    cursor.execute("SELECT last_insert_rowid()")
    course_id = cursor.fetchone()[0]

    # Add student
    cursor.execute(f"INSERT INTO students (StudentName, CourseID) VALUES ('{student_name}', {course_id})")
    connection.commit()

def update_course_and_student(course_id, student_name, course_name, department, credits):
    cursor = connection.cursor()

    # Update course
    cursor.execute(f"UPDATE courses SET CourseName='{course_name}', Department='{department}', Credits={credits} WHERE CourseID={course_id}")
    connection.commit()

    # Update student (assuming one student per course for simplicity)
    cursor.execute(f"UPDATE students SET StudentName='{student_name}' WHERE CourseID={course_id}")
    connection.commit()

def delete_course_and_student(course_id):
    cursor = connection.cursor()

    # Delete course
    cursor.execute(f"DELETE FROM courses WHERE CourseID={course_id}")
    
    # Also delete related student
    cursor.execute(f"DELETE FROM students WHERE CourseID={course_id}")
    
    connection.commit()

def set_up_database():
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS courses")
        cursor.execute("DROP TABLE IF EXISTS students")
    except:
        pass

    # Create the 'courses' table
    cursor.execute("CREATE TABLE courses (CourseID INTEGER PRIMARY KEY, CourseName TEXT, Department TEXT, Credits INTEGER)")

    # Create the 'students' table
    cursor.execute("CREATE TABLE students (StudentID INTEGER PRIMARY KEY, StudentName TEXT, CourseID INTEGER, FOREIGN KEY (CourseID) REFERENCES courses(CourseID))")

    # Insert sample data
    for course_data in [('Alice Smith', 'Computer Science Basics', 'Computer Science', 3),
                        ('Bob Johnson', 'Microeconomics', 'Economics', 4),
                        ('Charlie Brown', 'English Literature', 'English', 3),
                        ('David Davis', 'Calculus I', 'Mathematics', 4),
                        ('Eva White', 'General Psychology', 'Psychology', 3)]:
        add_course_and_student(*course_data)

    connection.commit()

def test_set_up_database():
    print("testing set_up_database()")
    set_up_database()
    items = get_courses_and_students()
    assert len(items) == 5
    course_ids = [item['CourseID'] for item in items]
    student_names = [item['StudentName'] for item in items]
    course_names = [item['CourseName'] for item in items]
    departments = [item['Department'] for item in items]
    credits = [item['Credits'] for item in items]

    print("Course IDs:", course_ids)
    print("Student Names:", student_names)
    print("Course Names:", course_names)
    print("Departments:", departments)
    print("Credits:", credits)

def test_get_courses_and_students():
    print("testing get_courses_and_students()")
    items = get_courses_and_students()
    assert type(items) is list
    assert len(items) > 0
    for item in items:
        assert type(item) is dict
        assert 'StudentName' in item
        assert type(item['StudentName']) is str
        assert 'CourseID' in item
        assert type(item['CourseID']) is int
        assert 'CourseName' in item
        assert type(item['CourseName']) is str
        assert 'Department' in item
        assert type(item['Department']) is str
        assert 'Credits' in item
        assert type(item['Credits']) is int

def test_add_course_and_student():
    print("testing add_course_and_student()")
    set_up_database()
    items = get_courses_and_students()
    original_length = len(items)
    add_course_and_student("History of Art", "Art", 3, "Renaissance Art")
    items = get_courses_and_students()
    assert len(items) == original_length + 1
    course_ids = [item['CourseID'] for item in items]
    student_names = [item['StudentName'] for item in items]
    course_names = [item['CourseName'] for item in items]
    departments = [item['Department'] for item in items]
    credits = [item['Credits'] for item in items]

    print("Course IDs:", course_ids)
    print("Student Names:", student_names)
    print("Course Names:", course_names)
    print("Departments:", departments)
    print("Credits:", credits)

def test_update_course_and_student():
    print("testing update_course_and_student()")
    set_up_database()
    items = get_courses_and_students()
    course_id = items[2]['CourseID']
    student_name = items[2]['StudentName']
    course_name = items[2]['CourseName']
    department = items[2]['Department']
    credits = items[2]['Credits']
    update_course_and_student(course_id, "New Student", "New Course", "New Department", 5)
    items = get_courses_and_students()
    assert items[2]['StudentName'] == "New Student"
    assert items[2]['CourseName'] == "New Course"
    assert items[2]['Department'] == "New Department"
    assert items[2]['Credits'] == 5
    course_ids = [item['CourseID'] for item in items]
    student_names = [item['StudentName'] for item in items]
    course_names = [item['CourseName'] for item in items]
    departments = [item['Department'] for item in items]
    credits = [item['Credits'] for item in items]

    print("Course IDs:", course_ids)
    print("Student Names:", student_names)
    print("Course Names:", course_names)
    print("Departments:", departments)
    print("Credits:", credits)

def test_delete_course_and_student():
    print("testing delete_course_and_student()")
    set_up_database()
    add_course_and_student("History of Art", "Art", 3, "Renaissance Art")
    items = get_courses_and_students()
    for item in items:
        if item['CourseName'] == 'History of Art':
            delete_course_and_student(item['CourseID'])
    items = get_courses_and_students()
    for item in items:
        assert item['CourseName'] != 'History of Art'
    course_ids = [item['CourseID'] for item in items]
    student_names = [item['StudentName'] for item in items]
    course_names = [item['CourseName'] for item in items]
    departments = [item['Department'] for item in items]
    credits = [item['Credits'] for item in items]

    print("Course IDs:", course_ids)
    print("Student Names:", student_names)
    print("Course Names:", course_names)
    print("Departments:", departments)
    print("Credits:", credits)

if __name__ == "__main__":
    test_set_up_database()
    test_get_courses_and_students()
    test_add_course_and_student()
    test_update_course_and_student()
    test_delete_course_and_student()
    print("done.")
