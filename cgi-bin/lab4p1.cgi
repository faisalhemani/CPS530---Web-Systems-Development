
#!/usr/bin/perl
use CGI':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 
use strict;
print "Content-type: text/html\n\n";
print <<ENDHTML;
<html>
	<head>
		<title>Hello World</title>
		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
		<!-- Optional theme -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
		<link rel="stylesheet" type="text/css" href="/Lab4/lab4.css" />
	</head>
	<body>
		<h2>This is my First <br> Perl Program</h2>
	</body>
</html>



ENDHTML



