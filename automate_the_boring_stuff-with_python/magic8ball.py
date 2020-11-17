#!/usr/bin/env python
import random

def magic_ball(answer):
	if answer == "1":
		return "it is certain"
	elif answer == "2":
		print "maybe"
	elif answer == "3":
		print "i will think about it"
	elif answer == "4":
		print "ofcourse not"
	elif answer == "5":
		print "try again later"
	elif answer == "6":
		print "not available"
	elif answer == "7":
		print "not interested"
	elif answer == "8":
		print "better luck next time"
	elif answer == "":
		return "not none"
r = raw_input()
rajat = magic_ball(r)
print rajat