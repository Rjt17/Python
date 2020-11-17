try:
	age = int(input())
	if age>=18:
		print("can cast")
	else:
		print("cannot cast")
except ValueError:
	print("enter a numeric value")