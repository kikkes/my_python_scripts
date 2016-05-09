<?php
header('Content-Type: application/json');

$link = mysqli_connect("localhost", "root","", "episeries");
/* check connection */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}


	//require_once('connect.php');     // You have access to $db_server here.
   
	//$email = $_POST["email"];
	//$password = $_POST["password"];
	$email = "kim@episeries.com";
	$password = "lol";
	
	mysqli_query($link, "INSERT INTO `users`(`email`, `password`) VALUES ('".$email."','".$password."')");
	
	
	
	mysqli_close($link);
	
?>