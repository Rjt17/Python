import string
import random
import time
import sys
import os

password = ""
length = 0
list_password = []

def load_animation(given_str): 

	load_str = given_str
	ls_len = len(load_str) 
 
	animation = "|/-\\"
	anicount = 0
	counttime = 0
	i = 0					

	while (counttime != 80): 
		time.sleep(0.075) 
		load_str_list = list(load_str) 
		x = ord(load_str_list[i])
		y = 0

		if x != 32 and x != 46:			 
			if x>90: 
				y = x-32
			else: 
				y = x + 32
			load_str_list[i]= chr(y) 

		res =''			 
		for j in range(ls_len): 
			res = res + load_str_list[j] 
			
		sys.stdout.write("\r"+res + animation[anicount]) 
		sys.stdout.flush() 
		load_str = res 

		anicount = (anicount + 1)% 4
		i =(i + 1)% ls_len 
		counttime = counttime + 1


def chooser():
	values = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
	values2 = list(random.choice(values))
	real_value = random.choice(values2)
	return real_value

print("Welcome to password generator")
print("Please enter the length of password you want")

while length<8:
	length = int(input())
	if length < 8:
		print("Minimum length should be 8\nplease try again")


print()
print("Please enter the number of passwords you want")
iterations = int(input())
print()

load_animation("generating passwords please wait...")
print("\n")

def creater():
	global password
	global length
	global list_password
	password += random.choice(list(string.ascii_lowercase))
	password += random.choice(list(string.ascii_uppercase))
	password += random.choice(list(string.digits))
	password += random.choice(list(string.punctuation))


	for x in range(0, int(length)-4):
		password += chooser()

	list_password.append(password)
	password = ""

for x in range(0, iterations):
	creater()

for x in list_password:
	print("[+] "+x)
	time.sleep(0.5)

print("\nThankyou for using this application")
time.sleep(3)
sys.exit()