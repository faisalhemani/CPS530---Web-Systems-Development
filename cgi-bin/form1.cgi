#!/usr/bin/perl 
 
use CGI':standard';
use strict; 
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 
 
print "Content-type: text/html\\n\\n"; 
 
my $fname = param('fname');
my $lname = param('lname'); 
my $gender = param('gender'); 
my $lang = param('lang');

print "<html>\n";
print "<head>\n"; 
print '<link rel="stylesheet" href="www2.scs.ryerson.ca/~mhemani/cgi-bin/lab4.css">'. "\n"; 
print "</head>\n";

print "<body>\n";

print "<h2> How Do You Code </h2>\n"; 
 
print "<h3>Hello $fname $lname ($gender) <br> Your favourite Language:$lang</h3>\n"; 
 
print "<h4>Thank You for Your Time!</h4>\n"; 

print "</body>\n";
print "</html>\n";
