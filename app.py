from bottle import route, post, run, template, redirect, request
import database

# Call set_up_database to create tables and insert sample data
database.set_up_database()

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    # Fetch data from both tables using a JOIN
    items = database.get_courses_and_students()
    return template("list.tpl", data=items)

@route("/add")
def get_add():
    return template("add_course_student.tpl")

@post("/add")
def post_add():
    student_name = request.forms.get("student_name")
    course_name = request.forms.get("course_name")
    department = request.forms.get("department")
    credits = request.forms.get("credits")

    # Add course and student
    database.add_course_and_student(student_name, course_name, department, credits)
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    items = database.get_courses_and_students(id)
    return template("update_course_student.tpl", item=items[0])

@post("/update")
def post_update():
    student_name = request.forms.get("student_name")
    course_name = request.forms.get("course_name")
    department = request.forms.get("department")
    credits = request.forms.get("credits")
    id = request.forms.get("id")

    # Update course and student
    database.update_course_and_student(id, student_name, course_name, department, credits)
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    # Delete course and related students
    database.delete_course_and_student(id)
    redirect("/list")

run(host='localhost', port=8080)
