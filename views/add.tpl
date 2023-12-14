<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Employee</title>
</head>
<body>
    <h1>Add New Employee</h1>
    <form action="/add" method="post">
        <label for="employee_name">Employee Name:</label>
        <input type="text" id="employee_name" name="employee_name" required><br>

        <label for="company_name">Company Name:</label>
        <input type="text" id="company_name" name="company_name" required><br>

        <label for="department">Department:</label>
        <input type="text" id="department" name="department" required><br>

        <label for="salary">Salary:</label>
        <input type="number" id="salary" name="salary" required><br>

        <input type="submit" value="Add">
    </form>
    <p><a href="/">Back to List</a></p>
</body>
</html>
