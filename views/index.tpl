<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee-Company App</title>
</head>
<body>
    <h1>Employee-Company App</h1>

    <!-- Search Bar -->
    <form action="/search" method="get">
        <label for="search_company">Search by Company Name:</label>
        <input type="text" id="search_company" name="search_company" required>
        <input type="submit" value="Search">
    </form>

    <table border="1">
        <thead>
            <tr>
                <th>Employee ID</th>
                <th>Employee Name</th>
                <th>Company ID</th>
                <th>Company Name</th>
                <th>Department</th>
                <th>Salary</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            % for row in data:
                <tr>
                    <td>{{ row[0] }}</td>
                    <td>{{ row[1] }}</td>
                    <td>{{ row[2] }}</td>
                    <td>{{ row[3] }}</td>
                    <td>{{ row[4] }}</td>
                    <td>{{ row[5] }}</td>
                    <td>
                        <a href="/edit/{{ row[0] }}">Edit</a>
                        <a href="/delete/{{ row[0] }}" onclick="return confirm('Are you sure you want to delete this record?')">Delete</a>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
    <p><a href="/add">Add New Employee</a></p>
</body>
</html>
