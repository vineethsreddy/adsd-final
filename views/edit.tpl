<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Employee</title>
</head>
<body>
    <h1>Edit Employee</h1>
    <form action="/edit/{{ data[0] }}" method="post">
        <label for="employee_name">Employee Name:</label>
        <input type="text" id="employee_name" name="employee_name" value="{{ data[1] }}" required><br>

        <label for="company_name">Company Name:</label>
        <input type="text" id="company_name" name="company_name" value="{{ data[3] }}" required><br>

        <label for="department">Department:</label>
        <input type="text" id="department" name="department" value="{{ data[4] }}" required><br>

        <label for="salary">Salary:</label>
        <input type="number" id="salary" name="salary" value="{{ data[5] }}" required><br>

        <input type="submit" value="Update">
    </form>
    <p><a href="/">Back to List</a></p>
</body>
</html>
