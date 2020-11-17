#!/usr/bin/env python

spam = ['apples', 'cats', 'tofu', 'animals']

def listtostring(list1):
	
	n = ""											#creates new variable named "n"
	
	if len(list1) > 1:
		list1.insert(-1,'and')						#inserts "and" in list1
	
	for i in range(len(list1) -1):					
		if len(list1) > 1:							#if length of list1 is greater than 1.
			n += list1[i] + ","						#applies this.
		else:
			print list1
	if len(list1) > 1:
		n += list1[-1]								# adds the last string of list
	rajat = n 											
	
	print rajat

listtostring(spam)