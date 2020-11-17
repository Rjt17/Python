#!/usr/bin/env python
#test program:- flow test

yes =  "yes"
no = "no"

print("please enter only 'YES' or 'NO'")
print
print("is it raining?")
answer = input("yes or no: ")
if answer == yes:
	print("do you have an umbrella?")
	answer1 = input("yes or no: ")
	if answer1 == no:
		while answer1 == no:
			print("wait for a while.")
			print("is it still raining?")
			answer2 = input("yes or no: ")
			if answer2 != yes:
				print("go outside")
				break
	elif answer1 == yes:
		print("go outside")
	else:
		print("you didn't enter yes or no, now the program will terminate.")	
elif answer == no:
	print("go outside.")
else:
	print("you didn't enter yes or no, now the program will terminate.")
