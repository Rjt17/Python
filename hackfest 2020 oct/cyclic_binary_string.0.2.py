binary_s = str(input())
if "1" not in binary_s:
	print(-1)

else:	
	binary_s = list(binary_s)
	zero = binary_s.count("0")
	one = binary_s.count("1")
	greatest = 0
	new_string = ""

	for x in range(0,one):
		new_string += "1"
	for x in range(0,zero):
		new_string += "0"

	decimal = int(new_string, 2)
	for power in range(len(new_string)+1, 0, -1):
		divisor = 2 ** power
		if decimal % divisor == 0:
			greatest = power
			break
	print(greatest)