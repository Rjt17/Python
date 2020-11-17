#!/usr/bin/env python
import os
os.chdir("/root/python_scripts")
usernamefile = open("/root/python_scripts/username")
passwordfile = open("/root/python_scripts/password")
username = usernamefile.read()
password = passwordfile.read()
n = 1

print("ENTER YOUR USERNAME AND YOUR PASSWORD.")
print

while n == 1:
	userinput = raw_input("USERNAME: ")
	passinput = raw_input("PASSWORD: ")
	if userinput == username and passinput == password:
		print("WELCOME")
		break
	else:
		print("USERNAME OR PASSWORD INCORRECT.")