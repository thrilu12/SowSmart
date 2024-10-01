<?php
// Database configuration
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "ourdb";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve data from the form
$username = $_POST['email'];
$password = $_POST['password'];

// Validate user credentials
$sql = "SELECT * FROM users WHERE email = '$username' AND password = '$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Successful login
    header("Location: dashboard.html"); // Redirect to the welcome page
    exit();
} else {
    // Failed login
    echo "Invalid username or password";
    echo $username;
    echo $password;
}

// Close connection
$conn->close();
?>
