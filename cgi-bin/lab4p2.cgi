#!/usr/bin/perl
use CGI':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 
use strict;
print "Content-type: text/html\n\n";
print <<ENDHTML;
<html>
	<head>
		<title>from</title>
		<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="/Lab4/lab4.css">
	</head>
	<body>
		<form action="http://www2.scs.ryerson.ca/~mhemani/cgi-bin/form1.cgi" method="get">
			First name: <br> <input  type="text" name="fname" placeholder="Bob"><br>
			Last name: <br> <input type="text" name="lname" placeholder="Marley"><br>
			Gender: <br> <input type="radio" name="gender" value="male"> Male<br>
			<input type="radio" name="gender" value="female"> Female<br>
			<input type="radio" name="gender" value="other"> Other<br>
			Favorite Coding Language: <br>
			<select>
			<option value="HTML / CSS">HTML / CSS</option>
			<option value="Java">Java</option>
			<option value="Javascript">JavaScript</option>
			<option value="C">C</option>
			<option value="Objective C / Swift">Objective C / Swift</option>
			<option value="C#">C#</option>
			<option value="Python">Python</option>
			</select>
			<input style="color:#000000;" type="submit" value="Submit">
		</form>
	</body>
</html>

ENDHTML


