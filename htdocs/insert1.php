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
$firstName = $_POST['firstName'];
$lastName = $_POST['lastName'];
$email = $_POST['email'];
$password = $_POST['password'];
$confirmPassword = $_POST['confirmPassword'];
$phoneNumber = $_POST['phoneNumber'];



// Insert data into the database
$sql = "INSERT INTO users (firstName,lastName,email,password,confirmPassword,phoneNumber ) VALUES 
('$firstName','$lastName', '$email','$password','$confirmPassword','$phoneNumber')";

if ($conn->query($sql) === TRUE) {
    echo "Record inserted successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close connection
$conn->close();
?>
