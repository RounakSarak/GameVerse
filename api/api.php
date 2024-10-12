<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "api";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $player_name = $_POST['player_name'] ?? '';
    $win_status = $_POST['win_status'] ?? 0;
    $time_taken = $_POST['time_taken'] ?? 0;

    $stmt = $conn->prepare("INSERT INTO game_results (player_name, win_status, time_taken) VALUES (?, ?, ?)");
    $stmt->bind_param("sii", $player_name, $win_status, $time_taken);

    if ($stmt->execute()) {
        echo json_encode(["status" => "success", "message" => "Score saved successfully."]);
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to save score."]);
    }

    $stmt->close();
}

$conn->close();
?>