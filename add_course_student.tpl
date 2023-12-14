<html>
<head>
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

        form {
            width: 50%; /* Adjust the width of the form */
            margin-top: 20px; /* Optional margin from the top */
        }

        label {
            display: block;
            margin: 10px 0;
        }

        input, select {
            width: calc(100% - 20px); /* Adjust the width of the input fields */
            padding: 8px;
            margin: 5px 0;
            box-sizing: border-box;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }
  </style>
</head>
<body>
<h2>Add New Student and Course</h2>
<hr/>
<form action="/add" method="post">
  <p>Student Name: <input name="student_name" required/></p>
  <p>Course Name: <input name="course_name" required/></p>
  <p>Department: <input name="department" required/></p>
  <p>Credits: <input name="credits" type="number" required/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
<a href="/">Back to List</a>
<hr/>
</body>
</html>
