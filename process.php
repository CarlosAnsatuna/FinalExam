<?php
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['giftIndices'])) {
    // Get the gift indices 
    $giftIndices = $_GET['giftIndices'];

    // Command to call the Python script
    $command = escapeshellcmd("python3 gift_selector.py " . escapeshellarg($giftIndices));

    // Execute the command and capture the output
    $output = shell_exec($command);

    // Display the result
    echo "<h1>Selected Gifts and Unique Code</h1>";
    echo "<pre>$output</pre>";
} else {
    echo "Invalid request. Please provide gift indices.";
}
?>
