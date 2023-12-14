import sqlite3
from bottle import Bottle, template, request, redirect

app = Bottle()
db_path = "employee_company_db.db"

def create_tables():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Create the 'company' table
    cursor.execute("CREATE TABLE IF NOT EXISTS company (CompanyID INTEGER PRIMARY KEY, CompanyName TEXT, Department TEXT, Salary INTEGER)")

    # Create the 'employee' table
    cursor.execute("CREATE TABLE IF NOT EXISTS employee (EmployeeID INTEGER PRIMARY KEY, EmployeeName TEXT, CompanyID INTEGER, FOREIGN KEY (CompanyID) REFERENCES company(CompanyID))")

    connection.commit()
    connection.close()

# Create tables if not exists
create_tables()

@app.route('/')
def index():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Fetch data from the joined tables
    cursor.execute("SELECT employee.EmployeeID, employee.EmployeeName, company.CompanyID, company.CompanyName, company.Department, company.Salary FROM employee LEFT JOIN company ON employee.CompanyID = company.CompanyID")
    data = cursor.fetchall()

    connection.close()

    return template('index', data=data)

@app.route('/add', method='GET')
def add_form():
    return template('add')

@app.route('/add', method='POST')
def add():
    employee_name = request.forms.get('employee_name')
    company_name = request.forms.get('company_name')
    department = request.forms.get('department')
    salary = request.forms.get('salary')

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Insert into 'company' table
    cursor.execute("INSERT INTO company (CompanyName, Department, Salary) VALUES (?, ?, ?)", (company_name, department, salary))
    company_id = cursor.lastrowid

    # Insert into 'employee' table
    cursor.execute("INSERT INTO employee (EmployeeName, CompanyID) VALUES (?, ?)", (employee_name, company_id))

    connection.commit()
    connection.close()

    redirect('/')

@app.route('/edit/<employee_id>', method='GET')
def edit_form(employee_id):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Fetch data for the selected employee
    cursor.execute("SELECT employee.EmployeeID, employee.EmployeeName, company.CompanyID, company.CompanyName, company.Department, company.Salary FROM employee LEFT JOIN company ON employee.CompanyID = company.CompanyID WHERE employee.EmployeeID=?", (employee_id,))
    data = cursor.fetchone()

    connection.close()

    return template('edit', data=data)

@app.route('/edit/<employee_id>', method='POST')
def edit(employee_id):
    employee_name = request.forms.get('employee_name')
    company_name = request.forms.get('company_name')
    department = request.forms.get('department')
    salary = request.forms.get('salary')

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Update 'company' table
    cursor.execute("UPDATE company SET CompanyName=?, Department=?, Salary=? WHERE CompanyID=?", (company_name, department, salary, employee_id))

    # Update 'employee' table
    cursor.execute("UPDATE employee SET EmployeeName=? WHERE EmployeeID=?", (employee_name, employee_id))

    connection.commit()
    connection.close()

    redirect('/')

# ... (previous code)

# ... (previous code)

# ... (previous code)

# ... (previous code)

from bottle import redirect

@app.route('/search', method='GET')
def search():
    search_company = request.query.get('search_company')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Fetch data from the joined tables based on the search
    cursor.execute("SELECT employee.EmployeeID, employee.EmployeeName, company.CompanyID, company.CompanyName, company.Department, company.Salary FROM employee LEFT JOIN company ON employee.CompanyID = company.CompanyID WHERE company.CompanyName LIKE ?", (f"%{search_company}%",))
    data = cursor.fetchall()

    connection.close()

    return template('search_results', data=data, search_company=search_company)



@app.route('/delete/<employee_id>')
def delete(employee_id):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Delete from 'company' table
    cursor.execute("DELETE FROM company WHERE CompanyID=?", (employee_id,))

    # Also delete from 'employee' table
    cursor.execute("DELETE FROM employee WHERE EmployeeID=?", (employee_id,))

    connection.commit()
    connection.close()

    redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
