#!/usr/bin/env python

import cgi
import os
import json
import sys

form = cgi.FieldStorage()
loggedinok = False

if form.getvalue('user') == 'bob' and form.getvalue('password') == 'hunter2':
	loggedinok=True
if 'loggedin=true' in os.environ['HTTP_COOKIE']:
	loggedinok=True
	
print "Content-type: text/html"
if loggedinok:
	print "Set-Cookie: loggedin=true"
print
print "<HTML><BODY><center><H1><font color='blue'>Hello, <font color='red'>world!</font></font></H1></center>"
print "<FORM method='POST'><INPUT name='user'/>"
print "	<INPUT name='password' type='password'>"
print "	<BUTTON tpye='submit'>Log in</BUTTON>"
print "</FORM>"
print "<P>Query string was: " + os.environ['QUERY_STRING'] + "</P>"
print "<P>Your browser is : " + os.environ['HTTP_USER_AGENT'] + "</P>"
#if os.environ['CONTENT_LENGTH']:
#	print "<P>Standard Input is: " + sys.stdin.read(int(os.environ['CONTENT_LENGTH'])) + "</P>"
print "<P>"
#print "User name was: " + form.getvalue('user') + ". "
#print "Password was: " + form.getvalue('password') + "."
print "</P>"
if loggedinok:
	print "<H2><center> LOG IN OK! </center></H2>"
	
cgi.print_environ()

print json.dumps(dict(os.environ), indent=4)

print "</BODY></HTML>"
