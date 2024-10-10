<?php
// api.php: Handles incoming POST requests and saves data to MySQL

// Database connection settings
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "api";

// Create a connection to MySQL
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the POST data
    $player_name = $_POST['player_name'] ?? '';
    $win_status = $_POST['win_status'] ?? 0;  // 1 for win, 0 for loss
    $time_taken = $_POST['time_taken'] ?? 0;

    // Prepare the SQL statement
    $stmt = $conn->prepare("INSERT INTO game_results (player_name, win_status, time_taken) VALUES (?, ?, ?)");
    $stmt->bind_param("sii", $player_name, $win_status, $time_taken);

    // Execute the SQL statement
    if ($stmt->execute()) {
        echo json_encode(["status" => "success", "message" => "Score saved successfully."]);
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to save score."]);
    }

    // Close the statement
    $stmt->close();
}

// Close the database connection
$conn->close();
?>
