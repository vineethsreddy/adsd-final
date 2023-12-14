<!DOCTYPE html>
<html>
<head>
    <title>Update Course and Student</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            flex-direction: column; /* Add this line */
        }

        h2 {
            margin-bottom: 20px; /* Add some margin between h2 and the form */
        }

        form {
            width: 300px; /* Adjust the width as needed */
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin-bottom: 8px;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-bottom: 15px;
            box-sizing: border-box;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h2>Update Course and Student</h2>

    <form action="/update" method="post">
        <!-- Add a hidden input field for the course ID -->
        <input type="hidden" name="id" value="{{str(item['CourseID'])}}"/>

        <label for="student_name">Student Name:</label>
        <input type="text" name="student_name" value="{{item['StudentName']}}" required/>

        <label for="course_name">Course Name:</label>
        <input type="text" name="course_name" value="{{item['CourseName']}}" required/>

        <label for="department">Department:</label>
        <input type="text" name="department" value="{{item['Department']}}" required/>

        <label for="credits">Credits:</label>
        <input type="text" name="credits" value="{{item['Credits']}}" required/>

        <button type="submit">Update</button>
    </form>
</body>
</html>
