<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Courses and Students</title>
</head>
<style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        h2 {
            margin-top: 20px; /* Adjust the margin as needed */
        }

        table {
            border-collapse: collapse;
            width: 80%; /* Adjust the width as needed */
            margin-top: 20px; /* Optional margin from the top */
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }
</style>
<body>
    <h2>Courses and Students</h2>
    <table border="1">
        <tr>
            <th>Course ID</th>
            <th>Student Name</th>
            <th>Course Name</th>
            <th>Department</th>
            <th>Credits</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
        % for item in data:
            <tr>
                <td>{{item['CourseID']}}</td>
                <td>{{item['StudentName']}}</td>
                <td>{{item['CourseName']}}</td>
                <td>{{item['Department']}}</td>
                <td>{{item['Credits']}}</td>
                <td><a href="/update/{{item['CourseID']}}">Update</a></td>
                <td><a href="/delete/{{item['CourseID']}}">Delete</a></td>
            </tr>
        % end
    </table>
    <a href="/add">Add a new course and student</a>
</body>
</html>
