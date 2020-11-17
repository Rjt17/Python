#!/usr/bin/env python
#this is supposed to be a calculator app in CLI environment.
#uses only +,-,/,*.

yes = "y"
no = "n"

def first():
	print "enter a number"
	first_n = raw_input()
	print
	print "enter an operator"
	operator_f = raw_input()
	print
	print "enter second number"
	second_n = raw_input()
	print

	try:
		if operator_f == "+" :
			answer = float(first_n) + float(second_n)
			print answer
			print "this is without decimal points " + str(int(answer))
		elif operator_f == "-" :
			answer1 = float(first_n) - float(second_n)
			print answer1
			print "this is without decimal points " + str(int(answer1))
		elif operator_f == "*" :
			answer2 = float(first_n) * float(second_n)
			print answer2
			print "this is without decimal points " + str(int(answer2))
		elif operator_f == "/" :
			answer3 = float(first_n) / float(second_n)
			print answer3
			print "this is without decimal points " + str(int(answer3))
		else:
			print "please enter an operator."
	except ZeroDivisionError:
		print "Error: you can't divide a number by 0"
	except ValueError:
		print "Error: you didn't enter an integer."


def con():
	while True:
		print "do you want to operate another pair of numbers?"
		con_ans = raw_input("Y or N: ")
		if con_ans == yes:
			first()
		elif con_ans == no:
			print "bye bye."
			break
		else:
			print "please enter Y or N"


print "enter a number"
first_n = raw_input()
print
print "enter an operator"
operator_f = raw_input()
print
print "enter second number"
second_n = raw_input()
print

try:
	if operator_f == "+" :
		answer = float(first_n) + float(second_n)
		print answer
		print "this is without decimal points " + str(int(answer))
		con()
	elif operator_f == "-" :
		answer1 = float(first_n) - float(second_n)
		print answer1
		print "this is without decimal points " + str(int(answer1))
		con()
	elif operator_f == "*" :
		answer2 = float(first_n) * float(second_n)
		print answer2
		print "this is without decimal points " + str(int(answer2))
		con()
	elif operator_f == "/" :
		answer3 = float(first_n) / float(second_n)
		print answer3
		print "this is without decimal points " + str(int(answer3))
		con()
	else:
		print "please enter an operator."
		for i in range(1,6):
			first()
		con()
except ZeroDivisionError:
	print "Error: you can't divide a number by 0"
except ValueError:
	print "Error: you didn't enter an integer."







