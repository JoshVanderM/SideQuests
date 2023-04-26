#!/usr/bin/python

# to access POST values
import cgi

# to access python files in Python folder
import sys
sys.path.append("../Python")

# to save the data to the database
from users import Users
from users import get_new_id

# get the username and password from the POST
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# generate a new user_id
user_id = get_new_id(username, password);

# create a new user object
new_user = Users(user_id, username, password, "name", "occupation", "0000-00-00", 0, 0)

# save that user to the database
database_username = "root"
database_password = "Sidequests123!!"
new_user.save(database_username, database_password)
