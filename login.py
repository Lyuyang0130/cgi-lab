#!/usr/bin/env python3
import cgi
import cgitb
from secret import username, password #this is the correct use name and password
from templates import login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie
import os,json

#Q1
print("******************Q1******************")
print(os.environ)
#json_object = json.dumps(dict(os.environ), indent = 4)
#print(json_object)

#Q2
print("******************Q2******************")
for param in os.environ.keys():
    if (param=="QUERY_STRING"):
        print("<b>%20s<b>: %s<br>" % (param, os.environ[param]))

#Q3
print("******************Q3******************")
for param in os.environ.keys():
    if param == "HTTP_USER_AGENT":
        print("<b>%20s<b>: %s<br>" % (param, os.environ[param]))

#Q4


#Create instance of FieldStorage
form = cgi.FieldStorage()

username_type = None
password_typ = None
#Get data from fields

username_type = form.getvalue('username')
password_type = form.getvalue('password')


#Q6
#if information right
if username_type==None and password_type == None:
    print(login_page())
else:
    if username_type==username and password_type == password:
        print("Content-type:text/html")
        print("Set-Cookie:flagID = 1\r\n")
        print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))
        for param in os.environ.keys():
            if param == 'HTTP_COOKIE':
                if 'flagID=1' in os.environ[param]:
                    print(secret_page(username_type,password_type))
    else:
        print(after_login_incorrect())
