import sqlite3

connection = sqlite3.connect("student_course_db.db")

cursor = connection.cursor()

# Fetch data from the 'courses' table
cursor.execute("SELECT CourseID, CourseName, Department, Credits FROM courses")
course_rows = list(cursor.fetchall())

# Fetch data from the 'students' table
cursor.execute("SELECT StudentID, StudentName, CourseID FROM students")
student_rows = list(cursor.fetchall())

print("Courses:")
print(course_rows)

print("\nStudents:")
print(student_rows)

# Combine the data into a single list of dictionaries
course_data = [{'CourseID': row[0], 'CourseName': row[1], 'Department': row[2], 'Credits': row[3]} for row in course_rows]
student_data = [{'StudentID': row[0], 'StudentName': row[1], 'CourseID': row[2]} for row in student_rows]

print("\nCombined Data:")
combined_data = []

for course in course_data:
    related_students = [student for student in student_data if student['CourseID'] == course['CourseID']]
    course_copy = course.copy()
    course_copy['Students'] = related_students
    combined_data.append(course_copy)

print(combined_data)
