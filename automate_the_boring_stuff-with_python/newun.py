#!/usr/bin/env python

#dictionay birthday

birthdays = {
			'rajat': 'august 17',
			'archi': 'february 21',
			'mummy': 'october 23',
			'papa': 'march 28',
			}

while True:
	print("please enter a name " + "(or enter nothing to stop.)")
	name = raw_input()
	if name == "":
		break
	
	if name in birthdays:
		print (birthdays[name] + " is the birthday of " + name)
	else:
		print("the entered name is not in our databse.")
		print("please enter the birthdate of " + name)
		bdate = raw_input()
		birthdays[name] = bdate
		print("databse updated.")

